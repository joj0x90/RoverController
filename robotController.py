#!/usr/bin/python3

"""
    This class will control the robot and provide all methods to do so
"""
class robot:
    # create an instance of robot, by providing two instances of motor
    def __init__(self, m1, m2):
        self.motor1 = m1
        self.motor2 = m2
        self.motor1.stop()  # be sure that both motors are stopped
        self.motor2.stop()
        self.dbg = True    # set this to False to deactivate the output of this class

    def __del__(self):
        del self.motor1
        del self.motor2

    def forward(self):
        if self.dbg:
            print("driving forward...")
        self.motor1.turn_cw()
        self.motor2.turn_ccw()

    def backward(self):
        if self.dbg:
            print("driving backwards...")
        self.motor1.turn_ccw()
        self.motor2.turn_cw()

    def turnLeft(self):
        if self.dbg:
            print("turning left...")
        self.motor1.turn_ccw()
        self.motor2.turn_ccw()

    def turnRight(self):
        if self.dbg:
            print("turning right...")
        self.motor1.turn_cw()
        self.motor2.turn_cw()

    def quit(self):
        if self.dbg:
            print("quitting application...")
        self.stop()

    def stop(self):
        if self.dbg:
            print("stopping...")
        self.motor1.stop()
        self.motor2.stop()

    def changeSpeed(self, speed):
        if self.dbg:
            print("settig speed to: " + str(speed))
        self.motor1.setSpeed(speed)
        self.motor2.setSpeed(speed)
