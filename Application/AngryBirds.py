""" A bird can be launched into the air and will stick where they land, the user will be able to see 
how far the bird has traveled and can change the air resistance to see how it effects the bird
and its distance. And can watch it knock over  
"""
from pickle import NONE
import sys
from typing import List

import pygame
import pygame_gui
from pygame_gui.elements import UITextEntryLine
from pygame_gui.elements import UITextBox
from pygame_gui.elements import UIHorizontalSlider

import pymunk
import pymunk.pygame_util
from pymunk.vec2d import Vec2d

import globals

# Library imports

import libraries.shapes as shapes
import libraries.toggleButton as toggleButton
import random

#friction = 1
#elasticity = 0
#mass = 10

class Values:
    def __init__(self, friction=1, elasticity=0, mass=10, shape_selected="Square", shape_being_dragged=None) -> None:
        self._friction = friction
        self._elasticity = elasticity
        self._mass = mass
        self._shape_selected = shape_selected
        self._shape_dragged = shape_being_dragged
    
    def get_friction(self):
        return self._friction
    
    def get_elasticity(self):
        return self._elasticity
    
    def get_mass(self):
        return self._mass
    
    def get_shape(self):
        return self._shape_selected
    
    def get_shape_dragged(self):
        return self._shape_dragged

    def set_friction(self, f):
        self._friction = f
    
    def set_elasticity(self, e):
        self._elasticity = e
    
    def set_mass(self, m):
        self._mass = m
    
    def set_shape(self, s):
        self._shape_selected = s

    def set_shape_dragged(self, s):
        self._shape_dragged = s

values = Values()

pygame.init()
font = pygame.font.SysFont("Arial", 16)

width, height = 1200, 700
manager = pygame_gui.UIManager((width, height), 'themes/GUI_Theme.json')
    
#textboxes and buttons for main gui

#Text 1
text_box = UITextBox(html_text="Gravity",relative_rect=pygame.Rect(50, 17, 100, 35),manager=manager,object_id='textb')

#first text box
gravity_box = UITextEntryLine(relative_rect=pygame.Rect(50,50, 100, 35),manager=manager,object_id='entryb')
gravity_box.set_text("900")

#text 2
text_box = UITextBox(html_text="Mass",relative_rect=pygame.Rect(150, 17, 100, 35),manager=manager,object_id='textb')

#second text box
mass_box = UITextEntryLine(relative_rect=pygame.Rect(150,50, 100, 35),manager=manager,object_id='entryb')
mass_box.set_text("10")
#text 3
text_box = UITextBox(html_text="Elasticity",relative_rect=pygame.Rect(250, 17, 100, 35),manager=manager,object_id='textb')

#third text box
elas_box = UITextEntryLine(relative_rect=pygame.Rect(250,50, 100, 35),manager=manager,object_id='entryb')
elas_box.set_text("0")
#text 4
text_box = UITextBox(html_text="Friction",relative_rect=pygame.Rect(350, 17, 100, 35),manager=manager,object_id='textb')

#fourth text box
friction_box = UITextEntryLine(relative_rect=pygame.Rect(350,50, 100, 35),manager=manager,object_id='entryb')
friction_box.set_text('1')
#text 5
#color_button = pygame_gui.elements.UIButton(text="Color",relative_rect=pygame.Rect(450, 17, 100, 35),manager=manager,object_id='toggleButton')


size_slider_x = UIHorizontalSlider(relative_rect=pygame.Rect((465, 25), (250, 25)), start_value=25, value_range=[1, 100], manager=manager, object_id='button')
size_slider_y = UIHorizontalSlider(relative_rect=pygame.Rect((465, 58), (250, 25)), start_value=25, value_range=[1, 100], manager=manager, object_id='button')

#Shapes buttons
circle_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((725, 15), (75, 75)),text='',manager=manager,object_id='pigButton')
square_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800, 15), (75, 75)),text='',manager=manager,object_id='squareButton')

#Pause Button


#Info Button
#menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1000, 25), (100, 50)),text='Menu',manager=manager,object_id='button')

