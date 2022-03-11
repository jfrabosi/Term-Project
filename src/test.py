'''!
@file       
@brief      
@details    
@author     Jakob Frabosilio 
@author     Ayden Carbaugh 
@author     Cesar Santana
@date       02/22/2022
'''

import utime
import cotask
import pyb
from encoder_driver import EncoderDriver
from motor_driver import MotorDriverExtrude
from motor_driver import MotorDriver
from controller import PID
from limit_switch import LimitSwitch
from task_share import Share
from gcode_convert import carttopolar

## Diameter of the transverse motor gear in inches
moe_diameter = 0.366 

pinC1 = pyb.Pin(pyb.Pin.board.PC1, pyb.Pin.OUT_PP)
pinA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)
pinA1 = pyb.Pin(pyb.Pin.board.PA1, pyb.Pin.OUT_PP)
pinA10 = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
pinB4 = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
pinB5 = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
pinA9 = pyb.Pin(pyb.Pin.board.PA9, pyb.Pin.OUT_PP)
pinA7 = pyb.Pin(pyb.Pin.board.PA7, pyb.Pin.OUT_PP)
pinA6 = pyb.Pin(pyb.Pin.board.PA6, pyb.Pin.IN, pull = pyb.Pin.PULL_DOWN)
pinB3 = pyb.Pin(pyb.Pin.board.PB3, pyb.Pin.IN, pull = pyb.Pin.PULL_DOWN)
pinA8 = pyb.Pin(pyb.Pin.board.PA8, pyb.Pin.IN, pull = pyb.Pin.PULL_DOWN)

## Creates a transverse motor object
trans_moe = MotorDriver(pinC1, pinA0, pinA1, pyb.Timer(5, freq = 20000))
## Creates a radial motor object
rad_moe = MotorDriver(pinA10, pinB4, pinB5, pyb.Timer(3, freq = 20000))
## Creates an extrusion motor object
ext_moe = MotorDriverExtrude(pinA9, pyb.Timer(1, freq = 20000), 2, pinA7)

## Creates a transverse encoder object
trans_enc = EncoderDriver(pyb.Pin.cpu.C6, pyb.Pin.cpu.C7, pyb.Timer(8, prescaler = 0, period = 65535), CPR = 8192*360/((22/7)*moe_diameter))
## Creates a transverse controller object
trans_con = PID(7, 45, 0, 0)

## Creates a radial encoder object
rad_enc = EncoderDriver(pyb.Pin.cpu.B6, pyb.Pin.cpu.B7, pyb.Timer(4, prescaler = 0, period = 65535), CPR = 7122)
## Creates a radial controller object
rad_con = PID(5.5, 45, 0, 0)

## Creates an extrusion encoder object
ext_enc = EncoderDriver(pyb.Pin.cpu.A2, pyb.Pin.cpu.A3, pyb.Timer(2, prescaler = 0, period = 65535), CPR = 14254)
## Creates an extrusion controller object
ext_con = PID(5.5, 45, 0, 0)

radSwitch = LimitSwitch(pinA6)
transSwitch = LimitSwitch(pinB3)
extSwitch = LimitSwitch(pinA8)

trans_enc.zero()
rad_enc.zero()


def radial_switch():
    radSwitchFlag.put(0)
    while True:
        if radSwitch.check():
            radSwitchFlag.put(1)
        yield
        
def transverse_switch():
    transSwitchFlag.put(0)
    while True:
        if transSwitch.check():
            transSwitchFlag.put(1)
        yield
        
def extrusion_switch():
    extSwitchFlag.put(0)
    while True:
        if extSwitch.check():
            extSwitchFlag.put(1)
        yield

