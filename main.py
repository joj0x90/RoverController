#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import sys
import tty
import termios

# setting GPIO-Pins
M1_l = 3
M1_r = 5
M1_PWM = 12
M2_l = 7
M2_r = 11
M2_PWM = 32

speeds = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]

def _getch():
    fd = sys.stdin.fileno()
    old_setting = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_setting)
    return ch

class motorController:
    def __init__(self, p1, p2, p3):
        self.pin1 = p1
        self.pin2 = p2
        self.pin_pwm = p3
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.pin_pwm, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin_pwm, 1000)  # start frequency
        self.pwm.start(0)

    def stop(self):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)
        self.pwm.stop()

    def turn_cw(self):
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.LOW)

    def turn_ccw(self):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.HIGH)
    
    def setSpeed(self, speed):
        if speed > 0:
            self.pwm.ChangeFrequency(speed)
        else:
            print("speed has to be > 0")

class robotController:
    def __init__(self, m1, m2):
        self.motor1 = m1
        self.motor2 = m2
        self.motor1.stop()
        self.motor2.stop()

    def __del__(self):
        print("Destructor called ...terminating")
        self.motor1.stop()
        self.motor2.stop()
        GPIO.cleanup()

    def forward(self):
        print("driving forward...")
        self.motor1.turn_cw()
        self.motor2.turn_ccw()

    def backward(self):
        print("driving backwards...")
        self.motor1.turn_ccw()
        self.motor2.turn_cw()

    def turnLeft(self):
        print("turning left...")
        self.motor1.turn_cw()
        self.motor2.turn_cw()

    def turnRight(self):
        print("turning right...")
        self.motor1.turn_ccw()
        self.motor2.turn_ccw()

    def quit(self):
        print("quitting application...")
        self.stop()

    def stop(self):
        print("stopping...")
        self.motor1.stop()
        self.motor2.stop()

    def changeSpeed(self, speed):
        self.motor1.setSpeed(speed)
        self.motor2.setSpeed(speed)

if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    motor_l = motorController(M1_l, M1_r, M1_PWM)
    motor_r = motorController(M2_l, M2_r, M2_PWM)
    ctrl = robotController(motor_l, motor_r)
    ctrl.changeSpeed(0)
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
            elif key == 'q':
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
                print("unrecognized key event: " + key + " -> " + str(ord(key)))
                last = False

    except KeyboardInterrupt:
        print("interrupted by user. terminating Program...")
