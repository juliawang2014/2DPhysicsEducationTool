from turtle import circle
import pygame
import pymunk
import pymunk.pygame_util

import sys
sys.path.append('Julia')
import globals

space = globals.space

class create_spring:
    b0 = space.static_body
    p0 = 100, 200

    body = pymunk.Body(mass=1, moment=10)
    body.position = (100, 50)
    circle = pymunk.Circle(body, radius=30)

    joint = pymunk.constraints.DampedSpring(b0, body, p0, (20, 0), 100, 50, 1)
    space.add(body, joint)

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 240))
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.image.save(self.screen, 'shape.png')

            self.screen.fill((220, 220, 220))
            space.debug_draw(self.draw_options)
            pygame.display.update()
            space.step(0.01)

        pygame.quit()

App().run()