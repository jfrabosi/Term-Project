
import cotask
import pyb
from TP_EncoderClass import EncoderClass
from TP_MotorDriver import MotorDriver
from TP_ClosedLoop import ClosedLoop

rad = []
tran = [0, 40, 70, -20, -80, 0]

trans_enc = EncoderClass(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
trans_mot = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
trans_loop = ClosedLoop(0.92)

def mot_trans():
    while True:
        for idx in range(0, len(tran)):
            ref_trans = tran[idx]
            trans_pos = trans_enc.update()
            duty_1 = trans_loop.update(ref_trans, trans_pos, 0, savedata=False)
            trans_mot.set_duty_cycle(duty_1)
        yield(0)
        
    
# def mot_rad():
    
# def mot_syr():
    

if __name__ == "__main__":
    
        task_0 = cotask.Task(mot_trans, name = 'Task_0', priority = 1, period = 10, profile=True, trace=False)
        
        cotask.task_list.append(task_0)

        while True:
            cotask.task_list.pri_sched()