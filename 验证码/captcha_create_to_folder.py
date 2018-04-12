from PIL import Image,ImageDraw, ImageFont, ImageFilter
import random
import os

class VerifyCode():

    def __init__(self):
        #验证码包含的字符
        self._letter_cases = 'abcdefghjkmnpqrstuvwxy'
        #大写方法
        self._upper_cases = self._letter_cases.upper()
        
        self._numbers = ''.join(map(str, range(3, 10)))
        pass
    # 宽度120 高度30  长方形
    # 背景=白色     前景色=蓝色

    def createCodeImage(self,size=(120,30),img_type='jpg',
                        mode='RGB',bg_color=(255,255,255),fg_color=(0,0,255),
                            font_size=18,font_type='arial.ttf',
                            length=4,draw_lines=True,n_line=(1,2),
                            draw_points=True,point_chance=2):
        width,height = size#(元组)
        img = Image.new(mode, size, bg_color)
        draw = ImageDraw.Draw(img)
        #生成长度为length的字符串
        def get_chars():
            return random.sample(self._letter_cases,length)
        #生成干扰线
        def creat_line():
            line_num = random.randint(*n_line)#sign that the param is a list
            #两点一直线
            for _ in range(line_num):
                begin = (random.randint(0, size[0]), random.randint(0, size[1]))
                end = (random.randint(0, size[0]), random.randint(0, size[1]))
                draw.line([begin, end], fill=(0, 0, 0))
        #生成干扰点
        def create_points():
            chance = min(100, max(0, int(point_chance)))
            for w in range(width):
                for h in range(height):
                    tmp = random.randint(0, 100)
                    if tmp > 100 - chance:
                        draw.point((w, h), fill=(0, 0, 0))


        #生成某个字体的字符串
        def create_strs():
            c_chars = get_chars()
            strs = ' %s ' % ' '.join(c_chars)
            font = ImageFont.truetype(font_type, font_size)
            font_width, font_height = font.getsize(strs)
            draw.text(((width - font_width) / 3, (height - font_height) / 3),
                        strs, font=font, fill=fg_color)
            return ''.join(c_chars)


        # draw = ImageDraw.Draw(img)
        #干扰线,干扰点,和字符串,  都与draw绑定
        if draw_lines:
            creat_line()
        if draw_points:
            create_points()
        strs = create_strs()

        params = [1 - float(random.randint(1, 2)) / 100,
                  0,
                  0,
                  0,
                  1 - float(random.randint(1, 10)) / 100,
                  float(random.randint(1, 2)) / 500,
                  0.001,
                  float(random.randint(1, 2)) / 500
                  ]
        img = img.transform(size, Image.PERSPECTIVE, params)
        img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        return img, strs

def folder_create():
    path=r"D:/captcha/original"
    isExists=os.path.exists(path)  
    # 判断结果  
    if not isExists:  
        # 如果不存在则创建目录  
        # 创建目录操作函数  
        os.makedirs(path)  

def captcha_create(num=100):
    folder_create()
    for i in range(num):
        #加个随机数,防止文件名重复
        #文件名就是验证码中的字符串
        rnd_int=random.randint(10000,99999)
        rnd_int_str=str(rnd_int)
        #返回验证码图片,和验证码字符串
        code_img,captcha_code= VerifyCode().createCodeImage()
        print(captcha_code)
        code_img.save(r'D:/captcha/original/%s%s.jpg'%(captcha_code,rnd_int_str),'JPEG')

if __name__ == '__main__':
    captcha_create()
    
