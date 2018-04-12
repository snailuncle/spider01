# -*- coding:utf-8 -*-
from PIL import Image
img1 = Image.open("test.png")
img1.show()

# getbands() - 显示该图像的所有通道，返回一个tuple
bands = img1.getbands()
print bands

# getbbox() - 返回一个像素坐标，4个元素的tuple
bboxs = img1.getbbox()
print bboxs

# getcolors() - 返回像素信息，是一个含有元素的列表[(该种像素的数量，(该种像素)),(...),...]
colors = img1.getcolors()
print colors

# getdata() - 返回图片所有的像素值，要使用list()才能显示出具体数值
#data = list(img1.getdata())
#print data

# getextrema() - 获取图像中每个通道的像素最小和最大值,是一个tuple类型
extremas = img1.getextrema()
print extremas

# getpixel() - 获取该坐标
pixels = img1.getpixel((87,180))
print pixels

# histogram() - 返回图片的像素直方图
print(img1.histogram())
