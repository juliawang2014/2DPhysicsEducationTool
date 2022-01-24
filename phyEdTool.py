import libraries.shapes as shapes
import pygame
import globals

#Set the caption of screen
pygame.display.set_caption('2DPhysicsEducationTool')

#set the color of scene 

circle = shapes.Circle(pygame.Vector2(150,50), 100.0, globals.Red, 2)
circle.angle = 50.0
circle.speed = 300.0
circle.display()

running = True

#game loop here: 

while running:
    #for loop for the event queue
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    globals.screen.fill(globals.background_color)
    circle.move()
    circle.bounce()
    circle.display()
    pygame.display.flip()