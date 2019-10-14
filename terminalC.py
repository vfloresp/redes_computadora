import serial 
import time
import numpy as np

s = serial.Serial('COM7')

s.is_open

#Se mantiene en un ciclo escuchando 
while 1:
  data = s.read_until(size=7)           
  try:
    dataS = data.decode()
    if len(dataS>4):
      source = dataS[:3]
      val = dataS[3:]
      print(dataS)
      if(source!="TA:" and source!="TB:"):
        print("Colision")
      #Si recibe trama de A, entonces envia un ack
      elif source == "TA:":
        resp = "TC: " + val
        s.write(resp.encode()+b'\n')
        print("ack = "+ resp)
  except:
    print("Colision")
  
  time.sleep(1/1000*55)       
s.close()

