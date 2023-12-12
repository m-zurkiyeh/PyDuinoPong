# ﻿PyDuino Pong
![Static Badge](https://img.shields.io/badge/python-3.7-blue) ![Static Badge](https://img.shields.io/badge/arduino-green)


A clone of Pong programmed in Python using Pygame that also utilizes arduino via the `serial` class that is imported in PyDuino.py 



![](/imgs/Ingenious%20Snaget.png)

### Prerequisites
- Python (3.7.0)
- A text editor such as VSCode or an IDE such as PyCharm
- Pygame
- Arduino 

## Installation
1. Install Pygame using the terminal command ```pip install pygame```
1. Install the ArduinoThreads Library by Ivan Seide
1. Set the python interpreter to 3.7.0 for pygame to work
1. Have an arduino with the following components:
    - 2 potentiometers
    - 2 led colors of your choice
    - 2 220 Ω Resistors
    - plenty of wires
1. Connect player 1 potentiometer into the A0 Port and player 2 potentiometer into the A1 Port (Port locations may vary board to board)
1. Connect player 1 led into the 16 digital port and the player 2 led into the 17 digital port
1. Open the arduino sketch "ArduinoPotentiometerController", Making sure that the arduino is properly plugged in

**NOTE: The project was built with the arduino port being in COM5, the Port the arduino is connecting to will vary person to person, computer to computer**
If this is the case for you: then you can change the variable `port = "COM5"` located in the PyDuino.py file to the correct value. 

**Please keep in mind to leave the 9600 value as is in** `self.arduino = serial.Serial(self.port,9600)` **as the value represents the baud rate necessary for the program to communicate with the arduino board**

## How to Run
Make sure the arduino code is verified and successfully uploaded to the board and Just run `python3 main.py` on a terminal

## Features
1. Using the arduino potentiometers to move the paddles
    - The program gets a hold of the values by reading the serial output coming from the arduino in which its uploaded sketch contains this code:
   ```
     Serial.print(pot1Val);
     Serial.print(",");
     Serial.print(pot2Val);
     Serial.println();
     delay(50);
   ```
   - The PyDuino class then gets the output and using the correct encode, the serial values are then converted into a list by splitting the comma in between the values and converted into a string using
   `potVals = str(self.arduino.readline(),'utf-8').split(",")`
   - Finally, the program selects the values from the list, parses them in to an int value and assigning them to variables `self.pot1` and `self.pot2` respectively using
     ```
     self.pot1 = int(potVals[0])
     self.pot2 = int(potVals[1])
     ```
    
       
 2. LED Indicators
    - The program also utilizes the connected leds to blink depending on which player has the advantage.
         - The arduino code awaits input to serial from the python side and depending on the signal, it will enable/disable the led threads accordingly:

              ```
              Arduino Code
              
              if (Serial.available() > 0) {
              data = Serial.readStringUntil('\n');
              if (data.equals("A")) p1LED.enabled = true;
              else if (data.equals("a")) p1LED.enabled = false;
              else if (data.equals("B")) p2LED.enabled = true;
              else if (data.equals("b")) p2LED.enabled = false;
              p1LED.run();
              p2LED.run();
              Serial.flush();
              }
              ```

              ```
              Python Code
              
              def writeToSerial(self, signal:bytes):
              self.arduino.write(signal)
              ```
              
           

***
NOTE: Keep in mind that to ensure the program runs very well its best to reupload the code or open the sketch, open the serial monitor and then close it.
Another Note is that you must not have the serial monitor opened on arduino or the program will not run
***


