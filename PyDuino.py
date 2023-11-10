import serial
import time
import threading
import sys


class PyDuino:
 port  = "COM5"
 arduino = serial.Serial(port,9600)
 potVals = ""
 pot1 = 0
 pot2 = 0
 def writeToSerial(self):
     while True:
        self.arduino.write(b'A\n')
        time.sleep(1)
        self.arduino.write(b'B\n')
        time.sleep(1)
 t1 = threading.Thread(target = writeToSerial,)

 def __init__(self, placeholder = ""):
    t1 = threading.Thread(target = self.writeToSerial,)

 def startThread(self):
    self.t1.start()
 
 def printSerial(self):
    while True:
      #print(str(self.arduino.readline(),'utf-8'))
      self.potVals = str(self.arduino.readline(),'utf-8').split(",")
      self.pot1 = int(self.potVals[0])
      self.pot2 = int(self.potVals[1])
      
      print(self.pot2)
      #print(f'Potentiometer 1: {self.pot1},  Potentiometer 2: {self.pot2}')
      sys.stdout.flush()
       



