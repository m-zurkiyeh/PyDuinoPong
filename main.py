import sys
import serial
import time
import threading
import pygame
from PyDuino import PyDuino

def main():
    #canvas = pygame.display.set_mode((500, 500)) 
    #print(type(sys.argv[1]))
    pyd = PyDuino()
    pyd.startThread()

    #pygame.display.set_caption("My Board") 
    exit = False
  
    # while not exit: 
    #     for event in pygame.event.get(): 
    #         if event.type == pygame.QUIT: 
    #             exit = True
    #     pygame.display.update() 

    pyd.printSerial()
    #pygame.init()

def initGUI():

    pass

if __name__ == '__main__':
    main()