#NOT DOING ANYTHING YET!!!
toggle_spawn = toggleButton.ToggleButton(rect=pygame.Rect((890,0),(150,45)), text1="Spawn Mode: On", text2="Destroy Mode: On", manager=manager, object_id="toggleButton")
toggle_move = toggleButton.ToggleButton(rect=pygame.Rect((890,50),(150,45)), text1="Move mode: Off", text2="Move mode: On", manager=manager, object_id="toggleButton")

#Info and Quit Buttons
info_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1050, 0), (100, 45)),text='Info',manager=manager,object_id='info')           
quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1050, 50), (100, 45)),text='Quit',manager=manager,object_id='quit')


space = pymunk.Space()
space.gravity = 0, 1400
def update_values():
        try:
            num_grav = float(gravity_box.get_text())
        except:
            grav = ''
        else:
            grav = num_grav

        try:
            num_elas = float(elas_box.get_text())
        except:
            elas = ''
        else:
            elas = num_elas
        
        try:
            num_fric = float(friction_box.get_text())
        except:
            fric = ''
        else:
            fric = num_fric
        
        try:
            num_mass = float(mass_box.get_text())
        except:
            mass = ''
        else:
            mass = num_mass

        if grav == '':
            grav_value = 0.0
        else:
            grav_value = float(grav)
            
        space.gravity = (0.0, grav_value)

        if elas == '':
            values.set_elasticity(0.0)
        else:
            values.set_elasticity(elas)

        if fric == '':
            values.set_friction(0.0)
        else:
            values.set_friction(fric)
        
        if mass == '':
            values.set_mass(1.0)
        else:
            values.set_mass(mass)
        

def create_ball(point, mass=5, radius=20, elasticity=0.95, friction=0.9) -> None:
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
    return body,shape

def create_rectangle(point, size_x=25, size_y=25, mass=5.0, friction=1 , elasticity=0 ):
    points = [(-size_x, -size_y), (-size_x, size_y), (size_x, size_y), (size_x, -size_y)]
    moment = pymunk.moment_for_poly(mass, points, (0, 0))
    body = pymunk.Body(mass, moment)
    body.position = point
    shape = pymunk.Poly(body, points)
    shape.friction = friction
    shape.elasticity = elasticity
    return body, shape

   

  
football_img = pygame.image.load('img/Bird.png')
pig_img = pygame.image.load('img/pig.png')

def create_football():
    vs = [(-30, 0), (0, 3), (10, 0), (0, -3)]
    football_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)

    football_shape = pymunk.Poly(football_body, vs)
    football_shape.friction = 0.5
    football_shape.collision_type = 1
    football_shape.density = 0.08

    
    
    return football_body, football_shape


pivot = []
gear = []

def stick_football_to_target(space, football_body, target_body, position, flying_footballs):
    pivot_joint = pymunk.PivotJoint(football_body, target_body, position)
    
    phase = target_body.angle - football_body.angle
    gear_joint = pymunk.GearJoint(football_body, target_body, phase, 1)
    space.add(pivot_joint)
    space.add(gear_joint)

    pivot.append(pivot_joint)
    gear.append(gear_joint)

    try:
        flying_footballs.remove(football_body)
    except:
        pass


def post_solve_football_hit(arbiter, space, data):
    if arbiter.total_impulse.length > 300:
        a, b = arbiter.shapes
        position = arbiter.contact_point_set.points[0].point_a
        b.collision_type = 0
        b.group = 1
        other_body = a.body
        football_body = b.body
        space.add_post_step_callback(
            stick_football_to_target,
            football_body,
            other_body,
            position,
            data["flying_footballs"],
        )

def on_mouse_motion():
    if values.get_shape_dragged() is not None:
        values.get_shape_dragged().shape.body.position = pygame.mouse.get_pos()
        values.get_shape_dragged().shape.body.velocity = 0, 0
        
