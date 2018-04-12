from PIL import Image,ImageDraw, ImageFont, ImageFilter
import random
import matplotlib.pyplot as plt

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

img_path=r"D:\captcha\create_captcha\acxh50391.jpg"
image = Image.open(img_path)
imgry = image.convert('L')  # 转化为灰度图
# plt.figure("灰度图")
# plt.imshow(imgry)
imgry.show()


table = get_bin_table()
out = imgry.point(table, '1')
print(image)
print(out)
# plt.figure("二值图")
# plt.imshow(out)
# plt.show()


# from PIL import Image
# import matplotlib.pyplot as plt
# img_path=r"D:\captcha\original\ajum38555.jpg"

# img=Image.open(img_path)
# img = img.convert('L')
# plt.figure("captcha")
# plt.imshow(img)
# plt.show()
