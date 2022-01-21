#import pygame module 
from numpy import true_divide
import pygame
import button
pygame.init()

#preset colors
White = (255,255,255)
Red = (255,0,0)
Blue = (202, 228, 241)
Black = (0,0,0)
Purple = (100, 20, 140)

#Fonts and color for fonts
font1 = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 24)
font2 = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 16)

#--------------Start of program----------------------
X = 1000
Y = 600
background_color = (Blue)
#fps variable
clock = pygame.time.Clock()
#Dimensions of the screen for the scene 
screen = pygame.display.set_mode((X,Y))
#Load in images here
start_img = pygame.image.load('img/start_btn.png').convert_alpha()
exit_img = pygame.image.load('img/quit_btn.jpg').convert_alpha()
blank_img = pygame.image.load('img/blank.png').convert_alpha()

#Set the caption of screen(top left corner words)
pygame.display.set_caption('2DPhysicsEducationTool')
#set the color of scene 
screen.fill(background_color)

#information on screen for our program
text1 = font1.render('2D Physics Education Tool', True, Black)

#button instances
start_button = button.Button(100, 200, start_img, 0.45)
exit_button = button.Button(550, 200, exit_img, 0.35)


#---------------------------------------------------------------

#----------Screen after start button!------------------------
def physics_selector():
    
    print('physics selector')
    text2 = font2.render('Please select which simulation you would like to run :)', True, White)
    X = 1000
    Y = 600
    screen = pygame.display.set_mode((X,Y))
    pygame.display.set_caption("Select Physics Simulation")

    #new background color
    screen.fill(pygame.Color(Purple))

    screen.blit(text2,(300,60))
    
    pygame.display.flip()
    
#--------------------------------------------------------------


#-----------where the game runs!-----------------------------
running = True
#game loop here: 

while running:
    clock.tick(60)

    screen.blit(text1,(350,20))

    if start_button.draw(screen) == True:
        print("Start")
        start_button = button.Button(0, 0, blank_img, .000001)
        exit_button = button.Button(835,500,exit_img, .2)
        physics_selector()

    


    if exit_button.draw(screen) == True:
        running = False
    #for loop for the event queue
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False
        

        pygame.display.update()