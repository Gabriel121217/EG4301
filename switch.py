import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

                            
pushpin = 17                                                  
GPIO.setup(pushpin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # using the internal Pull up resistor
  
while True:
    print(GPIO.input(pushpin))
    time.sleep(0.2)
