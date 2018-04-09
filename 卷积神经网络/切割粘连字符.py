def cutting_img(im,im_position,img,xoffset = 1,yoffset = 1):
  filename =  './out_img/' + img.split('.')[0]
  # 识别出的字符个数
  im_number = len(im_position[1])
  # 切割字符
  for i in range(im_number):
    im_start_X = im_position[1][i][0] - xoffset
    im_end_X = im_position[1][i][1] + xoffset
    im_start_Y = im_position[2][i][0] - yoffset
    im_end_Y = im_position[2][i][1] + yoffset
    cropped = im[im_start_Y:im_end_Y, im_start_X:im_end_X]
    cv2.imwrite(filename + '-cutting-' + str(i) + '.jpg',cropped)
