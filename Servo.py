import os.path
import subprocess
import time
from Utils import scaler

class Servo:
    def __init__(self, physical_pin, servo_speed_180, duty_min, duty_max):
        self.setup_servod()
        self.physical_pin = physical_pin
        self.servo_speed_180 = servo_speed_180
        self.servodegrees = scaler(0, 180, duty_min, duty_max)
        self.position = 0
        
    def setup_servod(self):
        if not os.path.exists("/dev/servoblaster"):
            subprocess.call(["servod", "--idle-timeout=2500ms"])

    def set_position(self, degrees, time = None):
        if time is None:
            return self._set_position(degrees)
        else:
            return self._set_position_slowly(degrees, time)

    def _set_position(self, degrees):
        with open("/dev/servoblaster", "w") as f:
            servovalue = int(self.servodegrees(degrees))
            f.write("P1-{}={}us\n".format(self.physical_pin, servovalue))

        # Block during travel
        travel_time = abs(self.position - degrees) / 180.0 * self.servo_speed_180
        self.position = degrees
        time.sleep(travel_time)

        
    def _set_position_slowly(self, degrees, total_time):
        travel_degrees = abs(self.position - degrees)
        total_travel_time = travel_degrees / 180.0 * self.servo_speed_180
        total_sleep_time = total_time - total_travel_time
        if total_sleep_time <= 0 or travel_degrees == 0:
            self._set_position(degrees)
            return
        tick_sleep_time = float(total_sleep_time) / travel_degrees
        step = 1 if self.position < degrees else -1
        for d in range(self.position, degrees + step, step):
            self._set_position(d)
            time.sleep(tick_sleep_time)
