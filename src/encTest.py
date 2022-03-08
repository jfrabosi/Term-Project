from encoder_driver import EncoderDriver
import pyb
import utime

testEnc = EncoderDriver(pyb.Pin.cpu.C6, pyb.Pin.cpu.C7, pyb.Timer(3, prescaler = 0, period = 65535), CPR = 7122)

testEnc.zero()

while True:
    print(testEnc.read())