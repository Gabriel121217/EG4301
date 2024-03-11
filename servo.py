from gpiozero import Servo
from time import sleep

servo = Servo(22)
val = -1

while True:
    servo.value = val
    sleep(0.1)
    val = val + 0.1
    if val > 1:
        val = -1
