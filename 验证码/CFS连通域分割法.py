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
import re
svm_model_path="D:/libsvm-3.22/python"
sys.path.append(svm_model_path)
from svmutil import svm_read_problem,svm_train,svm_load_model,svm_predict,svm_save_model


def cfs(img):
    """传入二值化后的图片进行连通域分割"""
    pixdata = img.load()
    w,h = img.size
    visited = set()
    q = queue.Queue()
    offset = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
    cuts = []
    for x in range(w):
        for y in range(h):
            x_axis = []
            y_axis = []
            if pixdata[x,y] == 0 and (x,y) not in visited:
                q.put((x,y))
                visited.add((x,y))
            while not q.empty():
                x_p,y_p = q.get()
                for x_offset,y_offset in offset:
                    x_c,y_c = x_p+x_offset,y_p+y_offset
                    if (x_c,y_c) in visited:
                        continue
                    visited.add((x_c,y_c))
                    try:
                        if pixdata[x_c,y_c] <30:
                            q.put((x_c,y_c))
                            x_axis.append(x_c)
                            y_axis.append(x_c)
                            #y_axis.append(y_c)
                    except Exception:
                        pass
            if x_axis:
                min_x,max_x = min(x_axis),max(x_axis)
                if max_x - min_x >  6:
                    # 宽度小于3的认为是噪点，根据需要修改
                    cuts.append((min_x,max_x))
            if y_axis:
                min_y,max_y = min(y_axis),max(y_axis)
                if max_y - min_y >  3:
                    # 宽度小于3的认为是噪点，根据需要修改
                    cuts.append((min_y,max_y))
    print(cuts)
    return cuts

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


    plt.imshow(img1)
    plt.show()

image_path=r"C:\Users\Administrator\Desktop\QQ图片20180423185646.jpg"

image = Image.open(image_path)
#二值化开始
#二值化与灰度图一般是一起处理的
#先变成灰度图,再进行二值化
# print('二值化')
# image_binary_result = image_binary(image)

# cfs(image)

# image_show_two(image_binary_result,image_binary_result)
image_show_two(image,image)











