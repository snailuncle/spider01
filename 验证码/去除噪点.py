from PIL import Image,ImageDraw, ImageFont, ImageFilter
import random
import matplotlib.pyplot as plt
import os
import cv2
import numpy as np

# 8.1   二值化图片
# 主要步骤如下：

# 将RGB彩图转为灰度图
# 将灰度图按照设定阈值转化为二值图

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
s=get_bin_table()

img_path=r"D:\captcha\create_captcha\erjs48626.jpg"
image = Image.open(img_path)
imgry = image.convert('L')  # 转化为灰度图
# plt.figure("灰度图")
# plt.imshow(imgry)
# imgry.show()


table = get_bin_table()
out = imgry.point(table, '1')
# plt.figure("二值图")
# plt.imshow(out)
# plt.show()


# from PIL import Image
# import matplotlib.pyplot as plt
# img_path=r"D:\captcha\original\ajum38555.jpg"

# img=Image.open(img_path)
# img = img.convert('L')
plt.figure("去噪前")
plt.imshow(out)
# plt.show()

# 对某个 黑点 周边的九宫格里面的黑色点计数
# 如果黑色点少于2个则证明此点为孤立点，然后得到所有的孤立点
# 对所有孤立点一次批量移除。
def sum_9_region(img, x, y):
    """
    9邻域框,以当前点为中心的田字框,黑点个数
    :param x:
    :param y:
    :return:
    """
    # todo 判断图片的长宽度下限
    cur_pixel = img.getpixel((x, y))  # 当前像素点的值
    width = img.width
    height = img.height

    if cur_pixel == 1:  # 如果当前点为白色区域,则不统计邻域值
        return 0

    if y == 0:  # 第一行
        if x == 0:  # 左上顶点,4邻域
            # 中心点旁边3个点
            sum = cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))
            return 4 - sum
        elif x == width - 1:  # 右上顶点
            sum = cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1))

            return 4 - sum
        else:  # 最上非顶点,6邻域
            sum = img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))
            return 6 - sum
    elif y == height - 1:  # 最下面一行
        if x == 0:  # 左下顶点
            # 中心点旁边3个点
            sum = cur_pixel \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y - 1)) \
                  + img.getpixel((x, y - 1))
            return 4 - sum
        elif x == width - 1:  # 右下顶点
            sum = cur_pixel \
                  + img.getpixel((x, y - 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y - 1))

            return 4 - sum
        else:  # 最下非顶点,6邻域
            sum = cur_pixel \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x, y - 1)) \
                  + img.getpixel((x - 1, y - 1)) \
                  + img.getpixel((x + 1, y - 1))
            return 6 - sum
    else:  # y不在边界
        if x == 0:  # 左边非顶点
            sum = img.getpixel((x, y - 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y - 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))

            return 6 - sum
        elif x == width - 1:  # 右边非顶点
            # print('%s,%s' % (x, y))
            sum = img.getpixel((x, y - 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x - 1, y - 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1))

            return 6 - sum
        else:  # 具备9领域条件的
            sum = img.getpixel((x - 1, y - 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1)) \
                  + img.getpixel((x, y - 1)) \
                  + cur_pixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y - 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))
            return 9 - sum

# sum_9_region(img,x,y)


# if black_point >= 3:
#     im.putpixel((x,y),0)
# elif black_point <2:
#     im.putpixel((x,y),255)
n=1
for i in range(n):
    w,h=out.size
    for x in range(w):
        for y in range(h):
            black_point_num=sum_9_region(out, x, y)
            if black_point_num<4:
                #黑点少于两个
                #该点为孤立点
                #将该点设为白色
                out.putpixel((x,y),1)

plt.figure("去噪后")
plt.imshow(out)
plt.show()
out.save('denoise.png')
