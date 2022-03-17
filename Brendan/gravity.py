import sys
sys.path.append('../Julia')

from typing import List
import globals

# Library imports
import pygame
import libraries.shapes as shapes

# pymunk imports
import pymunk
import pymunk.pygame_util

#pygame imports
import pygame_gui

#other imports
import datetime

class BouncyBalls(object):
    """
    This class implements a simple scene in which there is a static platform (made up of a couple of lines)
    that don't move. Balls appear spawn on mouse click and drop onto the platform. They bounce around.
    Brendan here, hahaha I copied Julia's code
    ok all this copying is getting a bit much
    """

    def __init__(self) -> None:
        # Space
        self._space = globals.space
        self._space.gravity = globals.gravity

        # Physics
        # Time step
        self._dt = 1.0 / 60.0
        # Number of physics steps per screen frame
        self._physics_steps_per_frame = 1

        # pygame
        pygame.init()
        self._screen = globals.screen
        self._clock = globals.clock

        self._draw_options = pymunk.pygame_util.DrawOptions(self._screen)

        # Static barrier walls (lines) that the balls bounce off of
        self._add_static_scenery()

        # Balls that exist in the world
        self._balls: List[pymunk.Circle] = []

        # Execution control
        self._running = True
        
        #set up pygame stuff
        self.manager = pygame_gui.UIManager((globals.screen_width, globals.screen_height))
        #hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((80, 500), (250, 50)),
        #                                     text='Say Hello',
        #                                     manager=self.manager)
        #self.ui_slider1 = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(relative_rect=pygame.Rect((10, 470), (250, 50)), start_value=25, value_range=(1, 100), manager=self.manager, object_id="size") #ball size
        self.ui_slider2 = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(relative_rect=pygame.Rect((10, 540), (250, 50)), start_value=900, value_range=(0, 2000), manager=self.manager, click_increment=100, object_id="gravity") #gravity
        self.ui_textbox = pygame_gui.elements.ui_text_box.UITextBox(html_text="Gravity: "+str(self._space.gravity.int_tuple[1]), relative_rect=pygame.Rect((300, 540), (250, 50)), manager=self.manager, object_id="gravityInfoTextBox")
        self.ui_textbox2 = pygame_gui.elements.ui_text_box.UITextBox(html_text="", relative_rect=pygame.Rect((600, 340), (350, 250)), manager=self.manager, object_id="doneBox")
        self.ui_textbox3 = pygame_gui.elements.ui_text_box.UITextBox(html_text="Velocity:", relative_rect=pygame.Rect((300, 340), (250, 50)), manager=self.manager, object_id="velocityBox")
        self.done_box_text = ""
        self.spawn_button = pygame_gui.elements.ui_button.UIButton(relative_rect=pygame.Rect((10, 270), (250, 50)), text="Spawn Ball", manager=self.manager, object_id="spawn")
        #self.ui_textbox.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR,params={'time_per_letter':1})
        self.time_delta = 0.0
        
        #BALL SIZE
        self.ball_size = 25 #default is 25 from shapes.py
        
        self.ball_start_time = 0 #time object used to see when the ball is spawned
        self.ball_end_time = 0
        self.is_ball_done_rolling = False #turns true once ball is at the bottom of the ramp

    def run(self) -> None:
        """
        The main loop of the game.
        :return: None
        """
        # Main loop
        while self._running:
            # Progress time forward
            for _ in range(self._physics_steps_per_frame):
                self._space.step(self._dt)

            self._handle_ball_timing()
            self._show_ball_velocity()
            self._process_events()
            self._clear_screen()
            self._draw_objects()
            pygame.display.flip()
            # Delay fixed time between frames
            self.time_delta = self._clock.tick(60)
            pygame.display.set_caption("Bouncing balls - fps: " + str(self._clock.get_fps()))

    def _add_static_scenery(self) -> None:
        """
        Create the static bodies.
        :return: None
        """
        window_w = pygame.display.Info().current_w
        window_h = pygame.display.Info().current_h
        static_body = self._space.static_body
        static_lines = [
            pymunk.Segment(static_body, (0, 0), (window_w, 0), 1.0),
            pymunk.Segment(static_body, (0, 0), (0, window_h), 1.0),
            pymunk.Segment(static_body, (window_w, 0), (window_w, window_h), 1.0),
            pymunk.Segment(static_body, (0, window_h-400), (window_w, window_h-300), 5.0),
        ]
        for line in static_lines:
            line.elasticity = 0.0
            line.friction = 0.0
        self._space.add(*static_lines)

    def _process_events(self) -> None:
        """
        Handle game and events like keyboard input. Call once per frame only.
        :return: None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self._running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pygame.image.save(self._screen, "bouncing_balls.png")
        #    elif event.type == pygame.MOUSEBUTTONDOWN:
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_object_id == "spawn":
                    self._deleteAllBalls()
                    shapes.create_ball(self, (33,173), 10, self.ball_size, elasticity=0.1)
                    self.is_ball_done_rolling = False
                    self.ball_start_time = datetime.datetime.now()
            elif event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_object_id == "gravity":
                    if event.value != self._space.gravity.int_tuple[1]:
                        self._space.gravity = (0, event.value)
                        self.ui_textbox.clear_text_surface()
                        self.ui_textbox.set_text("Gravity: " + str(self._space.gravity.int_tuple[1]))         

            self.manager.process_events(event)

    def _clear_screen(self) -> None:
        """
        Clears the screen.
        :return: None
        """
        self._screen.fill(globals.background_color)

    def _draw_objects(self) -> None:
        """
        Draw the objects.
        :return: None
        """
        self._space.debug_draw(self._draw_options)
        self.manager.update(self.time_delta)
        #self._screen.blit()
        self.manager.draw_ui(self._screen)
        
    def _deleteAllBalls(self) -> None:
        """remove all balls from self._balls"""
        for ball in self._balls:
            self._space.remove(ball)
        self._balls = []
        
    def _handle_ball_timing(self) -> None:
        """take care of some timing stuff"""
        #if self._balls:
                #print(self._balls[0].body.position.x)
            #self.ui_textbox2.set_text(str(self._balls[0].body.position.x))
            #self.ui_textbox2.rebuild()
        if self._balls and self._balls[0].body.position.x > 974 and not self.is_ball_done_rolling:
            #section to calculate time delta
            self.ball_end_time = datetime.datetime.now()
            time_delta = self.ball_end_time - self.ball_start_time
            
            self.done_box_text += "ball done rolling, time:" + str(time_delta) + "<br>"
            self.ui_textbox2.set_text(self.done_box_text)
            self.is_ball_done_rolling = True
            
    def _show_ball_velocity(self) -> None:
        """update velocity text box to show ball velocity"""
        
        if self._balls:
            if abs(self._balls[0].body.velocity) > 0.01:
                self.ui_textbox3.set_text("Velocity: " + str(abs(self._balls[0].body.velocity)))
            else:
                self.ui_textbox3.set_text("Velocity: 0.0")
                #print(abs(self._balls[0].body.velocity))
         #   if not self.ball_previous_coords:
         #       self.ball_previous_coords = self._balls[0].body.position
         #   else:
         #       print(pymunk.vec2d.Vec2d.get_distance(self._balls[0].body.position, self.ball_previous_coords))
         #       self.ball_previous_coords = self._balls[0].body.position


if __name__ == "__main__":
    game = BouncyBalls()
    game.run()
