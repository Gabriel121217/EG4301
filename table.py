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
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


def moveup():
    GPIO.output(14, 1)

def movedown():
    GPIO.output(15, 1)

def stop():
    GPIO.output(14, 0)
    GPIO.output(15, 0)

while (True):    
    moveup()
    time.sleep(2)
    stop()
    time.sleep(1)
    movedown()
    time.sleep(2)
    stop()

