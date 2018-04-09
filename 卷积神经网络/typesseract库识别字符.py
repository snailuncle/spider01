# 识别验证码
      cutting_img_num = 0
      for file in os.listdir('./out_img'):
        str_img = ''
        if fnmatch(file, '%s-cutting-*.jpg' % img_name.split('.')[0]):
          cutting_img_num += 1
      for i in range(cutting_img_num):
        try:
          file = './out_img/%s-cutting-%s.jpg' % (img_name.split('.')[0], i)
          # 识别字符
          str_img = str_img + image_to_string(Image.open(file),lang = 'eng', config='-psm 10') #单个字符是10，一行文本是7
        except Exception as err:
          pass
      print('切图：%s' % cutting_img_num)
      print('识别为：%s' % str_img)
