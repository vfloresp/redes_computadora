import serial 
import time
import numpy as np

s = serial.Serial('COM5')

s.is_open

while 1:
  data = s.read_unitl(size=7)           # Wait forever for anything
  print(data.decode())
  time.sleep(1/1000*55)              # Sleep (or inWaiting() doesn't give the correct value)
  #data_left = s.inWaiting()  # Get the number of characters ready to be read
  #tdata += s.read(data_left) # Do the read and combine it with the first character

s.close()
