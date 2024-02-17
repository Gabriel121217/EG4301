import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

def set_gpio_high():
    GPIO.output(23, GPIO.HIGH)

def set_gpio_low():
    GPIO.output(23, GPIO.LOW)

# Example usage
set_gpio_high()  # Call this function to set GPIO pin 14 to high
time.sleep(2)    # Sleep for 2 seconds (for demonstration purposes)
set_gpio_low()   # Call this function to set GPIO pin 14 to low

# Cleanup GPIO
GPIO.cleanup()