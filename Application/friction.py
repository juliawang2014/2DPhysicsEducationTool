from email.mime import application
import sys
sys.path.append('../Application')

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

#import for Reed GUI
from pygame_gui.elements import UITextEntryLine
from pygame_gui.elements import UITextBox
from pygame_gui.core import ObjectID
from pygame_gui import UIManager
from pygame_gui.elements import UITextBox

class Friction(object):

    def __init__(self) -> None:
        # Space
        self._space = globals.space
        self._space.gravity = globals.gravity
        self._rect_friction = 0.25

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

        # Static barrier walls (lines) that the cubes can't pass
        self._add_static_scenery()
        #self.staticSlopeBody = None

        # rects that exist in the world
        self._rects: List[pymunk.Circle] = []

        # Execution control
        self._running = True
        
        #set up pygame stuff
        self.manager = pygame_gui.UIManager((globals.screen_width, globals.screen_height),'themes/GUI_Theme.json')
        
        
        self.time_delta = 0.0
    
        #Offical Order of Items
        self.spawn_button = pygame_gui.elements.ui_button.UIButton(relative_rect=pygame.Rect((10, 25), (125, 50)), text="Spawn", manager=self.manager, object_id="spawn")
        self.ui_slider2 = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(relative_rect=pygame.Rect((145, 25), (150, 25)), start_value=self._rect_friction, value_range=(0, 2), manager=self.manager, click_increment=0.1, object_id="friction") #friction
        self.ui_slider3 = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(relative_rect=pygame.Rect((145, 50), (150, 25)), start_value=-100, value_range=(-100, 200), manager=self.manager, click_increment=10, object_id="slope") #slope
        self.ui_textbox = pygame_gui.elements.ui_text_box.UITextBox(html_text="Friction:<br>0.25", relative_rect=pygame.Rect((305, 12.5), (100, 75)), manager=self.manager, object_id="gravityInfoTextBox")
        self.ui_textbox3 = pygame_gui.elements.ui_text_box.UITextBox(html_text="Velocity:", relative_rect=pygame.Rect((410, 12.5), (100, 75)), manager=self.manager, object_id="velocityBox")
        self.ui_textbox2 = pygame_gui.elements.ui_text_box.UITextBox(html_text="", relative_rect=pygame.Rect((520, 12.5), (200, 75)), manager=self.manager, object_id="doneBox")
        self.info_button = pygame_gui.elements.ui_button.UIButton(relative_rect=pygame.Rect((730, 25), (125, 50)), text="Info", manager=self.manager, object_id="info")
        self.quit_button = pygame_gui.elements.ui_button.UIButton(relative_rect=pygame.Rect((865, 25), (125, 50)), text="Quit", manager=self.manager, object_id="quit")
        self.done_box_text = ""

        self.GUI_background = pygame.image.load('img/4999GUIbackground.png')
        self.GUI_background = pygame.transform.scale(self.GUI_background, (1000,100))

        #cube SIZE
        self.rect_size = 25 #default is 25 from shapes.py
        self.rect_start_time = 0 #time object used to see when the rect is spawned
        self.rect_end_time = 0
        self.is_rect_done_sliding = False #turns true once rect is at the bottom of the ramp

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

            self._handle_rectangle_timing()
            self._show_rectangle_velocity()
            self._process_events()
            self._clear_screen()
            self._draw_objects()
            pygame.display.flip()
            
            #Reed
            pygame.display.update()
            #Reed
            # Delay fixed time between frames
            self.time_delta = self._clock.tick(60)
            pygame.display.set_caption("2DPhysicsEducationTool - Friction")

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
          #  pymunk.Segment(static_body, (0, window_h-200), (window_w, window_h-100), 5.0),
        ]
        for line in static_lines:
            line.elasticity = 0.0
            line.friction = 0.0
        #static_lines[3].friction = 0.15
        self._space.add(*static_lines)
        
        #section for creating line segment at bottom
        staticSlopeBody = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.slopeSegment = pymunk.Segment(staticSlopeBody, (0, window_h-200), (window_w, window_h-100), 5.0)
        self.slopeSegment.friction = 0.15
        self._space.add(staticSlopeBody)
        self._space.add(self.slopeSegment)

    def _process_events(self) -> None:
        """
        Handle game and events like keyboard input. Call once per frame only.
        :return: None
        """
        for event in pygame.event.get():
            #create messagebox to open with button
            def createmessage():
                info_message="""Spawn a rectangle on the screen by clicking the spawn button. The time it takes will be recorded and displayed. After move the slider to change friction to see how the time changes!
                """
                self.ui_window1 = pygame_gui.windows.UIMessageWindow(html_message=info_message,rect=pygame.Rect((400, 150), (300, 300)), manager=self.manager, object_id="window")
            
            #event handling
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self._running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pygame.image.save(self._screen, "bouncing_rects.png")
        #    elif event.type == pygame.MOUSEBUTTONDOWN:
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_object_id == "spawn":
                    self._deleteAllRectangles()
                    shapes.create_rectangle(self, (33,373), size_x=self.rect_size, size_y=self.rect_size, elasticity=0.1, friction=self._rect_friction)
                    self._rects[0].body.angle = 0.1
                    self.is_rect_done_sliding = False
                    self.rect_start_time = datetime.datetime.now()
                elif event.ui_object_id == "info":
                    createmessage()
                    print("Info Button Pressed")
                elif event.ui_object_id == "quit":
                    pygame.quit(); sys.exit();
            elif event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_object_id == "friction":
                    if self._rects and event.value != self._rects[0].friction:
                        self._rects[0].friction = event.value
                        self.ui_textbox.clear_text_surface() 
                    self.ui_textbox.set_text("Friction:<br>" + str(round(event.value, 4)))   
                    self._rect_friction = event.value
                if event.ui_object_id == "slope":
                    if self.slopeSegment:
                        #update slope endpoints, based on friction slider rn
                        window_w = pygame.display.Info().current_w
                        window_h = pygame.display.Info().current_h
                        self.slopeSegment.unsafe_set_endpoints(self.slopeSegment.a.int_tuple, (window_w, window_h- (event.value) - 100))
                        self._space.reindex_static()
                        
                        if self._rects and (self.getSlopeYCoordAtX(self._rects[0].body.position.x) - self._rects[0].body.position.y) < 30:
                            #30 is the magic number, cube should always be 30 pixels above slope, so update position of cube when stuff moves
                            currentXPosition = self._rects[0].body.position.x
                            self._rects[0].body.position = pymunk.vec2d.Vec2d(currentXPosition, (self.getSlopeYCoordAtX(currentXPosition) - 30))

            self.manager.process_events(event)
            
    def getSlopeYCoordAtX(self, x):
        """
        Helper function to get the y coordinate of static slope at a given x coordinate
        """
        #print(self.slopeSegment.a.y, self.slopeSegment.b.y)
        window_w = pygame.display.Info().current_w
        rise = self.slopeSegment.b.y - self.slopeSegment.a.y
        slope = rise / window_w
        yCord = self.slopeSegment.a.y + slope * x
        return yCord

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
        #self._screen.blit(self.backcolor, (0,0))
        self._screen.blit(self.GUI_background, (0,0))
        self.manager.draw_ui(self._screen)
        

    def _deleteAllRectangles(self) -> None:
        """remove all rects from self._rects"""
        for rect in self._rects:
            self._space.remove(rect)
        self._rects = []
        
    def _handle_rectangle_timing(self) -> None:
        """take care of some timing stuff"""
        if self._rects and self._rects[0].body.position.x > 970 and not self.is_rect_done_sliding:
            #section to calculate time delta
            self.rect_end_time = datetime.datetime.now()
            time_delta = self.rect_end_time - self.rect_start_time
            
            self.done_box_text += "Cube done sliding, time:" + str(time_delta) + "<br>"
            self.ui_textbox2.set_text(self.done_box_text)
            self.is_rect_done_sliding = True
            
    def _show_rectangle_velocity(self) -> None:
        """update velocity text box to show cube velocity"""
        
        if self._rects:
            if abs(self._rects[0].body.velocity) > 0.01:
                self.ui_textbox3.set_text("Velocity: " + str(round((abs(self._rects[0].body.velocity)),2)))
            else:
                self.ui_textbox3.set_text("Velocity: 0.0")

if __name__ == "__main__":
    game = Friction()
    game.run()
