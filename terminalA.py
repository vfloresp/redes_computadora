import serial 
import time
import numpy as np

s = serial.Serial('COM5')

envios = 0
colisiones = 0
reenvio = 0
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
    print('TA: ' + random)
    time.sleep(slotToSend/1000*55)
    data = s.read_until(size=7)
    try:
        dataS = data.decode()
        source = dataS[:3]
        val = int(dataS[3:])
        if((source!="TC:" and source!="TB:") or val<0 or val>255):
            colisiones = colisiones + 1
            print("Colision")
        elif source == "TC:":
            print(dataS)
    except:
       print("Colision")
       colisiones = colisiones + 1

s.close()
