from PIL import Image,ImageDraw, ImageFont, ImageFilter
import matplotlib.pyplot as plt

#threshold门槛
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
    print(table)
    return table

img_path=r"D:\captcha\original\ajum38555.jpg"
image = Image.open(img_path)
# print('*'*88)
# print(list(image.getdata()))
# print('*'*88)
#convert 转变
imgry = image.convert('L')  # 转化为灰度图
# print(list(imgry.getdata()))
# print('*'*88)
table = get_bin_table()
out = imgry.point(table, '1')
# print(list(out.getdata()))

# print(out.show())
# print(out.histogram())
# print(out.tobytes())
# plt.imshow(out)
# plt.show()
