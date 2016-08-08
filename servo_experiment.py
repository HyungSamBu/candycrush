import RPIO as GPIO
import time

servo = GPIO.PWM.Servo()

# GPIO 17 = physical pin 11
servo.set_servo(17, 1500)
time.sleep(2)
servo.set_servo(17, 2000)
time.sleep(2)
servo.set_servo(17, 1000)
time.sleep(3)
servo.stop_servo(17)
