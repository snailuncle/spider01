# a. 以数组的形式创建图像，PIL.image.fromarray(obj,mode=None)

# obj - 图像的数组，类型可以是numpy.array()

# mode - 如果不给出，会自动判断

# 本人觉得这个功能还是挺实用的，可以将一个数组（具体一点就是像素数组）转换为图像，从图像的本质去处理图像。

# 下面一段程序，就是用fromarray()函数实现图像的灰度化（使用了两种方法）。

# -*- coding:utf-8 -*-
from PIL import Image
import numpy as np
# a = Image.open("fromimg.png")
a = Image.open("captcha.jpg")
a.show()
b = a.resize((28,28))
datab = list(b.getdata())
#print( type(datab))
obj1 = []
obj2 = []
for i in range(len(datab)):
    obj1.append([sum(datab[i])/3])  # 灰度化方法1：RGB三个分量的均值
    obj2.append([0.3*datab[i][0]+0.59*datab[i][1]+0.11*datab[i][2]])
    #灰度化方法2：根据亮度与RGB三个分量的对应关系：Y=0.3*R+0.59*G+0.11*B

obj1 = np.array(obj1).reshape((28,28))
obj2 = np.array(obj2).reshape((28,28))
print( obj1)
print( obj2)

arrayimg1 = Image.fromarray(obj1)
arrayimg2 = Image.fromarray(obj2)
arrayimg1.show()
arrayimg2.show()
