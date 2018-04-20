
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


# 使用一组全部标记为8的21张图片来进行模型测试
# 测试图片生成带标记的特征文件名称为 last_test_pix_xy_new.txt
def svm_model_test():
    """
    使用测试集测试模型
    :return:
    """

    # 训练命令：model = svmtrain(train_label, train_data,  ['libsvm_options']);
    #                           精确度
    # 测试命令：[predict_label, accuracy, dec_values] = svmpredict(test_label, test_data, model);

    test_svm_file=r"D:\captcha\svm_feature\char_feature.txt"
    yt, xt = svm_read_problem(test_svm_file)
    model_path=r"D:\captcha_first\svm_feature\save_svm_model.txt"
    model = svm_load_model(model_path)
    # 单个样本预测的类别，就是上述测试命令中的返回值predict_label，它是一个列向量，第i个元素代表第i个测试样本的预测类别。
    # predict_label
    p_label, p_acc, p_val = svm_predict(yt, xt, model)#p_label即为识别的结果

    for item in p_label:
        print('%d' % item, end=',')

svm_model_test()
