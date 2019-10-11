import serial 
import time
import numpy as np

s = serial.Serial('COM5')

s.is_open

while 1:
  data = s.read()           # Wait forever for anything
  print(data.decode(7))
  time.sleep(1)              # Sleep (or inWaiting() doesn't give the correct value)
  #data_left = s.inWaiting()  # Get the number of characters ready to be read
  #tdata += s.read(data_left) # Do the read and combine it with the first character

s.close()
