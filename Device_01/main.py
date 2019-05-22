#!/usr/bin/env python3
import sys, os, json
from ev3dev.ev3 import *
from time import time
from Ev3_def import *
from ibm_set import *
import ibmiotf.device

Con_motor = LargeMotor('outD')

Color = ColorSensor('in2') # 21 O / 1 X >>> 5
Color.mode = 'COL-REFLECT'

def Conveyor_go():
    motor_angle(Con_motor,300,-600)
    motor_angle(Con_motor,300,300)   
def CommandCallback(event):
    if event.command == "Scr_order":
        data = event.data
        print("got event " + json.dumps(data))
        Conveyor_go()
        Dev01.publishEvent("Finish_Supply", "json", data)
try:
    Dev01 = ibmiotf.device.Client(Device_01_TOKEN)
    Dev01.connect()
    Dev01.commandCallback = CommandCallback

except ibmiotf.ConnectionException as e:
    print(e)

while True:
    pass