def radial_motor():
    '''!
    This generator homes our radial motor and then performs positional
    control based on a specified list of coordinates.
    '''
    ## Controller step time
    step_time = 0
    ## Controller error
    error = 10
    while abs(error) >= 5:
        rad_con.ref(20)
        start_time = utime.ticks_ms()
        utime.sleep_ms(10)
        pos = rad_enc.read()
        stop_time = utime.ticks_ms()
        step_time = utime.ticks_diff(stop_time, start_time)
        error = rad_con.compute(pos, step_time/1000, save_data=False)
        rad_moe.set_duty_cycle(50)
        yield (0)
    while not radSwitchFlag.get():
        rad_moe.set_duty_cycle(-100)
        yield(0)
    print('not!')
    rad_moe.set_duty_cycle(0)
    radFlag.put(1)
    rad_enc.setpos(-62)
    pos = trans_enc.read()
    while not transFlag.get():
        rad_moe.set_duty_cycle(1)
        yield(0)
    radSwitchFlag.put(0)
    transFlag.put(0)
    while True:
        for idx in range(0, len(radial)):
            while abs(error) >= 5:
                if error > 0:
                    rad_con.ref(radial[idx])
                    start_time = utime.ticks_ms()
                    utime.sleep_ms(10)
                    pos = rad_enc.read()
                    stop_time = utime.ticks_ms()
                    step_time = utime.ticks_diff(stop_time, start_time)
                    error = rad_con.compute(pos, step_time/1000, save_data=False)
                    rad_moe.set_duty_cycle(100)
                elif error < 0:
                    rad_con.ref(radial[idx])
                    start_time = utime.ticks_ms()
                    utime.sleep_ms(10)
                    pos = rad_enc.read()
                    stop_time = utime.ticks_ms()
                    step_time = utime.ticks_diff(stop_time, start_time)
                    error = rad_con.compute(pos, step_time/1000, save_data=False)
                    rad_moe.set_duty_cycle(-100)
                yield (0)
            rad_moe.set_duty_cycle(0)
            error = 10
            print('rad pos:', pos)
            radFlag.put(1)
            while not transFlag.get() and radFlag.get():
                rad_moe.set_duty_cycle(1)
                yield(0)
            transFlag.put(0)
            radFlag.put(0)
        yield(0)     


def transverse_motor():
    '''!
    This generator homes our transverse motor and then performs positional
    control based on a specified list of coordinates.
    '''
    step_time = 0
    error = 10
    while abs(error) >= 5:
        trans_con.ref(-.25)
        start_time = utime.ticks_ms()
        utime.sleep_ms(10)
        pos = trans_enc.read()
        stop_time = utime.ticks_ms()
        step_time = utime.ticks_diff(stop_time, start_time)
        error = trans_con.compute(pos, step_time/1000, save_data=False)
        trans_moe.set_duty_cycle(50)
        yield (0)
    while not transSwitchFlag.get():
        trans_moe.set_duty_cycle(-100)
        yield(0)
    print('bot!')
    trans_moe.set_duty_cycle(0)
    transFlag.put(1)
    trans_enc.setpos(14.5)
    pos = trans_enc.read()
    while not radFlag.get():
        trans_moe.set_duty_cycle(1)
        yield(0)
    transSwitchFlag.put(0)
    radFlag.put(0)
    extFlag.put(1)
    while True:
        for idx in range(0, len(transverse)):
            index.put(idx)
            while abs(error) >= 5:
                if error > 0: 
                    trans_con.ref(transverse[idx])
                    start_time = utime.ticks_ms()
                    utime.sleep_ms(10)
                    pos = trans_enc.read()
                    stop_time = utime.ticks_ms()
                    step_time = utime.ticks_diff(stop_time, start_time)
                    error = trans_con.compute(pos, step_time/1000, save_data=False)
                    trans_moe.set_duty_cycle(-100)
                elif error < 0:
                    trans_con.ref(transverse[idx])
                    start_time = utime.ticks_ms()
                    utime.sleep_ms(10)
                    pos = trans_enc.read()
                    stop_time = utime.ticks_ms()
                    step_time = utime.ticks_diff(stop_time, start_time)
                    error = trans_con.compute(pos, step_time/1000, save_data=False)
                    trans_moe.set_duty_cycle(100)
                yield(0)
            trans_moe.set_duty_cycle(0)
            error = 10
            transFlag.put(1)
            while not radFlag.get() and transFlag.get():
                trans_moe.set_duty_cycle(1)
                yield(0)
            radFlag.put(0)
            transFlag.put(0)
        yield(0)
        
