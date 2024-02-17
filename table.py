from time import sleep

def moveup():
    import RPi.GPIO as GPIO
    from time import sleep
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, 1)

def movedown():
    import RPi.GPIO as GPIO
    from time import sleep
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, 1)

def stop():
    import RPi.GPIO as GPIO
    GPIO.cleanup()

for i in range(20):
    moveup()
    sleep(2)
    stop()
    sleep(0.5)
    movedown()
    sleep(2)
    stop()
