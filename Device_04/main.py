#!/usr/bin/env python3
import sys, os, json
import ibmiotf.device
from ev3dev.ev3 import *
from time import time
from Ev3_def import *
from ibm_set import *
from Robot_Arm import *

Pakagingmotor = LargeMotor('outB')

def Pakagingmotor_Go():
    motor_angle(Pakagingmotor,150,150)

    current_time =time()

    while  time() - current_time < 2:
        pass
    
    motor_angle(Pakagingmotor,150,-150)
def Robot_Go():
    Robot_Arm_Start()
    Gripper_Catch()
    Gripper_Move()
    Gripper_place()
    Robot_Arm_Start()
def Robot_Go(_address):
    Robot_Arm_Start()
    Gripper_Catch()
    Gripper_Move(_address)
    Gripper_place()
    Robot_Arm_Start()
def CommandCallback(event):
    if event.command == "Press_Go":
        data = event.data
        Pakagingmotor_Go()
        Dev04.publishEvent("Finish_Press", "json", data)
    if event.command == "Robot_Go":
        data = event.data

        Robot_Go(data["user"][1])

try:
    Robot_Arm_Start()

    Dev04 = ibmiotf.device.Client(Device_04_TOKEN)
    Dev04.connect()
    Dev04.commandCallback = CommandCallback

except ibmiotf.ConnectionException as e:
    print(e)

while True:
    pass
