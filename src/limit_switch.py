'''!
@file       limit_switch.py
@brief      Driver class for the DC motors
@details    This file contains methods that will be
            utilized by the DC motors for the
            entirety of the quarter.
@author     Cesar Santana
@author     Jakob Frabosilio
@author     Ayden Carbaugh
'''
import pyb

class LimitSwitch:
    def __init__(self, pin):
        # pass in pyb.pin obj with pull-up resistor, in)
        self.pin = pin
    def check(self):
        return self.pin.value()

if __name__ == '__main__':
    pinA6 = pyb.Pin(pyb.Pin.board.PA6, pyb.Pin.IN, pull = pyb.Pin.PULL_DOWN)
    while True:
        print(pinA6.value())