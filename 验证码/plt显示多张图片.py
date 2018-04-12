import matplotlib.pyplot as plt
img1=r"D:\captcha\original\ajum38555.jpg"
img2=r"D:\captcha\original\qkax96216.jpg"
from PIL import Image
import numpy as np


img1 = Image.open(img1)

img2 = Image.open(img2)


#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei'] 
#实例化一个fig
#也就是一个画板
fig=plt.figure("去噪前后对比")
#给画板设置一个标题
fig.suptitle("去噪前后对比", fontsize=20)
#subplot(123)
#1代表行  2代表列  3代表行列分割后的区域序号
#这个是2行1列
# 第一个区域
ax = plt.subplot(211)
#子区域的标题
ax.set_title("去噪前")
#子区域显示的内容
plt.imshow(img1)


ax=plt.subplot(212)
ax.set_title("去噪后")
plt.imshow(img2)

plt.show()



