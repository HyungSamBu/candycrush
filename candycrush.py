#!/usr/bin/env python
import ConfigParser
import os.path
import subprocess
import time
from tapioca_toggl import Toggl

def scaler(OldMin, OldMax, NewMin, NewMax):
    def fn(OldValue):
        return (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
    return fn

def configfile(config_path):
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    return config

class CandyCrush:
    def __init__(self, config):
        self.setup_apis(config)
        self.physical_pin = config.getint('Servo', 'physical_pin')
        self.servo_speed_180 = config.getfloat('Servo', 'speed_180')
        self.servodegrees = scaler(0, 180, 530, 2400)
        self.servo_last = 0
        self.setup_servod()

    # External APIs
    def setup_apis(self, config):
        toggl_token = config.get('API Tokens', 'toggl')
        self.toggl = Toggl(access_token=toggl_token)

    # Servo control
    def setup_servod(self):
        if not os.path.exists("/dev/servoblaster"):
            subprocess.call(["servod", "--idle-timeout=2500ms"])

    def set_servo(self, degrees):
        with open("/dev/servoblaster", "w") as f:
            servovalue = int(self.servodegrees(degrees))
            f.write("P1-{}={}us\n".format(self.physical_pin, servovalue))
        travel_time = abs(self.servo_last - degrees) / 180.0 * self.servo_speed_180
        self.servo_last = degrees
        time.sleep(travel_time)

    def dispense_candy(self):
        self.set_servo(180)
        time.sleep(1)
        for i in range(45):
            self.set_servo(180-i)
            time.sleep(0.05)
        self.set_servo(0)
        time.sleep(1)
        self.set_servo(180)
            
    # Run!
    def main(self):
        self.set_servo(0)
        time.sleep(2)
        self.set_servo(180)
        time.sleep(2)
        self.set_servo(90)
        time.sleep(2)
        self.set_servo(45)
        time.sleep(2)
        self.dispense_candy()

if  __name__ =='__main__':
    config = configfile('config')
    cc = CandyCrush(config)
    cc.main()
