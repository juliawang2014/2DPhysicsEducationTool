#import pygame module 
from numpy import true_divide
import pygame
import button
import os
pygame.init()

#preset colors
White = (255,255,255)
Red = (255,0,0)
Blue = (202, 228, 241)
Black = (0,0,0)
Purple = (100, 20, 140)

#Fonts and color for fonts
font1 = pygame.font.Font("fonts/arial.ttf", 24)
font2 = pygame.font.Font("fonts/arial.ttf", 16)

#--------------Start of program----------------------
X = 1000
Y = 600
background_color = (Purple)
#fps variable
clock = pygame.time.Clock()

#Dimensions of the screen for the scene 
screen = pygame.display.set_mode((X,Y))

#Load in images here
exit_img = pygame.image.load('img/quit_btn.jpg').convert_alpha()
blank_img = pygame.image.load('img/blank.png').convert_alpha()
button1_img = pygame.image.load('img/button1.jpg').convert_alpha()
button2_img = pygame.image.load('img/button2.jpg').convert_alpha()
button3_img = pygame.image.load('img/button3.jpg').convert_alpha()
button4_img = pygame.image.load('img/button4.jpg').convert_alpha()
button5_img = pygame.image.load('img/button5.jpg').convert_alpha()
#Set the caption of screen(top left corner words)
pygame.display.set_caption('2DPhysicsEducationTool')
#set the color of scene 
screen.fill(background_color)

#information on screen for our program
text1 = font1.render('2D Physics Education Tool', True, Black)

#button instances
#start_button = button.Button(100, 200, start_img, 0.45)
exit_button = button.Button(835,500,exit_img, .2)
text2 = font2.render('Please select which simulation you would like to run :)', True, White)

screen.blit(text2,(300,60))
button1 = button.Button(50, 100, button1_img, 0.45)
button2 = button.Button(375, 100, button2_img, 0.45)
button3 = button.Button(700, 100, button3_img, 0.45)
button4 = button.Button(200, 300, button4_img, 0.45)
button5 = button.Button(550, 300, button5_img, 0.45)

button1.draw(screen)
button2.draw(screen)
button3.draw(screen)
button4.draw(screen)
button5.draw(screen)

def gravity_window():
    pygame.init()
    pygame.display.set_caption('Gravity')
    pygame.display.set_mode((X,Y))
    

#---------------------------------------------------------------


#-----------where the game runs!-----------------------------
running = True
#game loop here: 

while running:
    clock.tick(60)

    screen.blit(text1,(350,20))

    if button1.draw(screen) == True:
        print("Button 1 clicked")
        os.system('phyEdTool.py')
        gravity_window()
       
        
        
       

    if button2.draw(screen) == True:
        print("Button 2 clicked")

    if button3.draw(screen) == True:
        print("Button 3 clicked")

    if button4.draw(screen) == True:
        print("Button 4 clicked")

    if button5.draw(screen) == True:
        print("Button 5 clicked")

    if exit_button.draw(screen) == True:
        running = False
        
    #for loop for the event queue
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False
        

        pygame.display.update()