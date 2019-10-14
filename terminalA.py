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

    #Reinicia los parametros de ack y repeticion
    ack = False
    rep = 0

    #Calcula el slot aleatorio para enviar
    slotToSend = np.random.randint(1,5)
    time.sleep(slotToSend/1000*55)
    random = str(np.random.randint(0,256))
    s.write(b'TA:'+random.encode()+b'\n')
    n = n + 1
    print('TA: ' + random)

    #Ciclo para esperar el ack
    while ack == False and rep < 3:
        #Espera un ciclo entre cada lectura
        time.sleep(1/1000*55)
        data = s.read_until(size=7)
        #Intenta decodificar los bytes recibidos
        try:
            dataS = data.decode()
            if len(dataS>4):
                source = dataS[:3]
                val = int(dataS[3:])
                if((source!="TC:" and source!="TB:") or val<0 or val>255):
                    print("Colision")
                    colisiones = colisiones + 1
                    rep = rep +1
                    s.write(b'TA:'+ random.encode()+b'\n')
                #El ack se recibio correctamente
                elif source == "TC:":
                    print(dataS)
                    ack = True
        #Si marca error trata de reenviar
        except:
            print("Colision")
            colisiones = colisiones + 1
            rep = rep + 1
            s.write(b'TA:'+ random.encode()+b'\n')

s.close()
