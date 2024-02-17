#Import all neccessary features to code.
import RPi.GPIO as GPIO
from time import sleep

#If code is stopped while the solenoid is active it stays active
#This may produce a warning if the code is restarted and it finds the GPIO Pin, which it defines as non-active in next line, is still active
#from previous time the code was run. This line prevents that warning syntax popping up which if it did would stop the code running.
GPIO.setwarnings(False)
#This means we will refer to the GPIO pins
#by the number directly after the word GPIO. A good Pin Out Resource can be found here https://pinout.xyz/
GPIO.setmode(GPIO.BCM)
#This sets up the GPIO 18 pin as an output pin
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


def moveup():
    GPIO.output(23, 1)

def movedown():
    GPIO.output(24, 1)

def stop():
    GPIO.output(23, 0)
    GPIO.output(24, 0)

while (True):    
    moveup()
    sleep(2)
    stop()
    sleep(1)
    movedown()
    sleep(2)
    stop()

