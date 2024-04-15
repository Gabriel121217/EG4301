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

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

                            
pushpin = 21                                                  
GPIO.setup(pushpin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # using the internal Pull up resistor


#idk why but i need to define these
reset_pin = DigitalInOut(board.D6)
req_pin = DigitalInOut(board.D12)

# Create I2C bus as normal
i2c = board.I2C()  # uses board.SCL and board.SDA

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

# Initialize I2C bus
bus = smbus2.SMBus(1)

#initialise i2c device
pn532_1 = PN532_I2C(tca[0], debug=False, reset=reset_pin, req=req_pin)
pn532_2 = PN532_I2C(tca[1], debug=False, reset=reset_pin, req=req_pin)
pn532_3 = PN532_I2C(tca[2], debug=False, reset=reset_pin, req=req_pin)
pn532_4 = PN532_I2C(tca[3], debug=False, reset=reset_pin, req=req_pin)

#makes pn532 able to read stuff
pn532_1.SAM_configuration()
pn532_2.SAM_configuration()
pn532_3.SAM_configuration()
pn532_4.SAM_configuration()

#collects data

while True:
    out_1 = pn532_1.read_passive_target(timeout=128)
    read_1 = str([hex(i) for i in out_1])

    out_2 = pn532_2.read_passive_target(timeout=128)
    read_2 = str([hex(i) for i in out_2])

    out_3 = pn532_3.read_passive_target(timeout=128)
    read_3 = str([hex(i) for i in out_3])

    out_4 = pn532_4.read_passive_target(timeout=128)
    read_4 = str([hex(i) for i in out_3])
