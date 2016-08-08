#!/usr/bin/env python
import os.path
import subprocess
import time

def scaler(OldMin, OldMax, NewMin, NewMax):
    def fn(OldValue):
        return (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
    return fn

def setup_servod():
    if not os.path.exists("/dev/servoblaster"):
        subprocess.call(["servod", "--idle-timeout=1000ms"])
    

def set_servo(physical_pin, degrees):
    servodegrees = scaler(0, 180, 530, 2400)
    with open("/dev/servoblaster", "w") as f:
        servovalue = int(servodegrees(degrees))
        f.write("P1-{}={}us\n".format(physical_pin, servovalue))

def main():
    set_servo(11, 0)
    time.sleep(2)
    set_servo(11, 180)
    time.sleep(2)
    set_servo(11, 90)
    time.sleep(2)
    set_servo(11, 45)
    time.sleep(2)
    set_servo(11, 30)

if  __name__ =='__main__':
    main()
