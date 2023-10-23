from gpiozero import AngularServo
from time import sleep
import RPi.GPIO as GPIO
import time

servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)
# switch
GPIO.setmode(GPIO.BCM)                
pushpin = 21                                                  
GPIO.setup(pushpin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # using the internal Pull up resistor

status = True

while (True):
    if GPIO.input(pushpin) == 0:
        if status:
            servo.angle = 90
            time.sleep(1)
            servo.angle = 0
            time.sleep(1)
            servo.angle = -90
            time.sleep(1)
            status = False
        else:
            print("locked")
            status = True
