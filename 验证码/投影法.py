def vertical(img):
    """传入二值化后的图片进行垂直投影"""
    pixdata = img.load()
    w,h = img.size
    ver_list = []
    # 开始投影
    for x in range(w):
        black = 0
        for y in range(h):
            if pixdata[x,y] == 0:
                black += 1
        ver_list.append(black)
    # 判断边界
    l,r = 0,0
    flag = False
    cuts = []
    for i,count in enumerate(ver_list):
        # 阈值这里为0
        #第一个有黑点的位置是起点,待切割字符的左边.
        #flag表示是否确定了起点
        #先确定起点,在确定终点
        if flag is False and count > 0:
            l = i
            flag = True
        if flag and count == 0:
            r = i-1
            flag = False
            cuts.append((l,r))
    return cuts

p = Image.open('1.png')
b_img = binarizing(p,200)
v = vertical(b_img)
