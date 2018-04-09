import cv2  
img=r"D:\captcha\original\ajum38555.jpg"
print(img)
image = cv2.imread(img) 
# cv2.namedWindow('showimage')  
cv2.imshow("Image",image)  
cv2.waitKey(0)  
cv2.destroyAllWindows()


#彩色图像转为灰度图像
img2 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) 
#灰度图像转为彩色图像
img3 = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
# cv2.COLOR_X2Y，其中X,Y = RGB, BGR, GRAY, HSV, YCrCb, XYZ, Lab, Luv, HLS
