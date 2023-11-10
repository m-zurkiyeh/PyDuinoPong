import serial
import time
import threading
from PyDuino import PyDuino

def main():
    pyd = PyDuino()
    pyd.startThread()
    pyd.printSerial()

if __name__ == '__main__':
    main()