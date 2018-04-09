# 去除边框
import cv2
# 图像的大小可以通过其shape属性来获取，shape返回的是一个tuple元组，第一个元素表示图像的高度，第二个表示图像的宽度，第三个表示像素的通道数。
def clear_border(img,img_name):
    filename = './out_img/' + img_name.split('.')[0] + '-clearBorder.jpg'
    h, w = img.shape[:2]
    for y in range(0, w):#宽
        for x in range(0, h):#高
            #只处理图片边边角角的两个像素
            if y < 2 or y > w - 2:
                img[x, y] = 255
            if x < 2 or x > h -2:
                img[x, y] = 255

    cv2.imwrite(filename,img)
    return img
