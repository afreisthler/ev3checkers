import ev3dev.ev3 as ev3
import time

DRAW_WIDTH = 15
DRAW_HEIGHT = 15

class Square(object):


    def __init__(self, color, x, y):
        self.checker = None
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen):
        # screen = ev3.Screen()
        x0 = DRAW_WIDTH * self.x
        y0 = DRAW_HEIGHT * self.y
        x1 = x0 + DRAW_WIDTH
        y1 = y0 + DRAW_HEIGHT
        screen.draw.rectangle((x0, y0, x1, y1), fill=self.color)


