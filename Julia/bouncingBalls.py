import enum
import random
import libraries.shapes as shapes
import pygame
import globals
import math

#Set the caption of screen
pygame.display.set_caption('2DPhysicsEducationTool')

#set the color of scene 



number_of_circles = 5
circles = []

for n in range(number_of_circles):
    size = random.randint(50,100)
    x = random.randint(size, globals.screen_width-size)
    y = random.randint(size, globals.screen_height-size)

    circle = shapes.Circle(pygame.Vector2(x,y), size, globals.Red, 2)
    circle.angle = random.uniform(0, math.pi*2)
    circle.speed = random.random()*6
    circles.append(circle)

running = True

#game loop here: 

while running:
    #for loop for the event queue
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    globals.screen.fill(globals.background_color)
    for i, c in enumerate(circles):

        c.move()
        c.bounce()
        for c2 in circles[i+1:]:
            shapes.collide(c, c2)
        c.display()

    pygame.display.flip()