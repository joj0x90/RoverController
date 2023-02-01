#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import keyboard as kb

# setting GPIO-Pins
M1_l = 2
M1_r = 3
M2_l = 4
M2_r = 17

class robotController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(M1_l, GPIO.OUT)
        GPIO.setup(M1_r, GPIO.OUT)
        GPIO.setup(M2_l, GPIO.OUT)
        GPIO.setup(M2_r, GPIO.OUT)

    def forward(self):
        print("driving forward...")

    def backward(self):
        print("driving backwards...")

    def turnLeft(self):
        print("turning left...")

    def turnRight(self):
        print("turning right...")

    def quit(self):
        print("quit application.")

if __name__ == "__main__":
    ctrl = robotController()
    try:
        while(True):
            kb.on_press_key('w', ctrl.forward)
            kb.on_press_key('s', ctrl.backward)
            kb.on_press_key('a', ctrl.turnLeft)
            kb.on_press_key('d', ctrl.turnRight)
            kb.on_press_key('q', ctrl.quit)

    except KeyboardInterrupt:
        print("interrupted by user. terminating Program...")
