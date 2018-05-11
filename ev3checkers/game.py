#!/usr/bin/env python3

import logging
import ev3dev.ev3 as ev3
from ev3checkers.components.board import Board


class Game(object):

    def __init__(self):
        self.screen = ev3.Screen()
        self.board = Board(screen=self.screen)

    def draw(self):
        self.screen.clear()
        self.board.draw()
        self.screen.update()

# This is the entry point for a call from skynet, launched through scheduler and func
if __name__ == "__main__":
    try:
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
        game = Game()
        game.draw()
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
    except:
        while True:
            pass

    while True:
        pass