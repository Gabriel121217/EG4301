import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that the servo is connected to
servo_pin = 18

# Set the GPIO pin as an output
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM instance
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz (adjust as needed)

try:
    # Start the PWM with a duty cycle of 7.5% to stop the servo
    pwm.start(12.5)
    time.sleep(60)

    # Stop the PWM
    pwm.stop()

except KeyboardInterrupt:
    # Handle Ctrl+C to cleanly exit
    pwm.stop()
    GPIO.cleanup()