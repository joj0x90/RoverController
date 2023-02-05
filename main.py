#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import sys
import tty
import termios

# setting GPIO-Pins
M1_l = 2
M1_r = 3
M2_l = 4
M2_r = 17

def _getch():
    fd = sys.stdin.fileno()
    old_setting = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_setting)
    return ch

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
        print("quitting application...")

if __name__ == "__main__":
    ctrl = robotController()
    try:
        while True:
            key = _getch()
            if key == 'w':
                ctrl.forward()
            elif key == 's':
                ctrl.backward()
            elif key == 'a':
                ctrl.turnLeft()
            elif key == 'd':
                ctrl.turnRight()
            elif key == 'q':
                ctrl.quit()
                break
            else:
                print("unrecognized key event: " + key)

    except KeyboardInterrupt:
        print("interrupted by user. terminating Program...")
