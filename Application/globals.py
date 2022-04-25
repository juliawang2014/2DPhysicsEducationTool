import pygame
import pymunk

#Background color is rbg color number.
White = (255,255,255)
Red = (255,0,0)
background_color = (White)

space = pymunk.Space()
gravity = (0.0, 900.0)

clock = pygame.time.Clock()

#Dimensions of the screen for the scene 
screen_width = 1000
screen_height = 600

#screen = pygame.display.set_mode((screen_width,screen_height))