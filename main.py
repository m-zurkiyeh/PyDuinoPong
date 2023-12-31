import sys
import serial
import time
import threading
import pygame
from PyDuino import PyDuino

WIDTH,HEIGHT = 800,460
PADDLE_WIDTH,PADDLE_HEIGHT = 10,120
BALL_WIDTH,BALL_HEIGHT = 10,10
WHITE = (255,255,255)
FINAL_SCORE = 9

pygame.font.init()
pygame.mixer.init()



def main():
    guiThread = threading.Thread(target=initGUI)
    pygame.display.set_caption("PyDuino Pong") 
    guiThread.start()
    pyd.readSerial()
    

def initGUI():
    """
    Initializes the application's GUI
    
    """
    
    global p1,p2
    global ball
    global ball_x,ball_y
    global ball_x_speed,ball_y_speed
    global p1_led_on,p2_led_on
    global win_text
    global beep
    global beeep
    global p1_score,p2_score
    
    
    ball_x,ball_y = WIDTH/2,HEIGHT/2
    ball_x_speed,ball_y_speed = 3,3
    
    p1_x,p1_y = 0,0
    p2_x,p2_y = 790,0
    p1_score, p2_score = 0,0
    
    win,exit = False,False
    
    
    score_font = pygame.font.Font("fonts/pong-score.ttf", 48)
    win_font = pygame.font.Font("fonts/EMULOGIC-ZREW.ttf",20)

    beep = pygame.mixer.Sound('sfx/boop.ogg')
    beeep = pygame.mixer.Sound('sfx/beeeep.ogg')
    
    
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    while not exit: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                exit = True
                pyd.writeToSerial(b'a\n')
                pyd.writeToSerial(b'b\n')
                pyd.endThread()
        
        p1_led_on = False
        p2_led_on = False
        
        p1 = pygame.Rect(p1_x,p1_y,PADDLE_WIDTH,PADDLE_HEIGHT)
        p2 = pygame.Rect(p2_x,p2_y,PADDLE_WIDTH,PADDLE_HEIGHT)
        
        ball = pygame.Rect(ball_x,ball_y,10,10) 
        
        if not win :
            ball_x += ball_x_speed      
            ball_y += ball_y_speed          # Move ball and get potentiometer values if neither player has won
            p1_y = pyd.get_pot1() / 3
            p2_y = pyd.get_pot2() / 3
        
        
        check_for_collision()
       
        
        p1_score_text = score_font.render(str(p1_score), True, WHITE) # Score text
        p2_score_text = score_font.render(str(p2_score), True, WHITE)
        

        #Lights up p1 led if score higher than p2
        if(p1_score > p2_score and p1_led_on == True):
            pyd.writeToSerial(b'A\n')
            pyd.writeToSerial(b'b\n')
            p2_led_on = False
        
        #Lights up p2 led if score higher than p1
        if(p2_score > p1_score and p2_led_on == True):
            pyd.writeToSerial(b'B\n')
            pyd.writeToSerial(b'a\n')
            p1_led_on = False
        
        # Change win text depending on which player has won
        if(p1_score == FINAL_SCORE):
            win = True 
            win_text = win_font.render("PLAYER 1 WINS", True, WHITE)
        elif(p2_score == FINAL_SCORE):
            win = True 
            win_text = win_font.render("PLAYER 2 WINS", True, WHITE)
        
        #Fills the screen and repeatedly rewriting the text
        screen.fill((0, 0, 0))
        screen.blit(p1_score_text,(120,40))
        screen.blit(p2_score_text,(680,40))
        
        #Draws the paddles as well as the ball
        pygame.draw.rect(screen,WHITE,p1)
        pygame.draw.rect(screen,WHITE,p2)
        
        
        if win == True:
            screen.blit(win_text,(WIDTH/2 - 150,HEIGHT/2 - 50)) # Only draw ball if game is still going
        else: pygame.draw.rect(screen,WHITE,ball)
        
        pygame.display.update()
        pygame.time.delay(10)
        
    pygame.quit()


def check_for_collision():
    
    """
    Checks if the ball hit the screen borders and/or the paddles
    
    """
    
    global p1,p2
    global ball
    
    global ball_x,ball_y
    global ball_x_speed,ball_y_speed
    
    global p1_led_on,p2_led_on
    
    global win_text
    
    global beep
    global beeep
    
    global p1_score,p2_score
    
    if (ball_y <= 0): 
        ball_y_speed *= -1
        beep.play()
    elif(ball_y >= HEIGHT) :
        ball_y_speed *= -1
        beep.play()
    elif(ball_x <= 0):
        p2_score += 1
        ball_x_speed *= -1
        ball_x,ball_y = WIDTH/2,HEIGHT/2            # * Collision Detection checks
        p2_led_on = True
        beeep.play()
    elif(ball_x >= WIDTH):
        ball_x,ball_y = WIDTH/2,HEIGHT/2
        p1_score += 1
        ball_x_speed *= -1
        p1_led_on = True
        beeep.play()
    elif(p1.colliderect(ball)):
        ball_x_speed = abs(ball_x_speed)
        beep.play()
    elif(p2.colliderect(ball)):
        ball_x_speed = -abs(ball_x_speed)
        beep.play()
    
    
    

if __name__ == '__main__':
    pygame.init()
    pyd = PyDuino()
    main()
