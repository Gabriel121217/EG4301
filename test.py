import boto3
from dotenv import load_dotenv
load_dotenv()
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

dynamodb = boto3.resource('dynamodb')
Userlink = "Ryan Tan Cheng Lee"
CartridgeIDtable = dynamodb.Table('4301_Cartridge').get_item((Key={"Cartridge number":"CartrdgeIndex"}).get("Item")
A = CartridgeIDtable.get("A")
B = CartridgeIDtable.get("B")
C = CartridgeIDtable.get("C")
D = CartridgeIDtable.get("D")
print(A)
print(B)
print(C)
print(D)
Supplytable = dynamodb.Table('eg4301_patient').get_item((Key={"UniqueID":Userlink}).get("Item")
print(Suppplytable)