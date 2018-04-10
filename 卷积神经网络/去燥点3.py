#coding=utf-8
"""
creat time:2015.09.14
"""
import cv2,sys
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image,ImageEnhance,ImageFilter #enhance增强因子
img_name=r"D:\captcha\original\ajum38555.jpg"
# img_name = '2+.png'
#去除干扰线
im = Image.open(img_name)
#图像二值化
# enhancer = ImageEnhance.Contrast(im)#contrast对比
# plt.figure("contrast对比")
# plt.imshow(im)
# im = enhancer.enhance(2)
# plt.figure("enhancer.enhance(2)")
# plt.imshow(im)
im = im.convert('1')#convert转换
# plt.figure("convert1")
# plt.imshow(im)
data = im.getdata()
# for i in data:
#     print(i)
# print(list(data))
data=list(data)
w,h = im.size
data_all=''
i=0
for y in range(h):
    for x in range(w):
        if data[i]==255:
            data[i]=1
        data_all=data_all+(str(data[i]))
        i+=1
    data_all=data_all+'\n'
print(data_all)
sys.exit()
# with open(r'D:\spider01\卷积神经网络\二值化打印.txt','w') as f:
#     f.write(data_all)
plt.figure("去噪前")
plt.imshow(im)

# print(w,h)
#im.show()
w,h = im.size
# 
black_point = 0
for x in range(1,w-1):
    for y in range(1,h-1):#列循环在内,从左往右纵向扫描
        mid_pixel = data[w*y+x] #中央像素点像素值
        if mid_pixel == 0: #找出上下左右四个方向像素点像素值
            top_pixel = data[w*(y-1)+x]
            left_pixel = data[w*y+(x-1)]
            down_pixel = data[w*(y+1)+x]
            right_pixel = data[w*y+(x+1)]

            #判断上下左右的黑色像素点总个数
            if top_pixel == 0:
                black_point += 1
            if left_pixel == 0:
                black_point += 1
            if down_pixel == 0:
                black_point += 1
            if right_pixel == 0:
                black_point += 1
            if black_point >= 3:
                im.putpixel((x,y),0)
            elif black_point <2:
                im.putpixel((x,y),255)
                
            #print black_point
            black_point = 0
plt.figure("去噪后")
plt.imshow(im)
plt.show()
