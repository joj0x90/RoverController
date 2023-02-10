#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import sys
import tty
import termios

# own modules:
from motorContoller import motor
from robotController import robot

# setting GPIO-Pins
M1_l = 3
M1_r = 5
M1_PWM = 12
M2_l = 7
M2_r = 11
M2_PWM = 32

speeds = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

def _getch():
    fd = sys.stdin.fileno()
    old_setting = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_setting)
    return ch

if __name__ == "__main__":
    motor_l = motor(M1_l, M1_r, M1_PWM)
    motor_r = motor(M2_l, M2_r, M2_PWM)
    ctrl = robot(motor_l, motor_r)
    ctrl.changeSpeed(100)
    try:
        last = False
        while True:
            key = _getch()
            if key == 'w' or (last and key == 'A'):
                ctrl.forward()
                last = False
            elif key == 's' or (last and key == 'B'):
                ctrl.backward()
                last = False
            elif key == 'a' or (last and key == 'D'):
                ctrl.turnLeft()
                last = False
            elif key == 'd' or (last and key == 'C'):
                ctrl.turnRight()
                last = False
            elif key == 'q' or ord(key) == 3:
                ctrl.quit()
                break
            elif ord(key) == 91:    # e.g. 'arrow-up-key' consists of tis key and 'A'
                last = True
            elif key == ' ':
                ctrl.stop()
            elif ord(key) >= 48 and ord(key) <= 57:   # selecting a predefined speed profile
                print("setting speed to: " + str(speeds[ord(key) - 48]))
                ctrl.changeSpeed(speeds[ord(key) - 48])
            else:
#                print("unrecognized key event: " + key + " -> " + str(ord(key)))
                last = False

    except KeyboardInterrupt:
        print("interrupted by user. terminating Program...")
        del ctrl
