from time import sleep
from py532lib.i2c import*
from py532lib.frame import*
from py532lib.constants import*
import board
import adafruit_tca9548a
import busio
from adafruit_pn532.i2c import PN532_I2C
from digitalio import DigitalInOut
import time
import smbus2
import bme280
import RPi.GPIO as GPIO
import time
from gpiozero import AngularServo
from time import sleep

from dotenv import load_dotenv
load_dotenv()
import boto3

####################################################################################################################################################################################
# Setting up and definitions
####################################################################################################################################################################################

#idk why but i need to define these
reset_pin = DigitalInOut(board.D6)
req_pin = DigitalInOut(board.D12)

# Create I2C
# bus as normal
i2c = board.I2C()  # uses board.SCL and board.SDA

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

#GPIO things
GPIO.setmode(GPIO.BCM)

#GPIO setup
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

#servo PWM
servo_pwm = GPIO.PWM(22, 50)  # GPIO pin 22, PWM frequency 50Hz
servo_pwm.start(0)  # Start PWM with duty cycle 0 (neutral position)


####################################################################################################################################################################################
# NFC SCAN THINGS
####################################################################################################################################################################################

#dictionary
# cartridge = {
#     "['0x60', '0xbb', '0xe9', '0x55']": "Cartridge A",
#     "['0xfe', '0x43', '0x22', '0x1d']": "Cartridge A",
#     "['0xa2', '0x4', '0xdc', '0x51']":"Cartridge B",
#     "['0xee', '0xed', '0x65', '0x1d']": "Cartridge B",
#     "['0xe8', '0x96', '0xff', '0xd']": "Cartridge C",
#     "['0x53', '0x8f', '0x12', '0x34']": "Cartridge C"
# }

cartridge = {
    "60bbe955": "Cartridge A",
    "fe43221d": "Cartridge A",
    "a24dc51":"Cartridge B",
    "eeed651d": "Cartridge B",
    "e896ffd": "Cartridge C",
    "538f1234": "Cartridge C"
}
#initialise i2c device
pn532_1 = PN532_I2C(tca[0], debug=False, reset=reset_pin, req=req_pin)
pn532_2 = PN532_I2C(tca[1], debug=False, reset=reset_pin, req=req_pin)
pn532_3 = PN532_I2C(tca[2], debug=False, reset=reset_pin, req=req_pin)

#makes pn532 able to read stuff
pn532_1.SAM_configuration()
pn532_2.SAM_configuration()
pn532_3.SAM_configuration()

def hexa (hexa):
    ans = ''
    for i in hexa:
        digits = i[2:]
        ans += digits
    return(ans)

def nfc_scan():
    out_1 = pn532_1.read_passive_target(timeout=128)
    read_1 = hexa([hex(i) for i in out_1])

    out_2 = pn532_2.read_passive_target(timeout=128)
    read_2 = hexa([hex(i) for i in out_2])

    out_3 = pn532_3.read_passive_target(timeout=128)
    read_3 = hexa([hex(i) for i in out_3])

    print('Bay 1', cartridge[read_1],'\nBay 2', cartridge[read_2],'\nBay 3', cartridge[read_3])
        

####################################################################################################################################################################################
# Temperature
####################################################################################################################################################################################

def temp():
    # BME280 sensor address (default address)
    address = 0x76

    # Initialize I2C bus
    bus = smbus2.SMBus(1)

    # Load calibration parameters
    calibration_params = bme280.load_calibration_params(bus, address)
    data = bme280.sample(bus, address, calibration_params)

    temperature_celsius = data.temperature
    pressure = data.pressure
    humidity = data.humidity

    print("Temperature",temperature_celsius,"\nPressure",pressure, "\nhumidity",humidity)

####################################################################################################################################################################################
# Movement
####################################################################################################################################################################################

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
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(23, 0)
    GPIO.output(24, 0)
    GPIO.cleanup()

####################################################################################################################################################################################
# Locking / Unlocking
####################################################################################################################################################################################

def lock():
    duty_cycle = (170 / 18) + 2  # Convert degrees to duty cycle
    servo_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Adjust this delay as needed
    servo_pwm.ChangeDutyCycle(0)  # Stop PWM

def unlock():
    duty_cycle = (0 / 18) + 2  # Convert degrees to duty cycle
    servo_pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Adjust this delay as needed
    servo_pwm.ChangeDutyCycle(0)  # Stop PWM

####################################################################################################################################################################################
# Control Panel
####################################################################################################################################################################################

def process_input(action):
    if action == 'up':
        moveup()
    elif action == 'down':
        movedown()
    elif action == 'stop':
        stop()
    elif action == 'scan':
        nfc_scan()
    elif action == 'temp':
        temp()
    elif action == "lock":
        lock()
    elif action == "unlock":
        unlock()
    
while True:
    unlock()
    user_input = input("Enter 'scan', 'temp', 'up', 'down', 'lock', 'unlock' or 'stop': ").lower()
    if user_input == 'stop':
        stop()
    else:
        stop()
        process_input(user_input)