def extrusion_motor():
    '''!
    This generator activates our extrusion motor based on a list of 
    specified coordinates.
    '''
    ext_moe.set_duty_cycle(1)
    while not extFlag.get():
        ext_moe.set_duty_cycle(1)
        yield(0)
    print('here!')
    while True:
        if extSwitchFlag.get():
            print('nope')
            ext_moe.set_duty_cycle(1)
            ext_enc.setpos(30)
            error = 10
            while abs(error) >= 5:
                ext_con.ref(150)
                start_time = utime.ticks_ms()
                utime.sleep_ms(10)
                pos = ext_enc.read()
                stop_time = utime.ticks_ms()
                step_time = utime.ticks_diff(stop_time, start_time)
                error = ext_con.compute(pos, step_time/1000, save_data=False)
                ext_moe.set_duty_cycle(100)
                print(error)
                yield(0)
            ext_moe.set_duty_cycle(1)
        val = index.get()
        if extrusion[val] == 1:
            ext_moe.set_duty_cycle(-70)
        elif extrusion[val] == 0:
            ext_moe.set_duty_cycle(1)
        yield(0)
                

if __name__ == "__main__":
     dataList = carttopolar()
     ## List of radial coordinates
     radial = dataList[2]
     ## List of transverse coordinates
     transverse = dataList[1]
     ## List of actuation values
     extrusion = dataList[0]
     
     ## Shared flag variable used to indicate when radial limit switch is pressed
     radSwitchFlag = Share('h', thread_protect = False, name = "radSwitchFlag")
     ## Shared flag variable used to indicate when transverse limit switch is pressed
     transSwitchFlag = Share('h', thread_protect = False, name = "transSwitchFlag")
     ## Shared flag variable used to indicate when extrusion limit switch is pressed
     extSwitchFlag = Share('h', thread_protect = False, name = "extSwitchFlag")
     ##
     radFlag = Share('h', thread_protect = False, name = "radFlag")
     ##
     transFlag = Share('h', thread_protect = False, name = "transFlag")
     ##
     extFlag = Share('h', thread_protect = False, name = "extFlag")
     ##
     index = Share('h', thread_protect = False, name = "index")
     
     ## Creates a radial_motor task
     task_0 = cotask.Task(radial_motor, name = 'Task_0', priority = 1, period = 10, profile=True, trace=False)
     ##Creates a transverse_motor task
     task_1 = cotask.Task(transverse_motor, name = 'Task_1', priority = 1, period = 10, profile=True, trace=False)
     ## Creates an extrusion_motor task
     task_2 = cotask.Task(extrusion_motor, name = 'Task_2', priority = 1, period = 10, profile=True, trace=False)
     ## Creates a radial_switch task
     task_3 = cotask.Task(radial_switch, name = 'Task 3', priority = 2, period = 10, profile=True, trace=False)
     ## Creates a transverse_switch task
     task_4 = cotask.Task(transverse_switch, name = 'Task 4', priority = 2, period = 10, profile=True, trace=False)
     ## Creates an extrusio_switch task
     task_5 = cotask.Task(extrusion_switch, name = 'Task 5', priority = 2, period = 10, profile=True, trace=False)
    
     cotask.task_list.append(task_0)
     cotask.task_list.append(task_1)
     cotask.task_list.append(task_2)
     cotask.task_list.append(task_3)
     cotask.task_list.append(task_4)
     cotask.task_list.append(task_5)

     while True:
         cotask.task_list.pri_sched()
