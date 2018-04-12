from PIL import Image,ImageDraw, ImageFont, ImageFilter
import random
import matplotlib.pyplot as plt
import os
import cv2
import numpy as np

img_path=r"D:\captcha\create_captcha\erjs48626.jpg"
image = Image.open(img_path)
info=list(image.getdata()  )
print(info)

