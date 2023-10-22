import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin where the switch is connected
switch_pin = 17  # You can change this to the GPIO pin you're using

# Set the GPIO pin as an input with a pull-up resistor
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Define the function you want to trigger when the switch is pressed
def switch_pressed(channel):
    print("Switch pressed!")

# Add an event listener for the switch
GPIO.add_event_detect(switch_pin, GPIO.FALLING, callback=switch_pressed, bouncetime=200)

try:
    # Your main program logic can go here
    while True:
        # Do something here
        time.sleep(1)

except KeyboardInterrupt:
    pass

# Clean up the GPIO settings
GPIO.cleanup()
