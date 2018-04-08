from PIL import Image,ImageDraw, ImageFont, ImageFilter
import random

class VerifyCode():

    def __init__(self):
        self._letter_cases = 'abcdefghjkmnpqrstuvwxy'
        self._upper_cases = self._letter_cases.upper()
        self._numbers = ''.join(map(str, range(3, 10)))
        pass

    def createCodeImage(self,size=(120,30),img_type='jpg',
                        mode='RGB',bg_color=(255,255,255),fg_color=(0,0,255),
                            font_size=18,font_type='arial.ttf',
                            length=4,draw_lines=True,n_line=(1,2),
                            draw_points=True,point_chance=2):
        width,height = size
        img = Image.new(mode, size, bg_color)
        draw = ImageDraw.Draw(img)

        def get_chars():
            return random.sample(self._letter_cases,length)

        def creat_line():
            line_num = random.randint(*n_line)#sign that the param is a list

            for i in range(line_num):
                begin = (random.randint(0, size[0]), random.randint(0, size[1]))
                end = (random.randint(0, size[0]), random.randint(0, size[1]))
                draw.line([begin, end], fill=(0, 0, 0))

        def create_points():
            chance = min(100, max(0, int(point_chance)))
            for w in range(width):
                for h in range(height):
                    tmp = random.randint(0, 100)
                    if tmp > 100 - chance:
                        draw.point((w, h), fill=(0, 0, 0))



        def create_strs():
            c_chars = get_chars()
            strs = ' %s ' % ' '.join(c_chars)
            font = ImageFont.truetype(font_type, font_size)
            font_width, font_height = font.getsize(strs)
            draw.text(((width - font_width) / 3, (height - font_height) / 3),
                        strs, font=font, fill=fg_color)
            return ''.join(c_chars)



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

if __name__ == '__main__':
    # code_img,capacha_code= creat_validata_code()
    code_img,capacha_code= VerifyCode().createCodeImage()
    print(capacha_code)
    code_img.save('xx.jpg','JPEG')
