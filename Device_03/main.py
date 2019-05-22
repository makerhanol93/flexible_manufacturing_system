#!/usr/bin/env python3
import sys, os, json
import ibmiotf.device
from ev3dev.ev3 import *
from time import time
from Ev3_def import *
from ibm_set import *

Con_motor = LargeMotor('outA')
Cover_motor = LargeMotor('outB')

Cover = ColorSensor('in1') # 21 O / 1 X >>> 5
Cover.mode = 'COL-REFLECT'

Blue_Color = ColorSensor('in2') # 21 O / 1 X >>> 5
Blue_Color.mode = 'COL-REFLECT'

Press_Color = ColorSensor('in3') # 21 O / 1 X >>> 5
Press_Color.mode = 'COL-REFLECT'

Red_Color = ColorSensor('in4') # 21 O / 1 X >>> 5
Red_Color.mode = 'COL-REFLECT'

def Conveyor_go():
    Con_motor.run_forever(speed_sp = -150)
def Cover_go():
    motor_time(Cover_motor,0.5,500)

    current_time =time()
    while  time() - current_time < 2:
        pass

    motor_time(Cover_motor,0.48,-500)
def CommandCallback(event):
    if event.command == "Red_set":  
        data = event.data

        Conveyor_go()

        while True:
            if Red_Color.value() > 3:
                Con_motor.stop(stop_action="hold")
                break
            pass
        
        motor_time(Con_motor,0.5,-150)

        Dev03.publishEvent("Finish_set_R", "json", data)
    if event.command == "Blue_set":
        data = event.data

        Conveyor_go()

        while True:
            if Blue_Color.value() > 3:
                Con_motor.stop(stop_action="hold")
                break
            pass

        motor_time(Con_motor,0.5,-150)

        Dev03.publishEvent("Finish_set_B", "json", data)
    if event.command == "Cover_set_Go":
        data = event.data

        Conveyor_go()

        while True:
            if Cover.value() > 3:
                Con_motor.stop(stop_action="hold")
                break
            pass

        motor_time(Con_motor,0.6,-150)

        Cover_go()

        Dev03.publishEvent("Finish_set_C", "json", data)  
    if event.command == "Press_set":
        data = event.data

        Conveyor_go()

        while True:
            if Press_Color.value() > 3:
                Con_motor.stop(stop_action="hold")
                break
            pass

        motor_time(Con_motor,0.5,-150)

        Dev03.publishEvent("Finish_set_Press", "json", data)
    if event.command == "Box_Out":
        data = event.data

        motor_time(Con_motor,3,-300)

        Dev03.publishEvent("Robot_Arm_Go", "json", data)
        Dev03.publishEvent("Request_order", "json", "order_push")
    
try:
    Dev03 = ibmiotf.device.Client(Device_03_TOKEN)
    Dev03.connect()
    Dev03.commandCallback = CommandCallback

except ibmiotf.ConnectionException as e:
    print(e)

while True:
    pass
