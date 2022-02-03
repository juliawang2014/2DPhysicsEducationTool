from numpy import double
import pygame
import globals
import math
import pymunk as pm
import pymunk.util as u
from pymunk import Vec2d

COLLTYPE_DEFAULT = 0
COLLTYPE_MOUSE = 1

class Shape:
    def flipyv(self, v):
        return int(v.x), int(-v.y + self.h)

    def __init__(self):
        self.shape_to_remove = None
        self.mouse_contact = None
    
    def create_ball(self, point, mass=1.0, radius=15.0, elasticity=0.95, friction=0.9):
        moment = pm.moment_for_circle(mass, 0.0, radius)
        ball_body = pm.Body(mass, moment)
        ball_body.position = Vec2d(*point)

        ball_shape = pm.Circle(ball_body, radius)
        ball_shape.elasticity = elasticity
        ball_shape.friction = friction
        ball_shape.collision_type = COLLTYPE_DEFAULT
        #self.space.add(ball_body, ball_shape)
        return ball_body, ball_shape
    
    def create_box(self, pos, size=10, mass=5.0):
        box_points = [(-size, -size), (-size, size), (size, size), (size, -size)]
        return self.create_poly(box_points, mass=mass, pos=pos)
    
    def create_poly(self, points, mass=5.0, pos=(0, 0)):
        moment = pm.moment_for_poly(mass, points)

        body = pm.Body(mass, moment)
        body.position = Vec2d(*pos)
        shape = pm.Poly(body, points)
        shape.friction = 0.5
        shape.collision_type = COLLTYPE_DEFAULT
        self.space.add(body, shape)
        return shape
    
    def draw_ball(self, ball):
        body = ball.body
        v = body.position + ball.offset.cpvrotate(body.rotation_vector)
        p = self.flipyv(v)
        r = ball.radius
        pygame.draw.circle(globals.screen, pygame.Color("Blue"), p, int(r), 2)
    
    def draw_poly(self, poly):
        body = poly.body
        ps = [p.rotated(body.angle) + body.position for p in poly.get_vertices()]
        ps.append(ps[0])
        ps = list(map(self.flipyv, ps))
        if u.is_clockwise(ps):
            color = pygame.Color("green")
        else:
            color = pygame.Color("red")
        pygame.draw.lines(globals.screen, color, False, ps)
    