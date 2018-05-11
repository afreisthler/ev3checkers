#!/usr/bin/env python3

import ev3dev.ev3 as ev3
import time

button = ev3.Button()
while True:
    if button.up:
        ev3.Sound.speak('Hello Turtle Robotics!').wait()
        time.sleep(2)
