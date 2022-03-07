
import utime
import cotask
import pyb
from encoder_driver import EncoderDriver
from motor_driver import MotorDriver
from controller import PID


trans_moe = MotorDriver(pyb.Pin.cpu.A10, pyb.Pin.cpu.B4, pyb.Pin.cpu.B5, pyb.Timer(3, freq = 20000))
trans_enc = EncoderDriver(pyb.Pin.cpu.B6, pyb.Pin.cpu.B7, pyb.Timer(4, prescaler = 0, period = 65535))
trans_con = PID(5.5, 45, 0, 0)

rad_moe = MotorDriver(pyb.Pin.cpu.A10, pyb.Pin.cpu.B4, pyb.Pin.cpu.B5, pyb.Timer(3, freq = 20000))
rad_enc = EncoderDriver(pyb.Pin.cpu.B6, pyb.Pin.cpu.B7, pyb.Timer(4, prescaler = 0, period = 65535))
rad_con = PID(5.5, 45, 0, 0)
moe_diameter = 6.35 #mm


tran = [0, 100, 105, 110, 115, 120, 125]
radial = [0, 50, 100, 136, 110, 140, 60, 80, 35, 0, 65, 155, 200, 130]
trans_enc.zero()
rad_enc.zero()

# Figure our how to get encoder back to a neutral position after

def transverse_motor():
    start = 0
    time = 0
    step_time = 0
    while True:
        # trans_moe.set_duty_cycle(50)
        for idx in range(0, len(tran)):
            # might be better to use error instead of a set time since most coordintaes
            # will be continuous and this will speed up process
            # Might need a PID controller for better accuracy
            while time <= 2000:
                trans_con.ref(tran[idx])
                start_time = utime.ticks_ms()
                utime.sleep_ms(10)
                pos = trans_enc.read()
                stop_time = utime.ticks_ms()
                step_time = utime.ticks_diff(stop_time, start_time)
                duty = trans_con.compute(pos, step_time/1000, save_data=False)
                trans_moe.set_duty_cycle(duty)
                stop = utime.ticks_ms()
                time = utime.ticks_diff(stop, start)
            time = 0
            start = stop
            print('pos:', pos)
            print('duty:', duty)
        yield(0)
        
def radial_motor():
    start = 0
    time = 0
    step_time = 0
    while True:
        # trans_moe.set_duty_cycle(50)
        for idx in range(0, len(radial)):
            # might be better to use error instead of a set time since most coordintaes
            # will be continuous and this will speed up process
            # Might need a PID controller for better accuracy
            while time <= 2000:
                rad_con.ref(radial[idx])
                start_time = utime.ticks_ms()
                utime.sleep_ms(10)
                pos = rad_enc.read()
                dist = (pos/360)*(22/7)*moe_diameter
                stop_time = utime.ticks_ms()
                step_time = utime.ticks_diff(stop_time, start_time)
                duty = rad_con.compute(dist, step_time/1000, save_data=False)
                rad_moe.set_duty_cycle(duty)
                stop = utime.ticks_ms()
                time = utime.ticks_diff(stop, start)
            time = 0
            start = stop
            print('dist:', dist)
            # print('duty:', duty)
        yield(0)

        
# def mot_syr():
    

if __name__ == "__main__":
    
        task_0 = cotask.Task(radial_motor, name = 'Task_0', priority = 1, period = 10, profile=True, trace=False)
        task_1 = cotask.Task(transverse_motor, name = 'Task_1', priority = 2, period = 10, profile=True, trace=False)
        
        cotask.task_list.append(task_0)
        # cotask.task_list.append(task_1)
        
        # Need to figure out how to move the encoder back to neutral position 
        # once done with operation
        while True:
            # trans_moe.set_duty_cycle(50)
            cotask.task_list.pri_sched()