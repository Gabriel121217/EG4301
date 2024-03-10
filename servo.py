from gpiozero import AngularServo
from time import sleep
import RPi.GPIO as GPIO
import time


#servo
servo = AngularServo(22, min_pulse_width=0.0006, max_pulse_width=0.00250)


def lock(deg):
    servo.angle = 80

def unlock(deg):
    servo.angle = -90

while True:
    user_input = input("Enter degree")
    lock(user_input)

