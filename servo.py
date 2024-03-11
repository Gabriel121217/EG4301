from gpiozero import Servo
from time import sleep

servo = Servo(22)

def lock():
    servo.value = 0.88

def unlock():
    servo.value = 0

for i in range(5):
    lock()
    sleep(2)
    unlock ()