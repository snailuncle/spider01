# 10×18
# def normalization(img):
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from numpy import array
from skimage import io
import matplotlib.pyplot as plt
from skimage import morphology

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
    left=27
    right=33
    upper=int(3)
    lower=int(h-3)
    region = (left, upper, right, lower)
    crop_img = img.crop(region)
    return crop_img

def x(img):
    size=(10,18)
    img_below = Image.new("1",size,"white")#单色模式
    w,h=img.size
    box=[0,5,w,h-2]
    im_crop = img.crop(box)
    w,h=im_crop.size
    img_below.paste(im_crop, (0,0,w,h))
    return img_below

img_path=r"D:\captcha\original\jpeq82584.jpg"
img_o=io.imread(img_path)

# img_o=Image.open(img_path)
img=image_binary(img_o)
# img_above=image_cut_useless_part(img)
# 3、删除小块区域pip

# img=io.imread(img_path)
img=morphology.remove_small_objects(img,min_size=300,connectivity=1)
io.imshow(img)
plt.show()

# 有些时候，我们只需要一些大块区域，那些零散的、小块的区域，我们就需要删除掉，则可以使用morphology子模块的remove_small_objects（)函数。
fig = plt.figure("图片处理前后对比")
plt.subplot(211)
plt.imshow(img_o)

img_below=x(img_above)
print(img.format,img.size,img.mode)
plt.subplot(212)
plt.imshow(img_below)
plt.show()










