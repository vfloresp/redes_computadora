import serial 
import time
import numpy as np

s = serial.Serial('COM5')

s.is_open
n = 0
while n<500:
    slotToSend = np.random.randint(1,5)
    time.sleep(slotToSend/1000*55)
    s.write(b'TA:')
    random = str(np.random.randint(0,256))
    s.write(random.encode())
    s.write(b'\n')
    n = n+1
    time.sleep(slotToSend/1000*55)
    data = s.read_until(size=7)
    try:
       dataS = data.decode()
       source = dataS[:2]
       if source == "TC":
           print(dataS)
    except:
       print("Colision")

s.close()
