from PIL import Image,ImageDraw, ImageFont, ImageFilter
import random
import matplotlib.pyplot as plt
import os
import cv2
import numpy as np
import sys
import time
import queue
import traceback
import string
import captcha_create_to_folder

#显示两张图片,用于观察对比
def image_show_two(img1,img2):
    #用来正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']
    #实例化一个fig
    #也就是一个画板
    fig = plt.figure("图片处理前后对比")
    #给画板设置一个标题
    fig.suptitle("图片处理前后对比", fontsize=20)
    #subplot(123)
    #1代表行  2代表列  3代表行列分割后的区域序号
    #这个是2行1列
    # 第一个区域
    ax = plt.subplot(211)
    #子区域的标题
    ax.set_title("处理前")
    #子区域显示的内容
    plt.imshow(img1)
    ax = plt.subplot(212)
    ax.set_title("处理后")
    plt.imshow(img2)
    plt.show()

#图片二值化
def image_binary(img):
    def get_bin_table(threshold=140):
        """
        获取灰度转二值的映射table
        :param threshold:
        :return:
        """
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        return table
    # 转化为灰度图
    imgry = img.convert('L')  
    table = get_bin_table()
    img_binary_result = imgry.point(table, '1')
    return img_binary_result

#图片去燥
def image_denoise(img):
    """传入二值化后的图片进行降噪"""
    #图片边缘最外层的一个像素不予考虑
    #九宫格形式
    #一个黑点周围超过5个白点,自测测试,可适当调整阈值.
    #就把黑点改成白点
    img_temp=img.copy()
    pixdata = img_temp.load()
    w,h = img_temp.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] == 1:#上
                count = count + 1
            if pixdata[x,y+1] == 1:#下
                count = count + 1
            if pixdata[x-1,y] == 1:#左
                count = count + 1
            if pixdata[x+1,y] == 1:#右
                count = count + 1
            if pixdata[x-1,y-1] == 1:#左上
                count = count + 1
            if pixdata[x-1,y+1] == 1:#左下
                count = count + 1
            if pixdata[x+1,y-1] == 1:#右上
                count = count + 1
            if pixdata[x+1,y+1] == 1:#右下
                count = count + 1
            if count > 5:
                pixdata[x,y] = 1
    # 进行一次膨胀
    w,h=img_temp.size
    pixdata = img_temp.load()
    offset = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
    try:
        col_xy=[]
        for x in range(2,w-1):
            for y in range(2,h-1):
                if pixdata[x,y] == 1:
                    count=0
                    for x_offset,y_offset in offset:
                        x_cop,y_cop = x+x_offset,y+y_offset
                        if pixdata[x_cop,y_cop] == 0:
                            count+=1
                    if count>1:
                        col_xy.append((x,y))
                        break
        for xy in col_xy:
            pixdata[xy[0],xy[1]] = 0

    except Exception:
        print('****************traceback.format_exc():****************\n%s' % traceback.format_exc())
        pass
    return img_temp

#裁剪图片无用的边缘部分
def image_cut_useless_part(img):
    w,h = img.size   
    #左右各裁剪1/6
    #上下各裁剪3个像素
    left=int(w*1/6)
    right=int(w*5/6)
    upper=int(3)
    lower=int(h-3)
    region = (left, upper, right, lower)
    crop_img = img.crop(region)
    return crop_img

#把图片切成四份,每份一个字符
#使用投影法切割
#投影法就是,想象一下,图片上所有像素都垂直落到地上,就形成了一摞一摞的,
#中间空白的地方就是分割图片的位置
#写出来,投影法,试了一下,效果不太好
#改为CFS连通域分割法
# def image_cut_4(img):
#     def vertical(img):
#         """传入二值化后的图片进行垂直投影"""
#         img_temp=img.copy()
#         pixdata = img_temp.load()
#         w,h = img.size
#         ver_list = []
#         # 开始投影
#         for x in range(w):
#             black = 0
#             for y in range(h):
#                 if pixdata[x,y] == 0:
#                     black += 1
#             ver_list.append(black)
#         #图片中可能还有未清除的噪点
#         #如果投影的某个位置左右邻居的投影都是0,该投影部分视为噪点,置为0
#         #部分噪点太粗,有两个像素.
#         times=len(ver_list)-6
#         plt.imshow(img_temp)
#         print(ver_list)
        
