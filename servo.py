from gpiozero import Servo
from time import sleep

servo = Servo(22)

def lock():
    servo.max()

def unlock():
    servo.min()

for i in range(5):
    lock()
    sleep(0.5)
    unlock()
    sleep(0.5)
    lock()
    sleep(0.5)
    unlock()
    sleep(0.5)