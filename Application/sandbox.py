# #Reed Code

import pygame_gui
from pygame_gui.elements import UITextEntryLine
from pygame_gui.elements import UITextBox
# Reed Code

from typing import List

import pygame
import pygame_gui
import pymunk
import pymunk.pygame_util
import libraries.shapes as shapes
import globals

class Sandbox(object):
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
        screen_width = 1200
        screen_height = 700

        self._screen = pygame.display.set_mode((screen_width,screen_height))
        self._clock = globals.clock

        self._draw_options = pymunk.pygame_util.DrawOptions(self._screen)

        # Static barrier walls (lines) that the balls bounce off of
        self._add_static_scenery()

        # Shapes that exist in the world
        self._balls: List[pymunk.Circle] = []
        self._rects: List[pymunk.Poly] = []
        # Execution control
        self._running = True
        self._pause = False
        # GUI
        font = pygame.font.SysFont("Arial", 16)
        self._guimanager = pygame_gui.UIManager((1200,200),'/themes/GUI_Theme.json')
        self._backcolor = pygame.Surface((1200,100))
        self._GUI()

        # Mouse interaction
        self.shape_being_dragged = None

    def run(self) -> None:
        """
        The main loop of the game.
        :return: None
        """
        # Main loop
        while self._running:
            # Progress time forward
            if not self._pause:
                for _ in range(self._physics_steps_per_frame):
                    self._space.step(self._dt)

            self._process_events()
            self._clear_screen()
            self._draw_objects()
            #pygame.display.flip()
            # Delay fixed time between frames
            self._clock.tick(60)
            self._guimanager.update(self._clock.get_fps())
            self._screen.blit(self._backcolor, (0,0))
            self._guimanager.draw_ui(self._screen)
            pygame.display.update()
            pygame.display.set_caption("Sandbox - fps: " + str(self._clock.get_fps()))

    def _add_static_scenery(self) -> None:
        """
        Create the static bodies.
        :return: None
        """
        window_w = pygame.display.Info().current_w
        window_h = pygame.display.Info().current_h
        static_body = self._space.static_body
        static_lines = [
            pymunk.Segment(static_body, (0, 100), (window_w, 100), 0.0),
            pymunk.Segment(static_body, (0, 0), (0, window_h), 0.0),
            pymunk.Segment(static_body, (window_w, 0), (window_w, window_h), 0.0),
            pymunk.Segment(static_body, (0, window_h), (window_w, window_h), 0.0),
        ]
        for line in static_lines:
            line.elasticity = 0.95
            line.friction = 0.9
        self._space.add(*static_lines)

    def _process_events(self) -> None:
        """
        Handle game and events like keyboard input. Call once per frame only.
        :return: None
        """
        for event in pygame.event.get():
            self._guimanager.process_events(event)
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self._running = False
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_p) or (self._pause_button.process_event(event)):
                self._pause = not self._pause
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[1] <= event.pos[0] - 200):
                    self.on_mouse_press()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.on_mouse_release()

        self.on_mouse_motion()
            

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

    def _GUI(self):
        ### Reed Code -------------------------------   

        #textboxes and buttons for main gui
        self._backcolor.fill(pygame.Color('#1d1135'))
        pygame.display.set_caption('Physics Tutorial')
        
        #Text 1
        text_box = UITextBox(html_text="Text1",relative_rect=pygame.Rect(50, 17, 100, 35),manager=self._guimanager,object_id='textb')

        #first text box
        self._text_box = UITextEntryLine(relative_rect=pygame.Rect(50,50, 100, 35),manager=self._guimanager,object_id='entryb')

        #text 2
        text_box = UITextBox(html_text="Text2",relative_rect=pygame.Rect(150, 17, 100, 35),manager=self._guimanager,object_id='textb')

        #second text box
        self._text_box2 = UITextEntryLine(relative_rect=pygame.Rect(150,50, 100, 35),manager=self._guimanager,object_id='entryb')

        #text 3
        text_box = UITextBox(html_text="Text3",relative_rect=pygame.Rect(250, 17, 100, 35),manager=self._guimanager,object_id='textb')

        #third text box
        self._text_box3 = UITextEntryLine(relative_rect=pygame.Rect(250,50, 100, 35),manager=self._guimanager,object_id='entryb')

        #text 4
        text_box = UITextBox(html_text="Text4",relative_rect=pygame.Rect(350, 17, 100, 35),manager=self._guimanager,object_id='textb')

        #fourth text box
        self._text_box4 = UITextEntryLine(relative_rect=pygame.Rect(350,50, 100, 35),manager=self._guimanager,object_id='entryb')

        #text 5
        text_box = UITextBox(html_text="Text5",relative_rect=pygame.Rect(450, 17, 100, 35),manager=self._guimanager,object_id='textb')

        #second text box
        self._text_box5 = UITextEntryLine(relative_rect=pygame.Rect(450,50, 100, 35),manager=self._guimanager,object_id='entryb')

        #Menu Button
        self._pause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((900, 25), (100, 50)),text='Pause',manager=self._guimanager,object_id='button')

        #Info Button
        self._menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1000, 25), (100, 50)),text='Menu',manager=self._guimanager,object_id='button')
        
        ### Reed Code -----------------------------------------------------------

    def on_mouse_press(self):
        shape_list = self._space.point_query(pygame.mouse.get_pos(), 1, pymunk.ShapeFilter())

        if len(shape_list) > 0:
            self.shape_being_dragged = shape_list[0]
        else:
            shapes.create_ball(self, pygame.mouse.get_pos())

    def on_mouse_release(self):
        self.shape_being_dragged = None
    
    def on_mouse_motion(self):
        if self.shape_being_dragged is not None:
            self.shape_being_dragged.shape.body.position = pygame.mouse.get_pos()
            self.shape_being_dragged.shape.body.velocity = 0, 0

if __name__ == "__main__":
    game = Sandbox()
    game.run()

