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
        self.servodegrees = scaler(0, 180, 530, 2400)
        self.setup_servod()

    # External APIs
    def setup_apis(self, config):
        toggl_token = config.get('API Tokens', 'toggl')
        self.toggl = Toggl(access_token=toggl_token)

    # Servo control
    def setup_servod(self):
        if not os.path.exists("/dev/servoblaster"):
            subprocess.call(["servod", "--idle-timeout=1000ms"])

    def set_servo(self, physical_pin, degrees):
        with open("/dev/servoblaster", "w") as f:
            servovalue = int(self.servodegrees(degrees))
            f.write("P1-{}={}us\n".format(physical_pin, servovalue))

    # Run!
    def main(self):
        self.set_servo(11, 0)
        time.sleep(2)
        self.set_servo(11, 180)
        time.sleep(2)
        self.set_servo(11, 90)
        time.sleep(2)
        self.set_servo(11, 45)
        time.sleep(2)
        self.set_servo(11, 30)

if  __name__ =='__main__':
    config = configfile('config')
    cc = CandyCrush(config)
    cc.main()
