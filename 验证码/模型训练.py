
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
svm_model_path=r"D:/libsvm-3.22/python"
sys.path.append(svm_model_path)
import svmutil
dir(svmutil)
from svmutil import svm_read_problem,svm_train,svm_load_model,svm_predict,svm_save_model



def train_svm_model(save_svm_model_path,char_svm_feature_path):
    """
    训练并生成model文件
    :return:
    """
    y, x = svm_read_problem(char_svm_feature_path)
    model = svm_train(y, x)
    svm_save_model(save_svm_model_path, model)
    # y, x = svm_read_problem(svm_root + '/train_pix_feature_xy.txt')
    # model = svm_train(y, x)
    # svm_save_model(model_path, model)
     
        


if __name__=='__main__':

    svm_model_path=r"D:\captcha\svm_feature\save_svm_model.txt"
    base_folder=r"D:/captcha/svm_feature"
    char_svm_feature_path=base_folder+'/'+'char_feature.txt'
    
    train_svm_model(svm_model_path,char_svm_feature_path)
