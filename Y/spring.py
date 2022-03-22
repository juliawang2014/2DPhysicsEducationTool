from vpython import *

def acc():
    dr_right = ball.pos - wall_right.pos
    force_right = -spring_right.constant*(mag(dr_right) - length)*norm(dr_right)
    
    dr_left = ball.pos - wall_left.pos
    force_left = -spring_left.constant*(mag(dr_left) - length)*norm(dr_left)
    
    return (force_right+force_left) / ball.mass

def change_radius(widget):
    print('radius:', widget.value)
    ball.radius = widget.value 

def change_massball(widget):
    print('massball:', widget.value)
    ball.mass = widget.value 

# --- main ---

length = 30.
fric = 0.01
massball = 1
mass = massball
radius = 2.5

scene2 = canvas(title='Masa con dos sistemas', width=400, height=200, center=vector(0,0,0), background=color.white) 

ball = sphere(pos=vector(2,0,0), velocity=vector(0,0,0), radius=radius, mass=massball, color=color.blue)

wall_right = box(pos=vector(length,0,0), size=vector(0.2, 5, 5), color=color.green)
wall_left = box(pos=vector(-length,0,0), size=vector(0.2, 5, 5), color=color.green)

spring_right = helix(pos=wall_right.pos, axis=ball.pos-wall_right.pos, constant=1, coils=10, thickness=0.2, radius=1, color=color.red)
spring_left = helix(pos=wall_left.pos, axis=ball.pos-wall_left.pos, constant=1, coils=10, thickness=0.2, radius=1, color=color.red)

scene2.caption = "Variación de la masa: Variación del radio:"

sl1 = slider(min=0.3, max=10, value=massball, length=220, bind=change_massball, right=15)
sl2 = slider(min=0.3, max=10, value=radius,   length=220, bind=change_radius,   right=15)


ball.trail = curve(color=ball.color)

t = 0
dt = 0.01

while t < 100:
    rate(500)
    ball.velocity = ball.velocity + acc() * dt
    ball.pos = ball.pos + ball.velocity * dt
    spring_right.axis = ball.pos - wall_right.pos
    spring_left.axis = ball.pos - wall_left.pos
    ball.trail.append(pos=ball.pos)
    t = t + dt