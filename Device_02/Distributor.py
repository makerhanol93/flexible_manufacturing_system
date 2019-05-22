#!/usr/bin/env python3
import sys, os, json
from ev3dev.ev3 import *
from time import time
from Ev3_def import *

Green_Brick = MediumMotor('outA')
Red_Brick = MediumMotor('outB')
Blue_Brick = MediumMotor('outC')

def Drop_Green_Brick():
    motor_time(Green_Brick,1,-200)
    motor_time(Green_Brick,1,200)
    pass

def Drop_Red_Brick():
    motor_time(Red_Brick,1,-200)
    motor_time(Red_Brick,1,200)
    pass

def Drop_Blue_Brick():
    motor_time(Blue_Brick,1,-200)
    motor_time(Blue_Brick,1,200)
    pass

