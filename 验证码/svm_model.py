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



def get_feature(img_path):
    """
    获取指定图片的特征值,
    1. 按照每排的像素点,高度为10,则有10个维度,然后为6列,总共16个维度
    :param img_path:
    :return:一个维度为10（高度）的列表
    """
    # img_path=r"D:\captcha\0\15242041174093.png"
    img = Image.open(img_path)
    width, height = img.size
    # print(img.size)

    pixel_cnt_list = []
    # height = 10
    for y in range(height):
        pix_cnt_x = 0
        for x in range(width):
            if img.getpixel((x, y)) == 0:  # 黑色点
                pix_cnt_x += 1

        pixel_cnt_list.append(pix_cnt_x)

    for x in range(width):
        pix_cnt_y = 0
        for y in range(height):
            if img.getpixel((x, y)) == 0:  # 黑色点
                pix_cnt_y += 1

        pixel_cnt_list.append(pix_cnt_y)

    result=' '.join(['{}:{}'.format(i,v) for i,v in enumerate(pixel_cnt_list,1)])
    pattern=r'([^\\/])[\\/][a-zA-Z0-9]+\.'
    num_char=re.search(pattern, img_path).group(1)
    result=' '.join((num_char,result))+'\n'
    svm_path="D:/captcha/svm_feature"
    svm_feature_path=svm_path+'/'+'char_feature.txt'
    with open(svm_feature_path,'a+') as f:
        f.write(result)

    # return result


def svm_folder_ctreate():
    path="D:/captcha/svm_feature"
    isExists=os.path.exists(path)  
    # 判断结果  
    if not isExists:  
        # 如果不存在则创建目录  
        # 创建目录操作函数  
        os.makedirs(path)  


if __name__=='__main__':
    svm_folder_ctreate()
    base_folder=r"D:/captcha"
    for i in range(0,10):
        char_img_folder=base_folder+'/'+str(i)
        img_file_list=os.listdir(char_img_folder)
        for img_path in img_file_list:
            img_path=char_img_folder+'/'+img_path
            get_feature(img_path)










































