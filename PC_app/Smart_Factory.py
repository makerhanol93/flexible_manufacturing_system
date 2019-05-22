#!/usr/bin/env python3
import ibmiotf.application
import json
from time import time
from ibm_set import *
import datetime

Brick_Inventory = {"Green":0,"Red":0,"Blue":0}

order_list = []
_value = []

def area(_data):
    if _data["user"][1] == '1':
        _data["user"][1] = "서울"

    elif _data["user"][1] == '2':
        _data["user"][1] = "대전"

    elif _data["user"][1] == '3':
        _data["user"][1] = "부산" 
def Brick_num(_data):
    Brick_Inventory["Green"] = _data["Green"]
    Brick_Inventory["Red"]   = _data["Red"]
    Brick_Inventory["Blue"]  = _data["Blue"]  
def Pub_order():
    if len(order_list) != 0:
        AppClient.publishCommand("EV3", "Device_01", "Scr_order", 
        "json",order_list.pop(0))
    pass
def Pub_dev_order():
    if len(order_list) == 1 and len(_value) == 0:
        AppClient.publishCommand("EV3", "Device_01", "Scr_order", 
        "json",order_list.pop(0))

        _value.append('go')
        pass
def EventCallback(event):
    
    #device_data
    if event.event == "Device_order":
        data = event.data
        area(data)
        order_list.append(data)
        Pub_dev_order()

        print()
        print("주문이 들어왔습니다!")
        s = datetime.datetime.now()
        print(s)
        print("------------------------------------------------")
        print("<< 방금 들어온 주문정보 >>")
        print("고객명: ", data["user"][0])
        print("배송지: ", data["user"][1])
        print("주문수량 ( Green:",data["order"][0],"개, Red:",data["order"][1],"개, Blue:",data["order"][2],"개 )")
        print("현재 대기중인 주문 수:", len(order_list),"개")
        print("------------------------------------------------")

    #robot
    if event.event == "Brick_num":
        data = event.data
        Brick_num(data)

    if event.event == "Request_order":
         Pub_order()

    if event.event == "Finish_Supply":
        data = event.data

        print()
        s = datetime.datetime.now()
        print(s)
        print("현재 '",data["user"][0],"' 고객님의 주문이 투입되었습니다.")

        AppClient.publishCommand("EV3", "Device_02", "Green_Go", 
        "json", data)

    if event.event == "Finish_G":
        data = event.data

        AppClient.publishCommand("EV3", "Device_03", "Red_set", 
        "json", data)
    
    if event.event == "Finish_set_R":
        data = event.data

        AppClient.publishCommand("EV3", "Device_02", "Red_Go", 
        "json", data)

    if event.event == "Finish_R":
        data = event.data

        AppClient.publishCommand("EV3", "Device_03", "Blue_set", 
        "json", data)

    if event.event == "Finish_set_B":
        data = event.data

        AppClient.publishCommand("EV3", "Device_02", "Blue_Go", 
        "json", data)

    if event.event == "Finish_B":
        data = event.data

        print()
        s = datetime.datetime.now()
        print(s)
        print("현재 '",data["user"][0],"' 고객님의 상품을 모두 담았습니다. 포장을 시작합니다.")

        AppClient.publishCommand("EV3", "Device_03", "Cover_set_Go", 
        "json", data)

    if event.event == "Finish_set_C":
        data = event.data

        AppClient.publishCommand("EV3", "Device_03", "Press_set", 
        "json", data)

    if event.event == "Finish_set_Press":
        data = event.data

        AppClient.publishCommand("EV3", "Device_02", "Check_Brick", 
        "json", data)

        AppClient.publishCommand("EV3", "Device_04", "Press_Go", 
        "json", data)
    
    if event.event == "Finish_Press":
        data = event.data

        AppClient.publishCommand("EV3", "Device_03", "Box_Out", 
        "json", data)
    
    if event.event == "Robot_Arm_Go":
        data = event.data
        AppClient.publishCommand("EV3", "Device_04", "Robot_Go", 
        "json", data)

        print()
        s = datetime.datetime.now()
        print(s)
        print("현재 '",data["user"][0],"' 고객님의 상품이 모두 준비되었습니다. 이제 '",data["user"][1],"' 지역으로 배송을 시작합니다.")

        if len(order_list) == 0 and _value[0] == 'go':
            del _value[0]
    
    ## Brick
    if event.event == "XXX":
        data = event.data
        if int(data) == 111:
            Stop_G = 1
        if int(data) == 222:
            Stop_R = 1
        if int(data) == 333:
            Stop_B = 1
def Sublist():
    AppClient.subscribeToDeviceEvents(
        deviceType="Customer", 
        deviceId="Order_01", 
        event="Device_order")

    AppClient.subscribeToDeviceEvents(
        deviceType="Customer", 
        deviceId="Order_02", 
        event="Device_order")

    AppClient.subscribeToDeviceEvents(
        deviceType="EV3", 
        deviceId="Device_01", 
        event="Finish_Supply")

    AppClient.subscribeToDeviceEvents(
        deviceType="EV3", 
        deviceId="Device_02", 
        event="Finish_G")

    AppClient.subscribeToDeviceEvents(
        deviceType="EV3", 
        deviceId="Device_02", 
        event="Finish_R")

    AppClient.subscribeToDeviceEvents(
        deviceType="EV3", 
        deviceId="Device_02", 
        event="Finish_B")
    
    AppClient.subscribeToDeviceEvents(
        deviceType="EV3", 
        deviceId="Device_03", 
        event="Finish_set_R")
    
    AppClient.subscribeToDeviceEvents(
        deviceType="EV3", 
        deviceId="Device_03", 
        event="Finish_set_B")

    AppClient.subscribeToDeviceEvents(
        deviceType="EV3", 
        deviceId="Device_03", 
        event="Finish_set_C")
    
    AppClient.subscribeToDeviceEvents(
        deviceType="EV3", 
        deviceId="Device_03", 
        event="Finish_set_Press")

    AppClient.subscribeToDeviceEvents(
        deviceType="EV3", 
        deviceId="Device_04", 
        event="Finish_Press")
    
    AppClient.subscribeToDeviceEvents(
        deviceType="EV3", 
        deviceId="Device_03", 
        event="Robot_Arm_Go")
    
    AppClient.subscribeToDeviceEvents(
        deviceType="EV3", 
        deviceId="Device_03", 
        event="Request_order")

    AppClient.subscribeToDeviceEvents(
        deviceType="EV3", 
        deviceId="Device_02", 
        event="XXX")
    
    AppClient.subscribeToDeviceEvents(
        deviceType="EV3", 
        deviceId="Device_02", 
        event="Brick_num")

try:
    AppClient = ibmiotf.application.Client(API_KEY_02)
    AppClient.connect()
    AppClient.deviceEventCallback = EventCallback
    Sublist()

except ibmiotf.ConnectionException as e:
    print(e)

while True:
    while True:
        if len(order_list) >= 1:
            _value[0] = 'go'
            break
        pass
    pass
