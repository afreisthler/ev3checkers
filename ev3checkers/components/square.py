import ev3dev.ev3 as ev3

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
        self.screen.draw.rectangle((0, 0, DRAW_WIDTH, DRAW_HEIGHT), fill='black')
