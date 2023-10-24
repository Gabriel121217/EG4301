from gpiozero import AngularServo
from time import sleep
import RPi.GPIO as GPIO
import time

servo = AngularServo(14, min_pulse_width=0.0006, max_pulse_width=0.0023)
# switch
GPIO.setmode(GPIO.BCM)                

while (True):
    servo.angle = 90


