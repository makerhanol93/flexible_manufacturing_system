#!/usr/bin/env python3
import sys, os, json
import ibmiotf.device
from ev3dev.ev3 import *
from time import time
from Ev3_def import *
from ibm_set import *
from Distributor import *

Brick_Inventory = {"Green":8,"Red":8,"Blue":8}

def Add_brick(_color,_num):
    Brick_Inventory[_color] = _num
    pass
def Check_Brick():
    if Brick_Inventory["Green"] == 0:
        Dev02.publishEvent("XXX", "json", 111)
    elif Brick_Inventory["Red"] == 0:
        Dev02.publishEvent("XXX", "json", 222)
    elif Brick_Inventory["Blue"] == 0:
        Dev02.publishEvent("XXX", "json", 333)
def Brick_num():
    Dev02.publishEvent("Brick_num", "json", Brick_Inventory)
    pass
def CommandCallback(event):
    if event.command == "Green_Go":
        data = event.data
        print("got event " + json.dumps(data))

        for i in range(1, int(data["order"][0])+1 ):
            Drop_Green_Brick()
            Brick_Inventory["Green"] = int(Brick_Inventory["Green"]) - 1 

        Dev02.publishEvent("Finish_G", "json", data)
    if event.command == "Red_Go":
        data = event.data
        print("got event " + json.dumps(data))

        for i in range(1, int(data["order"][1])+1 ):
            Drop_Red_Brick()
            Brick_Inventory["Red"] = int(Brick_Inventory["Red"]) - 1 

        Dev02.publishEvent("Finish_R", "json", data)
    if event.command == "Blue_Go":
        data = event.data
        print("got event " + json.dumps(data))

        for i in range(1, int(data["order"][2])+1 ):
            Drop_Blue_Brick()
            Brick_Inventory["Blue"] = int(Brick_Inventory["Blue"]) - 1 

        Dev02.publishEvent("Finish_B", "json", data)
    if event.command == "Check_Brick":
        data = event.data
        Check_Brick()
        pass
    if event.command == "Brick_num":
        Brick_num()
        pass

try:
    Dev02 = ibmiotf.device.Client(Device_02_TOKEN)
    Dev02.connect()
    Dev02.commandCallback = CommandCallback

except ibmiotf.ConnectionException as e:
    print(e)

while True:
    pass
