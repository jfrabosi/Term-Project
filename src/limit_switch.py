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
    '''!
    This class impliments a limit switch driver for the limit switches used
    on our term project
    '''
    def __init__(self, pin):
        '''!
        Creates a limit switch driver by initalizing
        a pin
        @param pin pin to be used for the limit switch
        '''
        # pass in pyb.pin obj with pull-up resistor, in)
        self.pin = pin
    def check(self):
        '''!
        This method checks whether or not the limit switch has beeen
        acuated and returns a pin value
        '''
        return self.pin.value()

if __name__ == '__main__':
    pinA6 = pyb.Pin(pyb.Pin.board.PB10, pyb.Pin.IN, pull = pyb.Pin.PULL_DOWN)
    while True:
        print(pinA6.value())