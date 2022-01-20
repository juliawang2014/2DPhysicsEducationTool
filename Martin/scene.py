#import pygame module 
from numpy import true_divide
import pygame

#Background color is rbg color number.
White = (255,255,255)
Red = (255,0,0)
background_color = (White)

#Dimensions of the screen for the scene 
screen = pygame.display.set_mode((1000,600))

#Set the caption of screen
pygame.display.set_caption('2DPhysicsEducationTool')

#set the color of scene 
screen.fill(background_color)

pygame.display.flip()

running = True

#game loop here: 

while running:
    #for loop for the event queue
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False