#!/usr/bin/python3

import RTC_DS1302

ThisRTC = RTC_DS1302.RTC_DS1302(4, 27, 22)

DateTime = { "Year":0, "Month":0, "Day":0, "DayOfWeek":0, "Hour":0, "Minute":0, "Second":0 }

Data = ThisRTC.ReadDateTime(DateTime)
print('Date read was: ' + Data)

ThisRTC.CloseGPIO()
