import serial
import time
import threading
import sys


class PyDuino:
 port = "COM5"
 potVals = ""
 pot1, pot2 = 0, 0
 def writeToSerial(self):
     while True:
        self.arduino.write(b'A\n')
        time.sleep(1)
        self.arduino.write(b'B\n')
        time.sleep(1)
        self.arduino.write(b'a\n')
        time.sleep(1)
        self.arduino.write(b'b\n')
        time.sleep(1)
      

 def __init__(self):
    self.arduino = serial.Serial(self.port,9600)
    self.t1 = threading.Thread(target = self.writeToSerial,)

 def startThread(self):
    self.t1.start()
    pass
    
   
 def printSerial(self):
    
    while True:
      #print(str(self.arduino.readline(),'utf-8'))
      potVals = str(self.arduino.readline(),'utf-8').split(",")
      self.pot1 = int(potVals[0])
      self.pot2 = int(potVals[1])
      
      # print(self.pot2)
      print(f'Potentiometer 1: {self.pot1},  Potentiometer 2: {self.pot2}')
      sys.stdout.flush()
       



