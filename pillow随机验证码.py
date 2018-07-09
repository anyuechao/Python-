#!/usr/bin/env python
#coding=utf-8

from PIL import Image

# print(dir(pillow))

# #打开一个 jpg 图像文件，注意当前路径
# im = Image.open('cc.png')
# #获得图像尺寸
# w,h = im.size
# print('Original image size: %sx%s' % (w, h))
# #缩放50%
# im.thumbnail((w//2,h//2))
# print('Resize image to: %sx%s' % (w//2, h//2))
# # 把缩放后的图像用jpeg格式保存:
# im.save('aa.png', 'png')



'''
# 比如，模糊效果也只需几行代码：
滤镜
'''
# from PIL import Image,ImageFilter

# # 打开一个 JPG 图像文件，注意是当前路径
# im = Image.open('cc.png')
# # 应用模糊滤镜
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.png','png')

# from PIL import Image,ImageDraw,ImageFont,ImageFilter
# import random

'''# # 随机字母'''

# def rndChar():
# 	return chr(random.randint(65,90))

# # 随机颜色
# def rndColor():
# 	return(random.randint(64,255),random.randint(64,255),random.randint(64,255))

# # 随机颜色2
# def rndColor2():
# 	return(random.randint(32,127),random.randint(32,127),random.randint(32,127))

# # 240*60
# width = 60 * 4
# height = 60
# image = Image.new('RGB',(width,height),(255,255,255))
# # 创建 font 对象
# font = ImageFont.truetype('Arial.ttf',36) 
# # 创建 Draw 对象
# draw = ImageDraw.Draw(image)
# # 创建每个像素
# for x in range(width):
# 	for y in range(height):
# 		draw.point((x,y),fill = rndColor())
# # 输出文字
# for t in range(4):
# 	draw.text((60 * t + 10,10),rndChar(),font=font,fill=rndColor2())

# # 模糊
# image = image.filter(ImageFilter.BLUR)
# image.save('code.jpg','jpeg')

















