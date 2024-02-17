from time import sleep

def moveup():
    import RPi.GPIO as GPIO
    from time import sleep
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, 1)
    sleep(5)
    stop()

def movedown():
    import RPi.GPIO as GPIO
    from time import sleep
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, 1)
    sleep(5)
    stop()

def stop():
    import RPi.GPIO as GPIO
    GPIO.cleanup()


while True:
    command = input("What do I do?:")
    if command == 'up':
        moveup()
    elif command == 'down':
        movedown()
