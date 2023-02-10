#!/usr/bin/python3

import RPi.GPIO as GPIO

class motor:
    def __init__(self, p1, p2, p3):
        GPIO.setmode(GPIO.BOARD)
        self.pin1 = p1
        self.pin2 = p2
        self.en_pin = p3
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.en_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.en_pin, 1000)  # start frequency
        self.pwm.start(25)

    def __del__(self):
        self.stop()
        self.pwm.stop()
        GPIO.cleanup()

    def stop(self):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)

    def turn_cw(self):
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.LOW)

    def turn_ccw(self):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.HIGH)
    
    def setSpeed(self, speed):
        if speed >= 0 and speed <= 100:
            self.pwm.ChangeDutyCycle(speed)
        else:
            print("requirement: 0 >= speed <= 100 is not fulfilled.")
