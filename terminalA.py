import serial 
import time
import numpy as np

s = serial.Serial('COM5')

s.is_open
n = 0
while n<500:
    slotToSend = np.random.randint(1,5)
    time.sleep(slotToSend/1000*50)
    s.write(b'TA:')
    random = np.random.randint(0,256)
    s.write(random.to_bytes(1,byteorder="little"))
    a.write(b'\n')
    n = n+1

s.close()
