'''!

@file       encoder_driver.py
@brief      Driver class for quadrature encoders
@details    This file contains methods that will be
            utilized by the encoders throughout the
            entirety of the quarter.
@author     Cesar Santana
@author     Jacob Frabosilio
@author     Ayden Carbaugh
'''

import pyb

class EncoderDriver:
    '''!
    This class impliments an encoder driver for an ME 405 kit.
    '''
    
    def __init__(self, pin1, pin2, timer, CPR):
        '''!
        Creates an encoder driver by initializing pins on
        the shoe and configureing channels.
        @param pin1 pin associated with encoder channel A
        @param pin2 pin associated with encioder channel B
        @param timer timer associated with the encoder
        @param CPR number of encoder counts per revolution
        '''
        ## Position of the encoder
        self.pos = 0
        ## Change in position of the encoder
        self.delta = 0
        ## Starting time of the encoder
        self.start = 0
        ## Stopping time of the encoder
        self.stop = 0
        ## Configures pin1 for the encoder
        self.pin1 = pin1
        ## Configures pin 2 for the encoder
        self.pin2 = pin2
        ## Configures a timer for the encoder
        self.timer = timer
        
        ## Sets CPR value
        self.CPR = CPR
        
        ## Configures channel 1 to the encoder timer
        self.ch1 = self.timer.channel(1, pyb.Timer.ENC_A, pin=self.pin1)
        ## Configures channel 2 to the encoder timer
        self.ch2 = self.timer.channel(2, pyb.Timer.ENC_B, pin=self.pin2)
    
    def read(self):
        '''!
        This method calculates the position of the encoder
        and accounts for overflow.
        '''
        self.stop = abs(self.timer.counter())
        
        self.delta = self.stop - self.start
        
        if self.delta < -32768:
            
            self.delta = self.delta + 65536
            
        elif self.delta > 32768:
            self.delta = self.delta - 65536
        
        self.delta = self.delta * 360 / self.CPR
        self.pos += self.delta
        self.start = self.stop
        
        return self.pos
        
    def setpos(self, pos):
        self.pos = pos
        self.start = abs(self.timer.counter())
        
    def zero(self):
        '''!
        This methods resets the position of the encoder to zero.
        '''
        self.start = abs(self.timer.counter())
        self.pos = 0
        return self.pos