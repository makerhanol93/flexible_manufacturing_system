#!/usr/bin/env python3
import ibmiotf.device
import json
from time import time
from ibm_set import *

def order():
    print("주문정보를 입력해주세요.")
    print()
    
    name    = input(" 이름을 입력하시오: ")
    address = input(" 배송지역을 입력하세요 (1.서울, 2.대전, 3.부산): ")

    Green = input(" 'Green' 제품을 몇개 주문하시겠습니까? (최대 2개): ")
    Red = input(" 'Red' 제품을 몇개 주문하시겠습니까? (최대 2개): ")
    Blue = input(" 'Blue' 제품을 몇개 주문하시겠습니까? (최대 2개): ")

    _data = {"user" : [name, address] ,"order" : [Green, Red, Blue]}

    App01.publishEvent("Device_order", "json", _data)

    print()
    print("주문되었습니다. 감사합니다.")
    print()

def CommandCallback(event):
    pass

try:
    App01 = ibmiotf.device.Client(Order_TOKEN)
    App01.connect()
    App01.commandCallback = CommandCallback
    
except ibmiotf.ConnectionException as e:
    print(e)

while True:
    order()
    pass
