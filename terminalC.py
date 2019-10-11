import serial 
import time
import numpy as np

s = serial.Serial('COM7')

s.is_open

while 1:
  data = s.read_until(size=7)           # Wait forever for anything
  try:
    dataS = data.decode()
    print(dataS)
    source = dataS[:2]
    if source == "TA":
      nSec = dataS[3:]
      resp = "TC: " + nSec
      s.write(resp.encode())
      s.write(b'\n')
      print("ack = "+ resp)
  except:
    print("Colision")
  
  time.sleep(1/1000*55)       
s.close()
