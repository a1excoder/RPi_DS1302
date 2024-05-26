# RPi_DS1302
Python library for working with DS1302 for Raspberry Pi

## The main part of the source code is taken from here
```
# RTC_DS1302 - Python Hardware Programming Education Project For Raspberry Pi
# Copyright (C) 2015 Jason Birch
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#/****************************************************************************/
#/* RTC_DS1302                                                               */
#/* ------------------------------------------------------------------------ */
#/* V1.00 - 2015-08-26 - Jason Birch                                         */
#/* ------------------------------------------------------------------------ */
#/* Class to handle controlling a Real Time Clock IC DS1302.                 */
#/****************************************************************************/

```
https://github.com/ksaye/IoTDemonstrations/blob/master/RTC_DS1302/RTC_DS1302.py


### public guide that I found
https://kevinsaye.wordpress.com/2017/12/22/adding-an-ds1302-to-a-raspberry-pi-zero-w/

<p align="center">
 <img src="https://raw.githubusercontent.com/a1excoder/RPi_DS1302/main/ds1302.jpg"/>
</p>

## usage example
```python
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

```
