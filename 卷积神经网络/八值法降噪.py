


import cv2,sys
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image,ImageEnhance,ImageFilter #enhance增强因子
img_name=r"D:\captcha\original\ajum38555.jpg"
from numpy import array
# 八值法降噪
def clean_img_eight(img, threshold):
    width, height = img.size
    arr = [[0 for col in range(width)] for row in range(height)]
    arr = array(arr)
    print(arr)
    for j in range(height):
        for i in range(width):
            point = img.getpixel((i, j))
            if point == 0:
                sum = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        #外框判断,出界无效
                        if i + x > width - 1 or j + y > height - 1 or \
                                i + x < 0 or j + y < 0:
                            sum += 1
                        #统计九宫格的黑点数量
                        else:
                            sum += img.getpixel((i + x, j + y))
                #更改矩阵值
                #如果九宫格的颜色值加起来超过阈值
                #就都变为白色
                if sum >= threshold:
                    arr[j, i] = 1

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i, j] == 1:
                img.putpixel((j, i), 1)
    return img


img=Image.open(img_name)
img = img.convert('1')
threshold=1500
img_clean=clean_img_eight(img, threshold)
plt.figure("去噪后")
plt.imshow(img_clean)
plt.show()

img_clean.save(r"D:\captcha\clear_border\ajum38555.jpg")
