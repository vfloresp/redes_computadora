import serial 
import time
import numpy as np

s = serial.Serial('COM8')

s.is_open
n = 0
#Envia constantemente tramas en una ranura aletoria
while n<600:
    slotToSend = np.random.randint(1,5)
    time.sleep(slotToSend/1000*55)
    random = str(np.random.randint(0,256))
    s.write(b'TB:'+random.encode()+b'\n')
    n = n+1

s.close()
