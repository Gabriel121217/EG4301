from time import sleep
from gevent import monkey
import RPi.GPIO as GPIO
from time import sleep
monkey.patch_all()
from gevent.pywsgi import WSGIServer
from flask import Flask, render_template
from flask_sock import Sock
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
from gpiozero import Servo
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

app = Flask(__name__)
app.config['SOCK_SERVER_OPTIONS'] = {'ping_interval': 25}

sock=Sock(app)

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
        if len(i)<4:
            digits+= "_"
        ans += digits
    return(ans)

def nfc_scan():
    total = []
    out_1 = pn532_1.read_passive_target(timeout=128)
    read_1 = hexa([hex(i) for i in out_1])

    out_2 = pn532_2.read_passive_target(timeout=128)
    read_2 = hexa([hex(i) for i in out_2])

    out_3 = pn532_3.read_passive_target(timeout=128)
    read_3 = hexa([hex(i) for i in out_3])

    total.append(read_1)
    total.append(read_2)
    total.append(read_3)
    return(total)
    
    print('Bay 1', cartridge[read_1],'\nBay 2', cartridge[read_2],'\nBay 3', cartridge[read_3])

####################################################################################################################################################################################
# Locking / Unlocking
####################################################################################################################################################################################
def lock():
    GPIO.setmode(GPIO.BCM)
    servo = Servo(22)
    servo.max()
    sleep(0.5)

def unlock():
    GPIO.setmode(GPIO.BCM)
    servo = Servo(22)
    servo.min()
    sleep(0.5)

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
    stopmotion()
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, 1)

def movedown():
    stopmotion()
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, 1)

def stopmotion():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(23, 0)
    GPIO.output(24, 0)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

@sock.route('/Up')
def Up(ws):
    print('up')
    moveup()

@sock.route('/RFIDScan')
def RFIDScan(ws):
    print('scan')
    message ='Scanning:' + str(nfc_scan())
    ws.send(message)

@sock.route('/Down')
def Down(ws):
    print('down')
    message='Unlocking:Loh Wai Keong'
    movedown()

@sock.route('/Stop')
def Stop(ws):
    print('stop')
    message='Unlocking:Loh Wai Keong'
    stopmotion()    
    
    
@sock.route('/Unlock')
def login(ws):
    print('login')
    message='Unlocking:Loh Wai Keong'
    unlock()
    moveup()
    sleep(10)
    stopmotion()
    ws.send(message)
    
if __name__=='__main__':
    server = '192.168.79.92'
    print('server starting')
    WSGIServer((server,4999),app).serve_forever()
    
