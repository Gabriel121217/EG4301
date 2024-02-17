from time import sleep

def moveup():
    import RPi.GPIO as GPIO
    from time import sleep
    stop()
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, 1)

def movedown():
    import RPi.GPIO as GPIO
    from time import sleep
    stop()
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, 1)

def stop():
    import RPi.GPIO as GPIO
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(23, 0)
    GPIO.output(24, 0)
    GPIO.cleanup()

def process_input(action):
    if action == 'up':
        moveup()
    elif action == 'down':
        movedown()
    elif action == 'stop':
        stop()
    
while True:
    user_input = input("Enter 'up', 'down', or 'stop': ").lower()
    if user_input == 'stop':
        stop()
        break
    else:
        process_input(user_input)
        stop()