#         for i in range(2,times):
#             if ver_list[i]!=0:
#                 left_count=0
#                 right_count=0
#                 if ver_list[i-1]==0:
#                     left_count+=1
#                 if ver_list[i-2]==0:
#                     left_count+=1
#                 if ver_list[i+1]==0:
#                     right_count+=1
#                 if ver_list[i+2]==0:
#                     right_count+=1
#                 if left_count>0 and right_count>0:
#                     ver_list[i]=0
#         # 判断边界
#         #left,right
#         l,r = 0,0
#         #flag表示左边界是否确定
#         flag = False
#         cuts = []
#         for i,count in enumerate(ver_list):
#             # 阈值这里为0
#             #第一个有黑点的位置是起点,待切割字符的左边.
#             #先确定起点,再确定终点
#             if flag is False and count > 0:
#                 l = i
#                 flag = True
#             if flag and count == 0:
#                 r = i-1
#                 flag = False
#                 cuts.append((l,r))
#         return cuts
#     def img_cut_char(left, upper, right, lower):
#         left=int(left)
#         right=int(right)
#         upper=int(upper)
#         lower=int(lower)
#         region = (left, upper, right, lower)
#         crop_img = img.crop(region)
#         return crop_img
    
#     #这是列表,列表中是元组
#     vertical_result=vertical(img)
#     #切割四次
#     w,h = img.size
#     img_char_list=[]
#     for i in range(len(vertical_result)):
#         left=vertical_result[i][0]
#         right=vertical_result[i][1]
#         upper=0
#         lower=h-1
#         img_char=img_cut_char(left, upper, right, lower)
#         img_char_list.append(img_char)
#     return img_char_list

#CFS连通域分割法
#原理:遍历图片每个像素,当黑点不再连接黑点,就是分割点
def cfs(img):
    pixdata = img.load()
    w,h=img.size
    print(w,h)
    info=''
    for y in range(h):
        for x in range(w):
            # print(x,y,pixdata[x,y])
            info=info+str(pixdata[x,y])
        info=info+'\n'
    im = img.getdata()
    print(im)
    with open('二值图.txt','w') as f:
        f.write(info)



    """传入二值化后的图片进行连通域分割"""
    img_temp=img.copy()
    pixdata = img_temp.load()
    w,h = img.size
    #visited记录的是已经检查过的点,黑点白点都有
    visited = set()
    #队列中记录的是黑点,没有白点
    q = queue.Queue()
    #八个方向,九宫格
    # 123
    # 456
    # 789
    #x轴右为正方向
    #y轴下位正方向
    #            1       2      3      4     6      7     8     9
    offset = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
    cuts = []
    #axis轴
    x_axis = []
    #思路
    #先遍历一次图片,如果找到第一个黑点,就开始连通域算法,找到这个黑点的连通域,如果这个连通域面积小于阈值,那么视为噪点
    for x in range(w):
        for y in range(h):
            try:
                if pixdata[x,y] == 0 and (x,y) not in visited:
                    q.put((x,y))
                    visited.add((x,y))
                    x_axis.append(x)
            except Exception:
                print('****************traceback.format_exc():****************\n%s' % traceback.format_exc())
                pass
            #在while循环中,会对队列中的每个黑点,做九宫格检查
            #如果有黑点,就加入到队列中,一直循环直到没有连续的黑点
            #这时候我们就可以切割了
            #但先要验证一下该连通域是不是噪点,
            #设定一个阈值,如果少于这个阈值,那这个连通域就是噪点
            #重新找下一个连通域
            black_point_count=1
            threshold=20
            while not q.empty():
                x_current,y_current=q.get()
                for x_offset,y_offset in offset:
                    #current_offset_point
                    x_cop,y_cop = x_current+x_offset,y_current+y_offset
                    if (x_cop,y_cop) in visited:
                        continue
                    visited.add((x_cop,y_cop))
                    try:
                        if pixdata[x_cop,y_cop] == 0:
                            # if len(cuts)>2:
                            #     print(x_cop,y_cop)
                            #     time.sleep(1)
                            black_point_count+=1
                            q.put((x_cop,y_cop))
                            x_axis.append(x_cop)
                    except Exception:
                        # print('****************traceback.format_exc():****************\n%s' % traceback.format_exc())
                        pass
            if black_point_count>threshold:
                #连通域正常,添加一个连通域
                min_x,max_x = min(x_axis),max(x_axis)
                cuts.append((min_x,max_x))
            x_axis=[]

    print(cuts)
    # sys.exit()
                
    return img,cuts

def image_cut_cfs(cfs_result):
    img=cfs_result[0]
    w,h = img.size   
    img_chars=[]
    for x_axis in (cfs_result[1]):
        left=int(x_axis[0])
        right=int(x_axis[1])
        upper=int(0)
        lower=int(h-1)
        region = (left, upper, right, lower)
        crop_img = img.crop(region)
        img_chars.append(crop_img)
        print('图片裁剪x轴各个区域分别是:',left,right)
    return img_chars


