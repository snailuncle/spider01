from PIL import Image,ImageDraw, ImageFont, ImageFilter


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


img_path=r"D:\captcha\ajum38555.jpg"
image = Image.open(img_path)
imgry = image.convert('L')  # 转化为灰度图

table = get_bin_table()
out = imgry.point(table, '1')
print(type(out))
print(out.show())
print(out.histogram())
print(out.tobytes())

