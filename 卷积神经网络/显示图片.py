from PIL import Image
import matplotlib.pyplot as plt
img_path=r"D:\captcha\original\ajum38555.jpg"

img=Image.open(img_path)
img = img.convert('L')
plt.figure("captcha")
plt.imshow(img)
plt.show()


# figure默认是带axis的，如果没有需要，我们可以关掉

# plt.axis('off')
# 打开图片后，可以使用一些属性来查看图片信息，如

# print img.size  #图片的尺寸
# print img.mode  #图片的模式
# print img.format  #图片的格式
# 显示结果为：

# (558, 450)
# RGBA
# PNG
# 二、图片的保存

# img.save('d:/dog.jpg')
# 就一行代码，非常简单。这行代码不仅能保存图片，还是转换格式，如本例中，就由原来的png图片保存为了jpg图片。

 