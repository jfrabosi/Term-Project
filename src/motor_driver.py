'''!
@file       motor_driver.py
@brief      Driver class for the DC motors
@details    This file contains methods that will be
            utilized by the DC motors for the
            entirety of the quarter.
@author     Cesar Santana
@author     Jakob Frabosilio
@author     Ayden Carbaugh
'''
import pyb

class MotorDriver:
    '''!
    This class impliments a motor driver for an ME 405 kit.
    '''
    def __init__(self, en_pin, in1pin, in2pin, timer):
        '''!
        Creates a motor driver by initializing GPIO
        pins and turning the motor off for safety.
        @param en_pin poin used to enable the motor
        @param in1pin pin used to send PWM signal to motor
        @param in2pin pin used to send PWM signal to motor
        @param timer timer associated with the motor
        '''
        
        ## Cofigures the en_pin for the motor
        self.en_pin = en_pin
        ## Configures the in1pin for the motor
        self.in1pin = in1pin
        ## Configures the in2pin for the motor
        self.in2pin = in2pin
        ## Configures a timer for the motor
        self.timer = timer
        ## Configures cghannel 1 to the motor timer
        self.ch1 = self.timer.channel(1, pyb.Timer.PWM, pin=self.in1pin)
        ## Configures channel 2 to the motor timer
        self.ch2 = self.timer.channel(2, pyb.Timer.PWM, pin=self.in2pin)
      
    def set_duty_cycle(self, level):
        '''!
        This method sets the duty cycle to be sent
        to the motor to the given level. Posotive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed intiger holding the duty
               cycle of the voltage sent to the motor
        '''
        self.en_pin.high()
        self.in1pin.low() 
        self.in2pin.low() 

        if level > 100:
            self.ch1.pulse_width_percent(100)
            self.ch2.pulse_width_percent(0)  
        elif level < -100:
            self.ch1.pulse_width_percent(0)
            self.ch2.pulse_width_percent(100)
        elif level>0:
            self.ch1.pulse_width_percent(abs(level))
            self.ch2.pulse_width_percent(0)
        elif level<0:
            self.ch1.pulse_width_percent(0)
            self.ch2.pulse_width_percent(abs(level))

class MotorDriverExtrude:
    '''!
    This class impliments a motor driver for an ME 405 kit.
    '''
    def __init__(self, pwmPin, timer, channel, directionPin):
        '''!
        Creates a motor driver by initializing GPIO
        pins and turning the motor off for safety.
        @param en_pin p 
        '''
        ## Configures the in1pin for the motor
        self.pwmPin = pwmPin
        ## Configures a timer for the motor
        self.timer = timer
        self.channel = channel
        self.dirPin = directionPin
        ## Configures cghannel 1 to the motor timer
        self.ch = self.timer.channel(self.channel, pyb.Timer.PWM, pin=self.pwmPin)
      
    def set_duty_cycle(self, level):
        '''!
        This method sets the duty cycle to be sent
        to the motor to the given level. Posotive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed intiger holding the duty
               cycle of the voltage sent to the motor
        '''
        if level > 100:
            self.ch.pulse_width_percent(100)
            self.dirPin.high()
        elif level < -100:
            self.ch.pulse_width_percent(100)
            self.dirPin.low()
        elif level>0:
            self.ch.pulse_width_percent(abs(level))
            self.dirPin.high()
        elif level<0:
            self.ch.pulse_width_percent(abs(level))
            self.dirPin.low()
            
# if __name__ == '__main__':
#     pinC1 = pyb.Pin(pyb.Pin.board.PC1, pyb.Pin.OUT_PP)
#     pinA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
#     pinA1 = pyb.Pin(pyb.Pin.board.PA1, pyb.Pin.OUT_PP)
#     pinA10 = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
#     pinB4 = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
#     pinB5 = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
#     pinB10 = pyb.Pin(pyb.Pin.board.PA9, pyb.Pin.OUT_PP)
#     pinA7 = pyb.Pin(pyb.Pin.board.PA7, pyb.Pin.OUT_PP)
#     trans_moe = MotorDriver(pinC1, pinA0, pinA1, pyb.Timer(5, freq = 20000))
#     rad_moe = MotorDriver(pinA10, pinB4, pinB5, pyb.Timer(3, freq = 20000))
#     ext_moe = MotorDriverExtrude(pinB10, pyb.Timer(1, freq = 20000), 2, pinA7)
#     while True:
#         ext_moe.set_duty_cycle(-80)
    
