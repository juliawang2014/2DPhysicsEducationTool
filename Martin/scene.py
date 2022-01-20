#import pygame module 
from numpy import true_divide
import pygame
pygame.init()


X = 1000
Y = 600
#Background color is rbg color number.
White = (255,255,255)
Red = (255,0,0)
background_color = (White)

#fps variable
clock = pygame.time.Clock()

#Dimensions of the screen for the scene 
screen = pygame.display.set_mode((X,Y))

#Set the caption of screen
pygame.display.set_caption('2DPhysicsEducationTool')

#set the color of scene 
screen.fill(background_color)

pygame.display.flip()

#information for font on the screen:
font1 = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 24)
font1Color = (0,150,250)
text1 = font1.render('2D Physics Education Tool', True, font1Color)



running = True

#game loop here: 

while running:
    clock.tick(60)

    screen.blit(text1,(350,20))


    #for loop for the event queue
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False
        

        pygame.display.update()