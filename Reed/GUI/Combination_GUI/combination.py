"""Football can be launched into the air and will stick where they land, the user will be able to see 
how far the football has traveled and can change the air resistance to see how it effects the football 
and its distance. 
"""
import sys

# #Reed Code

import pygame_gui
from pygame_gui.elements import UITextEntryLine
from pygame_gui.elements import UITextBox
from pygame_gui.core import ObjectID
from pygame_gui import UIManager
# Reed Code

from typing import List

import pygame
import pygame_gui
import pymunk
import pymunk.pygame_util
from pymunk.vec2d import Vec2d



def create_football():
    vs = [(-30, 0), (0, 3), (10, 0), (0, -3)]
    football_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)

    football_shape = pymunk.Poly(football_body, vs)
    football_shape.friction = 0.5
    football_shape.collision_type = 1
    football_shape.density = 0.1

    
    
    return football_body, football_shape


def stick_football_to_target(space, football_body, target_body, position, flying_footballs):
    pivot_joint = pymunk.PivotJoint(football_body, target_body, position)
    phase = target_body.angle - football_body.angle
    gear_joint = pymunk.GearJoint(football_body, target_body, phase, 1)
    space.add(pivot_joint)
    space.add(gear_joint)
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

width, height = 1200, 700

def main():
    ### PyGame init
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.SysFont("Arial", 16)

    ### Reed Code -------------------------------
    backcolor = pygame.Surface((1200,100))
    guimanager = pygame_gui.UIManager((1200,200),'Reed/GUI/Martin AirRes Combination/GUI_theme.json')

    #textboxes and buttons for main gui
    backcolor.fill(pygame.Color('#1d1135'))
    pygame.display.set_caption('Physics Tutorial')
    
    #Text 1
    text_box = UITextBox(html_text="Text1",relative_rect=pygame.Rect(50, 17, 100, 35),manager=guimanager,object_id='textb')

    #first text box
    text_box = UITextEntryLine(relative_rect=pygame.Rect(50,50, 100, 35),manager=guimanager,object_id='entryb')

    #text 2
    text_box = UITextBox(html_text="Text2",relative_rect=pygame.Rect(150, 17, 100, 35),manager=guimanager,object_id='textb')

    #second text box
    text_box2 = UITextEntryLine(relative_rect=pygame.Rect(150,50, 100, 35),manager=guimanager,object_id='entryb')

    #text 3
    text_box = UITextBox(html_text="Text3",relative_rect=pygame.Rect(250, 17, 100, 35),manager=guimanager,object_id='textb')

    #third text box
    text_box3 = UITextEntryLine(relative_rect=pygame.Rect(250,50, 100, 35),manager=guimanager,object_id='entryb')

    #text 4
    text_box = UITextBox(html_text="Text4",relative_rect=pygame.Rect(350, 17, 100, 35),manager=guimanager,object_id='textb')

    #fourth text box
    text_box4 = UITextEntryLine(relative_rect=pygame.Rect(350,50, 100, 35),manager=guimanager,object_id='entryb')

    #text 5
    text_box = UITextBox(html_text="Text5",relative_rect=pygame.Rect(450, 17, 100, 35),manager=guimanager,object_id='textb')

    #second text box
    text_box5 = UITextEntryLine(relative_rect=pygame.Rect(450,50, 100, 35),manager=guimanager,object_id='entryb')

    #Menu Button
    menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((900, 25), (100, 50)),text='Pause',manager=guimanager,object_id='button')

    #Info Button
    info_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1000, 25), (100, 50)),text='Menu',manager=guimanager,object_id='button')
    
    ### Reed Code -----------------------------------------------------------

    ### Physics stuff
    space = pymunk.Space()
    space.gravity = 0, 1000
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    drag_constant = 0.0002
    
    # walls - the left-top-right walls
    static: List[pymunk.Shape] = [
        pymunk.Segment(space.static_body, (50, 550), (50, 50), 5),
        pymunk.Segment(space.static_body, (50, 50), (1150, 50), 5),
        pymunk.Segment(space.static_body, (1150, 50), (1150, 550), 5),
        pymunk.Segment(space.static_body, (50, 550), (1150, 550), 5),
    ]

    space.add(*static)
    manager = pygame_gui.UIManager((width, height))
    slider = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(relative_rect=pygame.Rect((600, 25), (250, 50)), start_value=.0002, value_range = (0,.002), manager=guimanager)
    
   # ui_slider = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(relative_rect=pygame.Rect((80, 500), (250, 50)), start_value=25, value_range=(1, 100), manager=manager)
    # this is where the firing of the football is located
    cannon_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    cannon_shape = pymunk.Circle(cannon_body, 25)
    cannon_shape.sensor = True
    
    cannon_body.position = 50, 550
    

    football_body, football_shape = create_football()
    space.add(football_body, football_shape)

    flying_footballs: List[pymunk.Body] = []
    handler = space.add_collision_handler(0, 1)
    handler.data["flying_footballs"] = flying_footballs
    handler.post_solve = post_solve_football_hit

    while running:

        for event in pygame.event.get():
            guimanager.process_events(event)
            if (
                event.type == pygame.QUIT
                or event.type == pygame.KEYDOWN
                and (event.key in [pygame.K_ESCAPE, pygame.K_q])
            ):
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] < 560:
                start_time = pygame.time.get_ticks()
            
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and event.pos[1] < 560:
                end_time = pygame.time.get_ticks()

                diff = end_time - start_time
                power = max(min(diff, 1000), 10) * 13.5
                impulse = power * Vec2d(1, 0)
                impulse = impulse.rotated(football_body.angle)
                football_body.body_type = pymunk.Body.DYNAMIC
                football_body.apply_impulse_at_world_point(impulse, football_body.position)

              
                flying_footballs.append(football_body)

                football_body, football_shape = create_football()
                space.add(football_body, football_shape)
                
            elif event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                print(event.value)
                drag_constant = event.value
            manager.process_events(event)


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
            pygame.draw.line(screen, pygame.Color("pink"), (30, 550), (30, 550 - h), 10)

        # Info and flip screen
        screen.blit(
            font.render(
                "Aim with mouse, hold left click to powerup, release to fire",
                True,
                pygame.Color("black"),
            ),
            (5, 0),
        )
        screen.blit(font.render("10",True,pygame.Color("black"),),(210,560),)
        screen.blit(font.render("20",True,pygame.Color("black"),),(310,560),)
        screen.blit(font.render("30",True,pygame.Color("black"),),(410,560),)
        screen.blit(font.render("40",True,pygame.Color("black"),),(510,560),)
        screen.blit(font.render("50",True,pygame.Color("black"),),(610,560),)
        screen.blit(font.render("60",True,pygame.Color("black"),),(710,560),)
        screen.blit(font.render("70",True,pygame.Color("black"),),(810,560),)
        screen.blit(font.render("80",True,pygame.Color("black"),),(910,560),)
        screen.blit(font.render("90",True,pygame.Color("black"),),(1010,560),)
        #pygame.display.flip()

        ### Update physics
        fps = 60
        dt = 1.0 / fps
        space.step(dt)

        delta = clock.tick(fps)
        
        #Reed Code
        guimanager.update(delta)
        screen.blit(backcolor, (0,0))
        guimanager.draw_ui(screen)
        pygame.display.update()
        #Reed Code

        #update GUI stuff
        manager.update(delta)
        manager.draw_ui(screen)
        pygame.display.flip()
        

if __name__ == "__main__":
    sys.exit(main())