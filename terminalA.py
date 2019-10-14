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
    ack = False
    rep = 0
    slotToSend = np.random.randint(1,5)
    time.sleep(slotToSend/1000*55)
    s.write(b'TA:')
    random = str(np.random.randint(0,256))
    s.write(random.encode())
    s.write(b'\n')
    n = n+1
    print('TA: ' + random)
    while ack == False and rep < 3:
        time.sleep(slotToSend/1000*55)
        data = s.read_until(size=7)
        if (len(data)<7):
            try:
                dataS = data.decode()
                source = dataS[:3]
                val = int(dataS[3:])
                if((source!="TC:" and source!="TB:") or val<0 or val>255):
                    colisiones = colisiones + 1
                    print("Colision")
                    rep = rep +1
                    s.write(b'TA:')
                    s.write(random.encode())
                    s.write(b'\n')
                elif source == "TC:":
                    print(dataS)
                    ack = True
            except:
                print("Colision")
                colisiones = colisiones + 1
                rep = rep + 1
                s.write(b'TA:')
                s.write(random.encode())
                s.write(b'\n')

s.close()
