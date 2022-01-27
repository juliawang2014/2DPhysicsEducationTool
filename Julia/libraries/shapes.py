from turtle import Screen, width
from numpy import double
import pygame
import globals
import math

drag = 0.3
elasticity = 0.75
gravity = pygame.Vector2(math.pi, -0.009)

def addVectors(vectorA: pygame.Vector2, vectorB: pygame.Vector2):
    x = math.sin(vectorA.x) * vectorA.y + math.sin(vectorB.x) * vectorB.y
    y = math.cos(vectorA.x) * vectorA.y + math.cos(vectorB.x) * vectorB.y

    angle = 0.5 * math.pi - math.atan2(y, x)
    length = math.hypot(x, y)

    return (angle, length)

def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y

    dist = math.hypot(dx, dy)
    if (dist < p1.size_w + p2.size_w) or (dist < p1.size_h + p2.size_h):
        tangent = math.atan2(dy, dx)

        p1.angle = 2*tangent - p1.angle
        p2.angle = 2*tangent - p2.angle

        (p1.speed, p2.speed) = (p2.speed, p1.speed)
        p1.speed *= elasticity
        p2.speed *= elasticity

        angle = 0.5 * math.pi + tangent

        p1.x += math.sin(angle)
        p1.y -= math.cos(angle)
        p2.x -= math.sin(angle)
        p2.y += math.cos(angle)

class Circle:
    def __init__(self, position: pygame.Vector2, size: double, color, thickness: int):
        self.x, self.y = position
        self.size_w = size
        self.size_h = size
        self.size = size
        self.color = color
        self.thickness = thickness
        self.speed = 0
        self.angle = 0
    
    def display(self):
        pygame.draw.circle(globals.screen, self.color, (self.x, self.y), self.size, self.thickness)

    def move(self):
        (self.angle, self.speed) = addVectors(pygame.Vector2(self.angle, self.speed), gravity)
        self.x += math.sin(self.angle) * self.speed
        self.y += math.cos(self.angle) * self.speed
    
    def bounce(self):
        w = globals.screen_width
        h = globals.screen_height
        if self.x > (w - self.size):
            self.x = 2 * (w - self.size) - self.x
            self.angle = -self.angle
            self.speed *= elasticity
        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle = -self.angle
            self.speed *= elasticity
        
        if self.y > (h - self.size):
            self.y = 2 * (h - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity
        
        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

class Rectangle:
    def __init__(self, position: pygame.Vector2, size_w: double, size_h: double, color, thickness: int):
        self.x, self.y = position
        self.size_w = size_w
        self.size_h = size_h
        self.color = color
        self.thickness = thickness
        self.speed = 0
        self.angle = 0
    
    def display(self):
        pygame.draw.rect(globals.screen, self.color, pygame.Rect(self.x, self.y, self.size_w, self.size_h), self.thickness)
    
    def move(self):
        (self.angle, self.speed) = addVectors(pygame.Vector2(self.angle, self.speed), gravity)
    
    def bounce(self):
        pass