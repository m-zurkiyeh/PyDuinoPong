import serial
import threading
import sys


class PyDuino:
 """
 Primary Class for handling Arduino Related events
 """
 port = "COM5"
 potVals = ""
 
 #
 def writeToSerial(self, signal:bytes):
      """
      Writes a signal to the Arduino Serial
      """
      self.arduino.write(signal)

      
      
 def __init__(self):
    """
    Default Constructor for the PyDuino Class
    """
    
    self.arduino = serial.Serial(self.port,9600) 
    self.t1 = threading.Thread(target = self.writeToSerial)
    self.t1.daemon = True
    self.exit_flag = False                                  # * DO NOT ALTER 
    self.pot1 = 0
    self.pot2 = 0


   
 def endThread(self): 
    """
    * Ends thread responsible for reading from serial
    """
    self.exit_flag = True

 def readSerial(self):
    """
    * Reads the numbers outputted from Arduino Serial and Converts the output into 2 int variables for the paddle's movements
    """
    while not self.exit_flag:
      potVals = str(self.arduino.readline(),'utf-8').split(",") # Converts the Arduino's Serial Output into a list
      
      self.pot1 = int(potVals[0]) # The list is then indexed and parsed into values that will be used to move the paddles
      self.pot2 = int(potVals[1])
      
      sys.stdout.flush() # * Cleans internal buffer

 
 def get_pot1(self) -> int:
    """
    Returns pot1

    Returns:
        int: player 1 potentiometer value
    """
    return self.pot1 
 
 
 def get_pot2(self) -> int:
    """
    Returns pot2

    Returns:
        int: player 2 potentiometer value
    """
    return self.pot2
    
       



