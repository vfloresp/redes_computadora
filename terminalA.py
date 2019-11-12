import serial 
import time
import numpy as np

s = serial.Serial('COM7')

envios = 0
colisiones = 0
reenvio = 0
s.is_open
n = 0
while n<500:

    #Reinicia los parametros de ack y repeticion
    ack = False
    ret = 0

    #Calcula el slot aleatorio para enviar
    slotToSend = np.random.randint(1,5)
    time.sleep(slotToSend/1000*55)
    random = str(np.random.randint(0,256))
    s.write(b'TA:'+random.encode()+b'\n')
    n = n + 1
    print('TA: ' + random)
    Ini = int(round(time.time() * 1000))
    #Ciclo para esperar el ack
    while ack == False and ret <= 3 and (Ini- int(round(time.time() * 1000)))<320:
        data = s.read_until(size=7)
        #Intenta decodificar los bytes recibidos
        try:
            dataS = data.decode()
            source = dataS[:3]
            val = dataS[3:]
            validarVal = int(val)
            if(source!="TC:" and source!="TB:"):
                print("Colision")
                if ret < 3:
                    colisiones = colisiones + 1
                    ret = ret +1
                    s.write(b'TA:'+ random.encode()+b'\n')
            #El ack se recibio correctamente
            elif source == "TC:":
                print(dataS)
                ack = True
        #Si marca error trata de reenviar
        except Exception as e:
            if str(e) != "invalid literal for int() with base 10: ''":
                print("Colision")
                if ret < 3:
                    colisiones = colisiones + 1
                    ret = ret + 1
                    s.write(b'TA:'+ random.encode()+b'\n')

        #Espera un ciclo entre cada lectura
        time.sleep(1/1000*55)

s.close()
