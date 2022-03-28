import pygame
import globals
import pymunk

def create_ball(obj, point, mass=10, radius=25, elasticity=0.95, friction=0.9, color=pygame.Color("Black")) -> None:
    """
    Create a ball.
    :return:
    """
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
    body = pymunk.Body(mass, inertia)
    body.position = point
    shape = pymunk.Circle(body, radius, (0, 0))
    shape.elasticity = elasticity
    shape.friction = friction
    shape.color = color
    globals.space.add(body, shape)
    obj._balls.append(shape)

def create_rectangle(obj, point, size_x=10, size_y=10, mass=1.0, friction=1, elasticity=0.95, color=pygame.Color("Black")):
    points = [(-size_x, -size_y), (-size_x, size_y), (size_x, size_y), (size_x, -size_y)]
    moment = pymunk.moment_for_poly(mass, points, (0, 0))
    body = pymunk.Body(mass, moment)
    body.position = point
    shape = pymunk.Poly(body, points)
    shape.elasticity = elasticity
    shape.friction = friction
    shape.color = color
    globals.space.add(body, shape)
    obj._rects.append(shape)

def create_triangle (obj, point, size_x=20, size_y=20, mass=1.0, friction=1, elasticity=0.95, color=pygame.Color("Black")):
    points = [(-size_x, -size_y), (size_x, -size_y), (0,size_x)]
    moment = pymunk.moment_for_poly(mass, points, (0,0))
    body = pymunk.Body(mass, moment)
    body.position = point
    shape = pymunk.Poly(body, points)
    shape.elasticity = elasticity
    shape.friction = friction
    shape.color = color
    globals.space.add(body, shape)
    obj._rects.append(shape)

def create_line(obj, point_a, point_b, thickness=5, mass=1.0, friction=1, elasticity=0.95, color=pygame.Color("Black")):
    moment = pymunk.moment_for_segment(mass, point_a, point_b, thickness)
    body = pymunk.Body(mass, moment)
    shape = pymunk.Segment(body, point_a, point_b, thickness)
    shape.elasticity = elasticity
    shape.friction = friction
    shape.color = color
    globals.space.add(body, shape)
    obj._rects.append(shape)

def create_static_rect(point, size_x=10, size_y=10, color=pygame.Color("Black")):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = point
    r = pymunk.Poly.create_box(body, (size_x, size_y))
    r.color = color
    globals.space.add(body, r)

def create_static_circle(point, radius=25, color=pygame.Color("Black")):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = point
    c = pymunk.Circle(body, radius)
    c.color = color
    globals.space.add(body, c)

def create_static_triangle(point, size_x=20, size_y=20, color=pygame.Color("Black")):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = point
    space = globals.space
    t = pymunk.Poly(body, [(-size_x, -size_y), (size_x, -size_y), (0,size_x)])
    t.color = color
    space.add(body, t)

def create_static_line(point_a, point_b, thickness=5, color=pygame.Color("Black")):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    l = pymunk.Segment(body, point_a, point_b, thickness)
    l.color = color
    globals.space.add(body, l)