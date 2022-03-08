
import utime
import cotask
import pyb
from encoder_driver import EncoderDriver
from motor_driver import MotorDriver
from controller import PID


trans_moe = MotorDriver(pyb.Pin.cpu.A10, pyb.Pin.cpu.B4, pyb.Pin.cpu.B5, pyb.Timer(3, freq = 20000))
trans_enc = EncoderDriver(pyb.Pin.cpu.B6, pyb.Pin.cpu.B7, pyb.Timer(4, prescaler = 0, period = 65535), CPR = 8192)
trans_con = PID(7, 45, 0, 0)

rad_moe = MotorDriver(pyb.Pin.cpu.A10, pyb.Pin.cpu.B4, pyb.Pin.cpu.B5, pyb.Timer(3, freq = 20000))
rad_enc = EncoderDriver(pyb.Pin.cpu.B6, pyb.Pin.cpu.B7, pyb.Timer(4, prescaler = 0, period = 65535), CPR = 8192)
rad_con = PID(5.5, 45, 0, 0)
moe_diameter = 0.366 #mm


radial = [0, 100, 105, 110, 115, 120, 125]
transverse = [5, 10, 5, 10]
trans_enc.zero()
rad_enc.zero()

# Figure our how to get encoder back to a neutral position after

def radial_motor():
    step_time = 0
    error = 10
    while True:
        # trans_moe.set_duty_cycle(50)
        for idx in range(0, len(radial)):
            # might be better to use error instead of a set time since most coordintaes
            # will be continuous and this will speed up process
            # Might need a PID controller for better accuracy
            while abs(error) >= 5:
                if error > 0:
                    rad_con.ref(radial[idx])
                    start_time = utime.ticks_ms()
                    utime.sleep_ms(10)
                    pos = rad_enc.read()
                    stop_time = utime.ticks_ms()
                    step_time = utime.ticks_diff(stop_time, start_time)
                    error = rad_con.compute(pos, step_time/1000, save_data=False)
                    trans_moe.set_duty_cycle(30)
                elif error < 0:
                    rad_con.ref(radial[idx])
                    start_time = utime.ticks_ms()
                    utime.sleep_ms(10)
                    pos = trans_enc.read()
                    stop_time = utime.ticks_ms()
                    step_time = utime.ticks_diff(stop_time, start_time)
                    error = rad_con.compute(pos, step_time/1000, save_data=False)
                    rad_moe.set_duty_cycle(-30)
                yield (0)
            trans_moe.set_duty_cycle(0)
            print('trans pos:', pos)
            error = 10
            # print('duty:', duty)
        yield(0)     


def transverse_motor():
    step_time = 0
    error = 10
    while True:
        # trans_moe.set_duty_cycle(50)
        for idx in range(0, len(transverse)):
            # might be better to use error instead of a set time since most coordintaes
            # will be continuous and this will speed up process
            # Might need a PID controller for better accuracy
            while abs(error) >= 5:
                if error > 0: 
                    trans_con.ref(transverse[idx])
                    start_time = utime.ticks_ms()
                    utime.sleep_ms(10)
                    ang = trans_enc.read()
                    print(ang)
                    pos = (ang/360)*(22/7)*moe_diameter
                    stop_time = utime.ticks_ms()
                    step_time = utime.ticks_diff(stop_time, start_time)
                    error = trans_con.compute(pos, step_time/1000, save_data=False)
                    trans_moe.set_duty_cycle(30)  
                elif error < 0:
                    trans_con.ref(transverse[idx])
                    start_time = utime.ticks_ms()
                    utime.sleep_ms(10)
                    ang = trans_enc.read()
                    pos = (ang/360)*(22/7)*moe_diameter
                    stop_time = utime.ticks_ms()
                    step_time = utime.ticks_diff(stop_time, start_time)
                    error = trans_con.compute(pos, step_time/1000, save_data=False)
                    trans_moe.set_duty_cycle(-30)
                yield(0)
            trans_moe.set_duty_cycle(0)
            print('rad pos:', pos)
            print('error:', error)
            error = 10
        yield(0)
        
# def mot_syr():
#     while True:
#         for idx in range(0, len(syringe)):
#             if syringe[idx] == 1:
#                 rad_moe.set_duty_cycle(30)
#             elif syringe[idx] == 0:
#                 rad_moe.set_duty_cycle(0)
#         yield(0)
                

if __name__ == "__main__":
    
        task_0 = cotask.Task(transverse_motor, name = 'Task_0', priority = 1, period = 10, profile=True, trace=False)
        # task_1 = cotask.Task(radial_motor, name = 'Task_1', priority = 1, period = 10, profile=True, trace=False)
        
        cotask.task_list.append(task_0)
        # cotask.task_list.append(task_1)
        
        # Need to figure out how to move the encoder back to neutral position 
        # once done with operation
        while True:
            cotask.task_list.pri_sched()