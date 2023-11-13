# ﻿PyDuino Pong
A clone of Pong programmed in Python using Pygame

![](https://github.com/m-zurkiyeh/PyDuinoPong/blob/main/imgs/Ingenious%20Snaget.png)

### Installation
1. Install the ArduinoThreads Library by Ivan Seide
1. Set the python interpreter to 3.7.0 for pygame to work
1. Have an arduino with the following components:
    - 2 potentiometers
    - 2 led colors of your choice
    - 2 220 Ω Resistors
    - plenty of wires
1. Connect player 1 potentiometer into the A0 Port and player 2 potentiometer into the A1 Port (Port locations may vary board to board)
1. Connect player 1 led into the 16 digital port and the player 2 led into the 17 digital port
1. Open the arduino sketch "ArduinoPotentiometerController"
 




```
import threading
import pygame
from PyDuino import PyDuino
```
