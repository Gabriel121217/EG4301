from gpiozero import Servo
from time import sleep

servo = Servo(22)

def lock():
    servo.max()

def unlock():
    servo.min()

for i in range(5):
    lock()
    sleep(0.5)
    unlock()
    sleep(0.5)
    lock()
    sleep(0.5)
    unlock()
    sleep(0.5)


def process_input(action):
    if action == "lock":
        lock()
    elif action == "unlock":
        unlock()
    
while True:
    unlock()
    user_input = input("Enter  'lock', 'unlock': ").lower()
    process_input(user_input)