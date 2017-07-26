"""
@description: build the verification code image
@author: merle
@contact: merle.liukun@gmail.com
@date: 17-7-20
"""
import random

from PIL import Image, ImageDraw, ImageFont, ImageFilter


# random char
def rand_char():
    return chr(random.randint(64, 90))


# random color one
def rand_color_first():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


# random color second
def rand_color_second():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


# image
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

font = ImageFont.truetype('/usr/share/fonts/TTF/AkaashNormal.ttf', 36)

draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rand_color_first())

for t in range(4):
    draw.text((60 * t + 10, 10), rand_char(), font=font, fill=rand_color_second())

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
