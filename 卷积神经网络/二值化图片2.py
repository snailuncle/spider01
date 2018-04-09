import cv2,os

# 自适应阀值二值化
# 两个参数  图片目录  图片名字
def _get_dynamic_binary_image(filedir, img_name):
    # filename =   './out_img/' + img_name.split('.')[0] + '-binary.jpg'
    filename = filedir + '_binary/' + img_name.split('.')[0] + '_binary.jpg'
    img_name = filedir + '/' + img_name
    print('.....' + img_name)
    im = cv2.imread(img_name)
    im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #灰值化
    # 二值化  适应门槛
    th1 = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
    cv2.imwrite(filename,th1)
    return th1
filedir=r'D:/captcha/original'
files=os.listdir(filedir)  
for img_name in files:  
    print(img_name) 
    _get_dynamic_binary_image(filedir, img_name)
