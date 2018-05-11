
import time
import ev3dev.ev3 as ev3
from ev3checkers.components.square import Square

WIDTH = 8
HEIGHT = 8
COLORS = ['white', 'lightgray']

class Board(object):


    def __init__(self, screen):

        self.screen = screen
        self.current_color = COLORS[0]

        # Initialize Board
        self.squares = []
        for w in range(WIDTH):
            self.squares.append([])

        for w in range(WIDTH):
            for h in range(HEIGHT):
                self.squares[w].append(Square(self.screen, self.current_color, w, h))
                self._switch_color()
            self._switch_color()

    def draw(self):
        for w in range(WIDTH):
            for h in range(HEIGHT):
                self.squares[w][h].draw()


    def _switch_color(self):
        if self.current_color == COLORS[0]:
            self.current_color = COLORS[1]
        else:
            self.current_color = COLORS[0]


    def __str__(self):
        display = ''
        for w in range(WIDTH):
            for h in range(HEIGHT):
                display += ' ' + self.squares[w][h].color
            display += '\n'
        return display


