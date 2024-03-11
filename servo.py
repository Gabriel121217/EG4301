from gpiozero import Servo
from time import sleep

servo = Servo(22)

def lock():
    servo.max()

def unlock():
    servo.min()

for i in range(5):
    servo.min()
    sleep(0.5)
    servo.mid()
    sleep(0.5)
    servo.max()
    sleep(0.5)