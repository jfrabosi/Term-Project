'''!
@file       motor_driver.py
@brief      Driver class for the DC motors
@details    This file contains methods that will be
            utilized by the DC motors for the
            entirety of the quarter.
@author     Cesar Santana
@author     Jacob Frabosilio
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

