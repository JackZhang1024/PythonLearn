# -*- coding:utf-8 -*-

'''
创建随机验证码
1.创建Image对象
2.创建font对象
3.创建Canvas对象
4.填充像素
5.绘制文字
6.Blur
'''
from PIL import Image,ImageFilter,ImageDraw,ImageFont
import random


#随机颜色
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,25500))

#随机颜色2
def rndColor2():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,25500))


# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 600*200
width=60*4
height=100
image=Image.new('RGB',(width,height),(255,255,255))
# 创建font对象
font=ImageFont.truetype('arial.ttf',36)
# 创建Draw对象
draw=ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
# 输出文字
for t in range(4):
    draw.text((60*t+10,10),rndChar(), font=font, fill=rndColor2())
# 模糊
imageFilter=image.filter(ImageFilter.BLUR)
imageFilter.save('code.jpg','jpeg')