from ev3dev.ev3 import *
from PIL import Image, ImageDraw, ImageFont

lcd = Screen()

f = ImageFont.truetype('/usr/share/fonts/truetype/msttcorefonts/Arial.ttf', 75)
lcd.draw.text((3,0), 'Hello', font=f)
lcd.draw.text((2,55), 'world', font=f)
lcd.update()