#显示图片,用于观察对比
def image_show_4(img_list):
    #用来正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']
    #实例化一个fig
    #也就是一个画板
    fig = plt.figure("分割后的字符")
    #给画板设置一个标题
    fig.suptitle("分割后的字符", fontsize=20)
    #subplot(123)
    #1代表行  2代表列  3代表行列分割后的区域序号
    #这个是2行1列
    # 第一个区域
    print('*'*88)
    print('图片被切割成%d个字符'%len(img_list))
    # for i in range(len(img_list)):
    #     ax = plt.subplot('41%d'%(i+1))
    #     #子区域的标题
    #     ax.set_title("第%d个"%(i+1))
    #     #子区域显示的内容
    #     plt.imshow(img_list[i])
    for i in range(len(img_list)):
        if len(img_list)>4:
            break
        serial_number=int('41%d'%(i+1,))
        ax = plt.subplot(serial_number)
        plt.imshow(img_list[i])
    # ax = plt.subplot('415')
    # plt.imshow(img_list[4])
    plt.show()
    

#归一化
def normalization(img):
    size=(10,18)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save('normalization.png')
    img = Image.open('normalization.png')
    # img_below = Image.new("1",size,"white")#单色模式
    # w,h=img.size
    # box=[0,5,w,h-2]
    # im_crop = img.crop(box)
    # w,h=im_crop.size
    # img_below.paste(im_crop, (0,0,w,h))
    return img
def img_chars_normalization(img_chars):
    img_list=[]
    for img in img_chars:
        img_list.append(normalization(img))
    return img_list

#创建26个英文字母文件夹
def folder_ctreate(file_path):
    d=dict.fromkeys(string.ascii_uppercase,0)
    a=[i for i in d.keys()]
    a.sort()
    for char in a:
        path=r"%s/%s"%(file_path,char)
        isExists=os.path.exists(path)  
        # 判断结果  
        if not isExists:  
            print(path)
            # 如果不存在则创建目录  
            # 创建目录操作函数  
            os.makedirs(path)  

def chars_put_correspond_folder(img_list,image_path):
    try:
        img_name=os.path.basename(image_path).split('.')[0][:4]
        chars=[]
        for char in img_name:
            chars.append(char.upper())
        for i in range(4):
            print('*'*33+'chars_put_correspond_folder'+'*'*33)
            path='/'.join(image_path.split(r"/")[0:2])+'/'+chars[i].upper()
            t = time.time()
            time_stamp=int(round(t * 1000))
            char_file_name='/'+str(time_stamp)+str(i)
            print('字符图片路径是: '+path+char_file_name)
            img_list[i].save(path+char_file_name+'.png')
    except Exception:
        pass
    

#验证码处理顺序
#灰度图->二值图->去噪->切割->归一化->训练->识别->验证
def captcha_pretreatment(image_path):
    print('正在处理:%s'%image_path)
    image = Image.open(image_path)
    #二值化开始
    #二值化与灰度图一般是一起处理的
    #先变成灰度图,再进行二值化
    # print('二值化')
    image_binary_result = image_binary(image)
    # image_show_two(image,image_binary_result)
    #二值化结束

    # print('去噪')
    #去噪开始
    image_denoise_result=image_denoise(image_binary_result)
    # image_show_two(image_binary_result,image_denoise_result)
    #去噪结束

    # print('切掉边缘')
    #裁剪图片无用的边缘部分
    #裁切图片开始
    img_cut_result = image_cut_useless_part(image_denoise_result)
    # image_show_two(image_denoise_result,img_cut_result)
    #裁切图片结束

    print('连通域切割字体')
    #切割字符
    #使用cfs连通域方法切割图片
    img_char_4=image_cut_cfs(cfs(img_cut_result))
    image_show_4(img_char_4)

    print('归一化')
    #归一化
    # 将字符图像归一化为 10×18 像素的二值图像是现实中是比较理想的，达到了识别速度快和识别准确率高的较好的平衡点。
    img_chars_normalization_result=img_chars_normalization(img_char_4)
    # image_show_4(img_chars_normalization_result)

    #切割好的字符放入对应文件夹
    chars_put_correspond_folder(img_chars_normalization_result,image_path)
    
def captcha_all_pretreatment(path):
    img_file=path+'/original'
    files=os.listdir(img_file)
    for file in files:
        captcha_pretreatment(img_file+'/'+file)


path=r"D:/captcha"
#创建文件夹,放素材,一共创造26个英文字母
folder_ctreate(path)
#生成验证码,每次默认100个
captcha_create_to_folder.captcha_create(0)
#将代码生成的验证码预处理
#分割为单个字符,放入对应的文件夹
# yxwp19340  图片名字格式
captcha_all_pretreatment(path)














