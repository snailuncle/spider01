
import cv2,sys
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image,ImageEnhance,ImageFilter #enhance增强因子
img_name=r"D:\captcha\original\ajum38555.jpg"

def clean_img(img, threshold):
    width, height = img.size
    for j in range(height):
        for i in range(width):
            point = img.getpixel((i, j))
            if point == 0:
                for x in range(threshold):
                    if j + x >= height:
                        break
                    else:
                        if point != img.getpixel((i, j + x)):
                            img.putpixel((i, j), 1)
                            break
    return img

img=Image.open(img_name)
print('*'*88)
print(list(img.getdata()))
img = img.convert('1')
print('*'*88)
print(list(img.getdata()))
threshold=2
img_clean=clean_img(img, threshold)
# plt.figure("去噪后")
# plt.imshow(img_clean)
# plt.show()
print(list(img_clean.getdata()))
