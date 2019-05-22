#!/usr/bin/env python3
import sys, os, json
from ev3dev.ev3 import *
from time import time

def motor_time(_motor,_time):

    _motor.run_forever(speed_sp=300)
    current_time =time()

    while  time() - current_time < _time:
        pass

    moter.stop(stop_action="hold")

def motor_time(_motor,_time,_speed):

    _motor.run_forever(speed_sp=_speed)
    current_time =time()

    while  time() - current_time < _time:
        pass

    _motor.stop(stop_action="hold")

def motor_angle(_motor,_angle):

    _motor.reset()
    _motor.run_forever(speed_sp = 300)

    while _motor.position <= _angle:
        pass
   
    _motor.stop(stop_action = "hold")

def motor_angle(_motor,_angle,_speed):

    _motor.reset()
    _motor.run_forever(speed_sp = _speed)

    while abs(_motor.position) <= abs(_angle):
        pass
    
    _motor.stop(stop_action = "hold")
