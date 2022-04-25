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
Grey = (169,169,169)

#Fonts and color for fonts
font1 = pygame.font.Font("fonts/Xolonium-Bold.ttf", 28)
font2 = pygame.font.Font("fonts/Xolonium-Regular.ttf", 20)

#--------------Start of program----------------------
X = 1000
Y = 600
background_color = (Grey)
#fps variable
clock = pygame.time.Clock()

#Dimensions of the screen for the scene
screen = pygame.display.set_mode((X,Y))

#Load in images here
exit_img = pygame.image.load('img/quit_btn.png').convert_alpha()
blank_img = pygame.image.load('img/blank.png').convert_alpha()
atom_img = pygame.image.load('img/atom.png').convert_alpha()
button1_img = pygame.image.load('img/GravityButton.png').convert_alpha()
button2_img = pygame.image.load('img/PlinkoButton.png').convert_alpha()
button3_img = pygame.image.load('img/Airresistance.png').convert_alpha()
button4_img = pygame.image.load('img/SpringsButton.png').convert_alpha()
button5_img = pygame.image.load('img/FrictionButton.png').convert_alpha()
#button6_img = pygame.image.load('img/button1.png').convert_alpha()
#button7_img = pygame.image.load('img/button1.png').convert_alpha()
button8_img = pygame.image.load('img/AngryBirdsButton.png').convert_alpha()
button9_img = pygame.image.load('img/SandboxButton.png').convert_alpha()
#Set the caption of screen(top left corner words)
pygame.display.set_caption("2DPhysicsEducationTool")
#set the color of scene
screen.fill(background_color)

#information on screen for our program
text1 = font1.render('2D Physics Education Tool', True, White)

#button instances
#start_button = button.Button(100, 200, start_img, 0.45)
exit_button = button.Button(845,525,exit_img, .3)
text2 = font2.render('- Please select which simulation you would like to run -', True, White)
text3 = font2.render('Disclaimer: The units in this program do not represent real world numbers.',True,White)
text4 = font2.render('The numbers and their relation is true. This tool is meant to be used to show ',True,White)
text5 = font2.render('how the modification of values effects objects in physics. ',True,White)
screen.blit(text1,(300,20))
screen.blit(text2,(220,60))
screen.blit(text3,(0,530))
screen.blit(text4,(0,550))
screen.blit(text5,(0,570))
button1 = button.Button(85, 125, button1_img, 0.2)
button2 = button.Button(400, 125, button2_img, 0.2)
button3 = button.Button(715, 125, button3_img, 0.2)
button4 = button.Button(85, 250, button4_img, 0.2)
button5 = button.Button(400, 250, button5_img, 0.2)
#button6 = button.Button(715, 250, button7_img, 0.43)
#button7 = button.Button(85, 375, button7_img, 0.43)
button8 = button.Button(715, 250, button8_img, 0.2)
button9 = button.Button(400, 375, button9_img, 0.2)
atom = button.Button(70,0,atom_img,.3)
atom1 = button.Button(820,0,atom_img,.3)
button1.draw(screen)
button2.draw(screen)
button3.draw(screen)
button4.draw(screen)
button5.draw(screen)
#button6.draw(screen)
#button7.draw(screen)
button8.draw(screen)
button9.draw(screen)
atom.draw(screen)
atom1.draw(screen)




#---------------------------------------------------------------


#-----------where the game runs!-----------------------------
running = True
#game loop here:

while running:
    clock.tick(60)



    if button1.draw(screen) == True:
        os.system('python gravityGUI.py')
    if button2.draw(screen) == True:
        os.system('python Plinko.py')
    if button3.draw(screen) == True:
        os.system('python AirResGUI.py')
    if button4.draw(screen) == True:
        os.system('python Spring.py')
    if button5.draw(screen) == True:
        os.system('python friction.py')
    if button8.draw(screen) == True:
        os.system('python AngryBirds.py')
    if button9.draw(screen) == True:
        os.system('python sandbox.py')

    if exit_button.draw(screen) == True:
        running = False

    #for loop for the event queue
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False


        pygame.display.update()
