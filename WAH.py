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


#dictionary
cartridge = {
    "['0x60', '0xbb', '0xe9', '0x55']": "Cartridge A",
    "['0xfe', '0x43', '0x22', '0x1d']": "Cartridge A",
    "['0xa2', '0x4', '0xdc', '0x51']":"Cartridge B",
    "['0xee', '0xed', '0x65', '0x1d']": "Cartridge B",
    "['0xe8', '0x96', '0xff', '0xd']": "Cartridge C",
    "['0x53', '0x8f', '0x12', '0x34']": "Cartridge C"
}

#idk why but i need to define these
reset_pin = DigitalInOut(board.D6)
req_pin = DigitalInOut(board.D12)

# Create I2C bus as normal
i2c = board.I2C()  # uses board.SCL and board.SDA

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

# BME280 sensor address (default address)
address = 0x76

# Initialize I2C bus
bus = smbus2.SMBus(1)

#initialise i2c device
pn532_1 = PN532_I2C(tca[0], debug=False, reset=reset_pin, req=req_pin)
pn532_2 = PN532_I2C(tca[1], debug=False, reset=reset_pin, req=req_pin)
pn532_3 = PN532_I2C(tca[2], debug=False, reset=reset_pin, req=req_pin)

#makes pn532 able to read stuff
pn532_1.SAM_configuration()
pn532_2.SAM_configuration()
pn532_3.SAM_configuration()

#collects data

while True:
    out_1 = pn532_1.read_passive_target(timeout=128)
    read_1 = str([hex(i) for i in out_1])

    out_2 = pn532_2.read_passive_target(timeout=128)
    read_2 = str([hex(i) for i in out_2])

    out_3 = pn532_3.read_passive_target(timeout=128)
    read_3 = str([hex(i) for i in out_3])

    print('Bay 1', cartridge[read_1],'\nBay 2', cartridge[read_2],'\nBay 3', cartridge[read_3])

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
    time.sleep()