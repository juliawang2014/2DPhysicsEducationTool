import pygame
import globals
import pymunk

def create_ball(obj, point, mass=10, radius=25) -> None:
    """
    Create a ball.
    :return:
    """
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
    body = pymunk.Body(mass, inertia)
    body.position = point
    shape = pymunk.Circle(body, radius, (0, 0))
    shape.elasticity = 0.95
    shape.friction = 0.9
    globals.space.add(body, shape)
    obj._balls.append(shape)

def create_rectangle(obj, point, size=10, mass=1.0, friction=1):
    points = [(-size, -size), (-size, size), (size, size), (size, -size)]
    moment = pymunk.moment_for_poly(mass, points, (0, 0))
    body = pymunk.Body(mass, moment)
    body.position = point
    shape = pymunk.Poly(body, points)
    shape.friction = 1
    globals.space.add(body, shape)