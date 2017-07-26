"""
@description: make the image to small
@author: merle
@contact: merle.liukun@gmail.com
@date: 17-7-20
"""

from PIL import Image


im = Image.open('code.jpg')

w, h = im.size
print('The size is: width:{}, height:{}'.format(w, h))

im.thumbnail((w//2, h//2))

print('Resize image to: width:{}, height:{}'.format(w//2, h//2))

im.save('thumbnail.jpg', 'jpeg')
