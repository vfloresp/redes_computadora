import serial 
import time
import numpy as np

s = serial.Serial('COM5')

s.is_open
n = 0
while n<600:
    slotToSend = np.random.randint(1,5)
    time.sleep(slotToSend/1000*100)
    s.write(b'TB:')
    random = np.random.randint(0,256)
    s.write(random.to_bytes(1,byteorder="little"))
    s.write(b'\n')
    n = n+1

s.close()
