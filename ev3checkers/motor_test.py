#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *
from time import sleep

m1 = LargeMotor('outA')
m2 = LargeMotor('outB')

m1.run_to_rel_pos(position_sp=180, speed_sp=100, stop_action="hold")
m2.run_to_rel_pos(position_sp=180, speed_sp=100, stop_action="hold")

sleep(5)   # Give the motor time to move