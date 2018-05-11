#!/usr/bin/env python3

import ev3dev.ev3 as ev3
import time

button = ev3.Button()
while True:
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
    if button.up:
        ev3.Sound.speak('Hello World!').wait()
        time.sleep(2)
