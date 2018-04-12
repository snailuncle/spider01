def binarizing(img,threshold):
    """传入image对象进行灰度、二值处理"""
    img = img.convert("L") # 转灰度
    pixdata = img.load()
    w, h = img.size
    # 遍历所有像素，大于阈值的为黑色
    # 已经转为灰度值,灰度值范围0-255
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img
