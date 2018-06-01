#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *
from time import sleep

m1 = LargeMotor('outA')
m2 = LargeMotor('outB')

for i in range(7):
    m1.run_to_rel_pos(position_sp=-110, speed_sp=150, stop_action="hold")
    m2.run_to_rel_pos(position_sp=-110, speed_sp=150, stop_action="hold")
    sleep(1)

for i in range(7):
    m1.run_to_rel_pos(position_sp=110, speed_sp=150, stop_action="hold")
    m2.run_to_rel_pos(position_sp=110, speed_sp=150, stop_action="hold")
    sleep(1)   


