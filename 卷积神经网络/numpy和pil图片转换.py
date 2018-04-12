# 10×18
# def normalization(img):
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from numpy import array

#图片二值化
def image_binary(img):
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
    # 转化为灰度图
    imgry = img.convert('L')  
    table = get_bin_table()
    img_binary_result = imgry.point(table, '1')
    return img_binary_result

#裁剪图片无用的边缘部分
def image_cut_useless_part(img):
    w,h = img.size   
    #左右各裁剪1/6
    #上下各裁剪3个像素
    left=53
    right=63
    upper=int(3)
    lower=int(h-3)
    region = (left, upper, right, lower)
    crop_img = img.crop(region)
    return crop_img



img_path=r"D:\captcha\original\ajum38555.jpg"
img=Image.open(img_path)
img=image_binary(img)
img=image_cut_useless_part(img)
arr = array(img)
img = Image.fromarray(arr)
print(arr)
plt.figure("captcha")
plt.imshow(img)
plt.show()




import sys
import numpy
from PIL import Image

img = Image.open(sys.argv[1]).convert('L')

im = numpy.array(img)
fft_mag = numpy.abs(numpy.fft.fftshift(numpy.fft.fft2(im)))

visual = numpy.log(fft_mag)
visual = (visual - visual.min()) / (visual.max() - visual.min())

result = Image.fromarray((visual * 255).astype(numpy.uint8))
result.save('out.bmp')





