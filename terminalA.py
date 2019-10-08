import serial 
import time
import numpy as numpy

s = serial.Serial('/dev/USB-SERIAL CH340')

s.is_open
n = 0
while n<1000:
    slotToSend = np.randInt(1,5)
    time.sleep(slotToSend/1000*50)
    s.write(b'TA:')
    random = np.randInt(0,256)
    s.write(random.to_bytes(1,byteorder="little"))
    n = n+1

s.close()
