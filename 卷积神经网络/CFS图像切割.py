import cv2,sys
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image,ImageEnhance,ImageFilter #enhance增强因子
from cv2 import ImgTools
from numpy import array




def cut_img(img, threshold, cut_width, cut_height, width_min, width_max, height_min):
    charters_imgs = []
    width, height = img.size
    charters_pixels = []
    visited_pixels = []
    pixel_arr = ImgTools.get_pixel_arr(img)
    for i in range(width):
        for j in range(height):
            pixel = img.getpixel((i, j))
            if pixel == 0 and [i, j] not in visited_pixels:
                charter_pixels = Node(i, j, pixel_arr, []).traversal()
                visited_pixels.extend(charter_pixels)
                if len(charter_pixels) > threshold:
                    charters_pixels.append(charter_pixels)
    for i in range(len(charters_pixels)):
        x_min = 0
        y_min = 0
        x_max = 0
        y_max = 0
        # 这里是为了处理没有粘连但是垂直方向有重合的字符
        width, height = img.size
        tmp_img = Image.new('1', (width * 2, height * 2), 255)
        for j in range(len(charters_pixels[i])):
            x, y = charters_pixels[i][j]
            tmp_img.putpixel((x, y), 0)
            if x > x_max:
                x_max = x
            else:
                if x < x_min or x_min == 0:
                    x_min = x
            if y > y_max:
                y_max = y
            else:
                if y < y_min or y_min == 0:
                    y_min = y
        if width_min < x_max - x_min < width_max and y_max - y_min > height_min:
            # charters_imgs.append(tmp_img.crop((x_min, y_min, x_max, y_max)))
            # 这里是为了将所有的图片切成一样大，便于后期的特征提取
            charters_imgs.append(tmp_img.crop((x_min, y_min, x_min + cut_width, y_min + cut_height)))
    return charters_imgs


class Node:
    x = 0
    y = 0
    graph_arr = [] # graph图表
    visited_neighbors = [] #neighbors邻居

    def __init__(self, x, y, graph_arr, visited_neighbors):
        self.x = x
        self.y = y
        self.graph_arr = graph_arr
        self.visited_neighbors = visited_neighbors

    def traversal(self): # traversal遍历
        #做一个九宫格
        for i in range(-1, 2):
            for j in range(-1, 2):
                p = self.x + i
                q = self.y + j
                #在graph_arr范围内,大概是指图片大小范围
                if (0 <= p < len(self.graph_arr)) and (0 <= q < len(self.graph_arr[0])):
                    #九宫格有黑色就做记录
                    if array(self.graph_arr)[p, q] == 0 and [p, q] not in self.visited_neighbors:
                        self.visited_neighbors.append([p, q])
                        next_node = Node(p, q, self.graph_arr, self.visited_neighbors)
                        next_node.traversal()#traversal横越,往返移动
        return self.visited_neighbors    


img_name=r"D:\captcha\clear_border\ajum38555.jpg"
