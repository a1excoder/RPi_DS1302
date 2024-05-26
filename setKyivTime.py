from datetime import datetime
from json import loads

import requests as req
import os


import RTC_DS1302


try:
    resp = req.get("http://worldtimeapi.org/api/timezone/Europe/Kyiv")
    if resp.status_code == 200:
        dt = loads(resp.text)['datetime']

        dt_obj = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S.%f%z')
        print(f"setting {dt_obj}")

        ThisRTC = RTC_DS1302.RTC_DS1302(4, 27, 22)

        ThisRTC.WriteDateTime(
        dt_obj.year - 2000, 
        dt_obj.month, 
        dt_obj.day, 
        dt_obj.weekday(), 
        dt_obj.hour, 
        dt_obj.minute, 
        dt_obj.second)
        
        ThisRTC.CloseGPIO()
    else:
        print(f"[!] response status code: {resp.status_code}")

except:
    print("[!] exception")
