#!$WORKON_HOME/candies/bin/python

# Setup virtualenv
#import os
#activate_this = os.environ['WORKON_HOME'] + '/candies/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))

import time
from Servo import Servo
from Utils import configfile
from tapioca_toggl import Toggl

class CandyCrush:
    def __init__(self, config):
        self.config = config
        self.setup_servo(config)
        self.setup_apis(config)

    # External APIs
    def setup_apis(self, config):
        toggl_token = config.get('API Tokens', 'toggl')
        self.toggl = Toggl(access_token=toggl_token)

    # Servo control
    def setup_servo(self, config):
        physical_pin = config.getint('Servo', 'physical_pin')
        servo_speed_180 = config.getfloat('Servo', 'speed_180')
        duty_min = config.getfloat('Servo', 'duty_min')
        duty_max = config.getfloat('Servo', 'duty_max')
        self.servo = Servo(physical_pin, servo_speed_180, duty_min, duty_max)

    def dispense_candy(self):
        servo = self.servo
        if not servo.position == 180:
            servo.set_position(180)
            time.sleep(1)
        servo.set_position(90, 1.5)
        servo.set_position(0, 0.5)
        time.sleep(1)
        servo.set_position(180, 1.5)
            
    # Run!
    def main(self):
        self.servo.set_position(180)
        self.dispense_candy()

if  __name__ =='__main__':
    config = configfile('config')
    cc = CandyCrush(config)
    cc.main()
