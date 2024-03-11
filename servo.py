import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

# Define servo PWM
servo_pwm = GPIO.PWM(22, 50)  # GPIO pin 22, PWM frequency 50Hz
servo_pwm.start(0)  # Start PWM with duty cycle 0 (neutral position)

# Function to move the servo to lock position (80 degrees)
def lock():
    duty_cycle = (170 / 18) + 2  # Convert degrees to duty cycle
    servo_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Adjust this delay as needed
    servo_pwm.ChangeDutyCycle(0)  # Stop PWM

# Function to move the servo to unlock position (-90 degrees)
def unlock():
    duty_cycle = (0 / 18) + 2  # Convert degrees to duty cycle
    servo_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Adjust this delay as needed
    servo_pwm.ChangeDutyCycle(0)  # Stop PWM

# Test the functions
try:
    # Move to lock position
    lock()
    time.sleep(2)  # Wait for 2 seconds
    # Move to unlock position
    unlock()
    time.sleep(2)  # Wait for 2 seconds

except KeyboardInterrupt:
    servo_pwm.stop()
    GPIO.cleanup()