import itertools
import random
import libraries.shapes as shapes
import pygame
import globals
import math

#Set the caption of screen
pygame.display.set_caption('2DPhysicsEducationTool')

number_of_rects = 3
rects = []

for n in range(number_of_rects):
    size_w = random.randint(50, 100)
    size_h = random.randint(50,100)
    biggest = (max(size_w, size_h))
    x = random.randint(biggest, globals.screen_width-biggest)
    y = random.randint(biggest, globals.screen_height-biggest)

    r = shapes.Rectangle(pygame.Vector2(x,y), size_w, size_h, globals.Red, 3)
    r.angle = random.uniform(0, math.pi*2)
    r.speed = random.random()*6
    rects.append(r)

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

object_list = circles + rects
running = True

#game loop here: 

while running:
    #for loop for the event queue
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    globals.screen.fill(globals.background_color)
    for i, object in enumerate(object_list):
        object.move()
        object.bounce()
        for object2 in object_list[i+1:]:
            shapes.collide(object, object2)
        object.display()

    pygame.display.flip()