def main():
    ### PyGame init
    #pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True
    #font = pygame.font.SysFont("Arial", 16)
    pygame.display.set_caption("2DPhysicsEducationTool- Angry Birds Simulation")
    ### Physics stuff
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    drag_constant = 0.003
    
    # walls - the left-top-right walls
    static: List[pymunk.Shape] = [
        pymunk.Segment(space.static_body, (50, 650), (50, 150), 5),
        pymunk.Segment(space.static_body, (50, 150), (1150, 150), 5),
        pymunk.Segment(space.static_body, (1150, 150), (1150, 650), 5),
        pymunk.Segment(space.static_body, (50, 650), (1150, 650), 5),
    ]
    for line in static:
        line.elasticity = 1
        line.friction = 1
    space.add(*static)
   # manager = pygame_gui.UIManager((width, height))
 
    
   
    # this is where the firing of the football is located
    cannon_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    cannon_shape = pymunk.Circle(cannon_body, 25)
    cannon_shape.sensor = True
    
    cannon_body.position = 50, 500
    

    football_body, football_shape = create_football()
    space.add(football_body, football_shape)

    flying_footballs: List[pymunk.Body] = []
    football_shapes: List[pymunk.Shape] = []
    pigs: List[pymunk.Shape] = []
    football_shapes.append(football_shape)
    handler = space.add_collision_handler(0, 1)
    handler.data["flying_footballs"] = flying_footballs
    
    #Sticking line
    #handler.post_solve = post_solve_football_hit

    reset_b = False
    def reset():
        for x in pivot:
            space.remove(x)
        pivot.clear()
        for x in gear:
            space.remove(x)
        gear.clear()   
        for c in football_shapes:
            space.remove(c)
        football_shapes.clear()
        for p in pigs:
            space.remove(p)
        pigs.clear()

        return False
    
    while running:
        for event in pygame.event.get():
            def createmessage():
                print('test')
                ui_window1 = pygame_gui.windows.UIMessageWindow(html_message='Information about the Experiment',rect=pygame.Rect((400, 150), (300, 300)), manager=manager, object_id="Messagebx")

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_b = True
            if reset_b:
                reset_b = reset()

            if event.type == pygame.MOUSEBUTTONDOWN:
                state = event.button
                if pygame.mouse.get_pos()[1] >= 100 and pygame.mouse.get_pos()[0] <= pygame.display.Info().current_w - 250:
                    size_x = size_slider_x.get_current_value()
                    size_y = size_slider_y.get_current_value()
                    if state == 3 and not toggle_move.get_state():
                        shape_list = space.point_query(pygame.mouse.get_pos(), 1, pymunk.ShapeFilter())
                        values.set_shape_dragged(shape_list[0])
                    elif state == 3 and toggle_spawn.get_state():
                        if values.get_shape() == "Square":
                            body, shape = create_rectangle(pygame.mouse.get_pos(),size_x = size_x, size_y=size_y,mass = values.get_mass(), friction=values.get_friction(), elasticity = values.get_elasticity())
                            space.add(body,shape)
                        elif values.get_shape() == "Circle":
                            body, shape = create_ball(pygame.mouse.get_pos(),mass = values.get_mass(), friction=values.get_friction(), elasticity = values.get_elasticity())
                            pigs.append(shape)
                            space.add(body,shape)
                    elif state == 3 and not toggle_spawn.get_state():
                        shape_list = space.point_query(pygame.mouse.get_pos(), 1, pymunk.ShapeFilter())
                        if len(shape_list) > 0:
                            if not toggle_spawn.get_state():
                                space.remove(shape_list[0].shape)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if toggle_spawn.pressed():
                    toggle_spawn.toggle()
                elif toggle_move.pressed():
                    toggle_move.toggle()
            
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                values.set_shape_dragged(None)
                    
                
            if (
                event.type == pygame.QUIT
                or event.type == pygame.KEYDOWN
                and (event.key in [pygame.K_ESCAPE, pygame.K_q])
            ):
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 560:
                start_time = pygame.time.get_ticks()
                
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and pygame.mouse.get_pos()[1] >= 100:
                end_time = pygame.time.get_ticks()

                diff = end_time - start_time
                power = max(min(diff, 1000), 10) * 13.5
                impulse = power * Vec2d(1, 0)
                impulse = impulse.rotated(football_body.angle)
                football_body.body_type = pymunk.Body.DYNAMIC
                football_body.apply_impulse_at_world_point(impulse, football_body.position)

              
                flying_footballs.append(football_body)

                football_body, football_shape = create_football()
                football_shapes.append(football_shape)
                space.add(football_body, football_shape)

            elif event.type == pygame_gui.UI_BUTTON_PRESSED and circle_button.check_pressed():
                values.set_shape("Circle")
                
            elif event.type == pygame_gui.UI_BUTTON_PRESSED and square_button.check_pressed():
                values.set_shape("Square")

            elif event.type == pygame_gui.UI_BUTTON_PRESSED and info_button.check_pressed():
                createmessage()
            
            elif event.type == pygame_gui.UI_BUTTON_PRESSED and quit_button.check_pressed():
                pygame.quit()
                sys.exit()

            elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                update_values()               

            manager.process_events(event)
        on_mouse_motion()

        mouse_position = pymunk.pygame_util.from_pygame(
            Vec2d(*pygame.mouse.get_pos()), screen

            
        )
        cannon_body.angle = (mouse_position - cannon_body.position).angle
        # move the unfired football
        football_body.position = cannon_body.position + Vec2d(
            cannon_shape.radius + 25, 0
        ).rotated(cannon_body.angle)
        football_body.angle = cannon_body.angle
        #print(football_body.angle)

        for flying_football in flying_footballs:

            pointing_direction = Vec2d(1, 0).rotated(flying_football.angle)
            # print(pointing_direction.angle, flying_football.angle)
            flight_direction = Vec2d(*flying_football.velocity)
            flight_direction, flight_speed = flight_direction.normalized_and_length()

            dot = flight_direction.dot(pointing_direction)
            
            drag_force_magnitude = (
                (1 - abs(dot)) * flight_speed ** 2 * drag_constant * flying_football.mass
            )
            football_tail_position = flying_football.position + Vec2d(-50, 0).rotated(
                flying_football.angle
            )
            flying_football.apply_impulse_at_world_point(
                drag_force_magnitude * -flight_direction, football_tail_position
            )

            flying_football.angular_velocity *= .5

        ### Clear screen
        screen.fill(pygame.Color("skyblue"))

        ### Draw stuff
        space.debug_draw(draw_options)
        
        

        # Power meter
        if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[1] < 560:
            current_time = pygame.time.get_ticks()
            diff = current_time - start_time
            power = max(min(diff, 1000), 10)
            h = power // 2
            pygame.draw.line(screen, pygame.Color("black"), (30, 650), (30, 650 - h), 10)

        # Info and flip screen
        screen.blit(
            font.render(
                "Aim with your mouse, hold down left click until bar is full, let go to launch bird. Right click to interact with building the scene (spawn, destroy, move).",
                True,
                pygame.Color("black"),
            ),
            (50, 100),
        )
        
    
        #pygame.display.flip()

        for f in football_shapes:
            pos_x = int(f.body.position.x)
            pos_y = int(f.body.position.y)
            pygame.draw.circle(screen,(0,0,0),(pos_x,pos_y),27)
            coin_rect = football_img.get_rect(center = (pos_x,pos_y))
            screen.blit(football_img,coin_rect)
        
        for p in pigs:
            pos_x = int(p.body.position.x)
            pos_y = int(p.body.position.y)
            pygame.draw.circle(screen,(0,0,0),(pos_x,pos_y),1)
            coin_rect = pig_img.get_rect(center = (pos_x,pos_y))
            screen.blit(pig_img,coin_rect)
    
        ### Update physics
        fps = 60
        dt = 1.0 / fps
        space.step(dt)

        delta = clock.tick(fps)
        
        #update GUI stuff
        manager.update(delta)
        GUI_background = pygame.image.load('img/4999GUIbackground.png')
        GUI_background = pygame.transform.scale(GUI_background, (1200,100))
        screen.blit(GUI_background, (0,0))
        manager.draw_ui(screen)
        pygame.display.flip()
        

if __name__ == "__main__":
    sys.exit(main())
