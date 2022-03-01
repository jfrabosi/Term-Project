
import utime
import cotask
import pyb
from TP_EncoderClass import EncoderClass
from TP_MotorDriver import MotorDriver
from TP_ClosedLoop import ClosedLoop


trans_enc = EncoderClass(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
trans_mot = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
trans_loop = ClosedLoop(3.5)

tran = [0, 100, 105, 110, 115, 120, 125]
trans_enc.zero()

# Figure our how to get encoder back to a neutral position after

def mot_trans():
    start = 0
    time = 0
    while True:
        for idx in range(0, len(tran)):
            # might be better to use error instead of a set time since most coordintaes
            # will be continuous and this will speed up process
            # Might need a PID controller for better accuracy
            while time <= 2000:
                ref_trans = tran[idx]
                trans_pos = trans_enc.update()
                duty_1 = trans_loop.update(ref_trans, trans_pos, 0, saveData=False)
                trans_mot.set_duty_cycle(duty_1)
                stop = utime.ticks_ms()
                time = utime.ticks_diff(stop, start)
            time = 0
            start = stop
            print('pos:', trans_pos)
            print('duty:', duty_1)
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