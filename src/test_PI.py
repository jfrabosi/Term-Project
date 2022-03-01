
import utime
import cotask
import pyb
from encoder_driver import EncoderDriver
from motor_driver import MotorDriver
from controller import PID


moe = MotorDriver(pyb.Pin.cpu.A10, pyb.Pin.cpu.B4, pyb.Pin.cpu.B5, pyb.Timer(3, freq = 20000))
enc = EncoderDriver(pyb.Pin.cpu.B6, pyb.Pin.cpu.B7, pyb.Timer(4, prescaler = 0, period = 65535))
con = PID(5.5, 35, 0, 360)


tran = [0, 100, 105, 110, 115, 120, 125]
enc.zero()

# Figure our how to get encoder back to a neutral position after

def mot_trans():
    start = 0
    time = 0
    step_time = 0
    while True:
        for idx in range(0, len(tran)):
            # might be better to use error instead of a set time since most coordintaes
            # will be continuous and this will speed up process
            # Might need a PID controller for better accuracy
            while time <= 2500:
                con.ref(tran[idx])
                start_time = utime.ticks_ms()
                utime.sleep_ms(10)
                pos = enc.read()
                stop_time = utime.ticks_ms()
                step_time = utime.ticks_diff(stop_time, start_time)
                duty = con.compute(pos, step_time/1000, save_data=False)
                moe.set_duty_cycle(duty)
                stop = utime.ticks_ms()
                time = utime.ticks_diff(stop, start)
            time = 0
            start = stop
            print('pos:', pos)
            print('duty:', duty)
        yield(0)
        
    
# def mot_rad():
    
# def mot_syr():
    

if __name__ == "__main__":
    
        task_0 = cotask.Task(mot_trans, name = 'Task_0', priority = 1, period = 10, profile=True, trace=False)
        
        cotask.task_list.append(task_0)

        
        # Need to integrate this while loop into the transverse motor task
        # Need to figure out how to move the encoder back to neutral position 
        # once done with operation
        while True:
            # for idx in range(0, len(tran)):
            #     while time <= 2000:
            #         ref_trans = tran[idx]
            #         trans_pos = trans_enc.update()
            #         duty_1 = trans_loop.update(ref_trans, trans_pos, 0, saveData=False)
            #         trans_mot.set_duty_cycle(duty_1)
            #         stop = utime.ticks_ms()
            #         time = utime.ticks_diff(stop, start)
            #     time = 0
            #     start = stop
            #     print('pos:', trans_pos)
            #     print('duty:', duty_1)

            # break
            cotask.task_list.pri_sched()