# -*- coding:utf-8 -*-
# 图像处理

from PIL import Image, ImageFilter

img = Image.open('test.jpg')
w, h = img.size
print('Original image size： %s %s ' % (w, h))
# 缩放图片
img.thumbnail((w/2, h/2))
print('Resize image to: %s %s' % (w/2, h/2))
# 把缩放后的图片以jpg的格式保存
img.save('thumbnail.jpg', 'jpeg')
# 模糊效果只需要几行代码就可以了
imgBlur = Image.open('test.jpg')
imgBLurProcessed=imgBlur.filter(ImageFilter.BLUR)
imgBLurProcessed.save('imgblur.jpg', 'jpeg')

