#!/usr/bin/env python3
import sys, os, json
from ev3dev.ev3 import *
from time import time
from Ev3_def import *


# 모터 객체
Topmotor = LargeMotor('outA')
Undermotor = LargeMotor('outC')

Gripper = MediumMotor('outD')

# 터치센서 객체
Touchsensorunder = TouchSensor('in1')
Touchsensortop = TouchSensor('in3')

def Robot_Arm_Start():

    Undermotor.run_forever(speed_sp=200)

    while True:
        if Touchsensorunder.value():
            Undermotor.stop(stop_action="hold")
            break
        pass
    
    # 보정
    #motor_angle(Undermotor,5*10,-200)

    Topmotor.run_forever(speed_sp=-200)

    while True:
        if Touchsensortop.value():
            Topmotor.stop(stop_action="hold")
            break
        pass
    
    current = time()
    while  time() - current < 1:
        pass 
def Gripper_Catch():

    motor_angle(Topmotor,10*20,200)

    #motor_time(Gripper,3,-300)
    motor_time(Gripper,2,300)

    motor_angle(Topmotor,10*20,-200)
def Gripper_Move():
    motor_angle(Undermotor,5*60,-200)
    pass
def Gripper_Move(_degree_setter):
    
    if _degree_setter == "서울":
        motor_angle(Undermotor,5*60,-200)

    if _degree_setter == "대전":
        motor_angle(Undermotor,5*90,-200)

    if _degree_setter == "부산":
        motor_angle(Undermotor,5*120,-200)

    pass
def Gripper_place():

    motor_angle(Topmotor,10*30,200)

    motor_time(Gripper,1.2,-100)
    #motor_angle(Topmotor,30,-200)

    motor_angle(Topmotor,10*30,-200)

    pass
def Gripper_Back():
    motor_angle(Undermotor,5*60,200)
    pass
