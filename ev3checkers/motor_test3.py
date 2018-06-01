
from ev3dev.ev3 import *
from time import sleep

m3 = MediumMotor('outC')

m1 = LargeMotor('outA')
m2 = LargeMotor('outB')

BLOCK_ROTATIONS = 135
direction = -1

for i in range(7):
    for i in range(7):
        m3.run_to_rel_pos(position_sp=direction * BLOCK_ROTATIONS, speed_sp=150, stop_action="hold")
        sleep(1)
    direction = direction * -1
    m1.run_to_rel_pos(position_sp=-110, speed_sp=150, stop_action="hold")
    m2.run_to_rel_pos(position_sp=-110, speed_sp=150, stop_action="hold")
    sleep(1)

for i in range(7):
    m3.run_to_rel_pos(position_sp=BLOCK_ROTATIONS, speed_sp=150, stop_action="hold")
    sleep(1)

for i in range(7):
    m1.run_to_rel_pos(position_sp=110, speed_sp=150, stop_action="hold")
    m2.run_to_rel_pos(position_sp=110, speed_sp=150, stop_action="hold")
    sleep(1)