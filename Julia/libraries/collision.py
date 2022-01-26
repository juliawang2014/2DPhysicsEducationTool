from numpy import double
from pygame import Vector2, sprite


import math

class Collision(sprite):
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def is_colliding(self, other):
        return (self.x == other.x) and (self.y == other.y)
    
    def is_aabb_collision(self, other):
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.x - other.x) * 2) < (self.height + other.height)
        return (x_collision and y_collision)