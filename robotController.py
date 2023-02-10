#!/usr/bin/python3

class robot:
    def __init__(self, m1, m2):
        self.motor1 = m1
        self.motor2 = m2
        self.motor1.stop()
        self.motor2.stop()

    def __del__(self):
        print("Destructor called ...terminating")
        del self.motor1
        del self.motor2

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
        self.motor1.turn_ccw()
        self.motor2.turn_ccw()

    def turnRight(self):
        print("turning right...")
        self.motor1.turn_cw()
        self.motor2.turn_cw()

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
