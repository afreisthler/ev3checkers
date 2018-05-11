import ev3dev.ev3 as ev3
import time

DRAW_WIDTH = 50
DRAW_HEIGHT = 50

class Square(object):


    def __init__(self, color, x, y):
        self.checker = None
        self.x = x
        self.y = y
        self.color = color
        self.screen = ev3.Screen()

    def draw(self):
        self.screen.clear()
        time.sleep(2)
        self.screen.draw.rectangle((0, 0, DRAW_WIDTH, DRAW_HEIGHT), fill='black')
        self.screen.update()
        time.sleep(2)
