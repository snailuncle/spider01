# -*- coding:utf-8 -*-
from PIL import Image
from PIL import ImageFilter

# BLUR - 模糊处理
# CONTOUR - 轮廓处理
# DETAIL - 增强
# EDGE_ENHANCE - 将图像的边缘描绘得更清楚
# EDGE_ENHANCE_NORE - 程度比EDGE_ENHANCE更强
# EMBOSS - 产生浮雕效果
# SMOOTH - 效果与EDGE_ENHANCE相反，将轮廓柔和
# SMOOTH_MORE - 更柔和
# SHARPEN - 效果有点像DETAIL
testimg = Image.open("captcha.jpg")
testimg.show()
# filterimg = testimg.filter(ImageFilter.MedianFilter)
filterimg = testimg.filter(ImageFilter.SMOOTH)
filterimg.show()
