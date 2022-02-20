from typing import List

import pygame_gui
from libraries.toggleButton import ToggleButton
import globals

# Library imports
import pygame
import libraries.shapes as shapes

# pymunk imports
import pymunk
import pymunk.pygame_util


class ToggleButtonExample(object):
    """
    This class implements a simple scene in which there is a static platform (made up of a couple of lines)
    that don't move. Balls appear spawn on mouse click and drop onto the platform. They bounce around.
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

        # pygame_gui stuff
        self.manager = pygame_gui.UIManager((globals.screen_width, globals.screen_height))
        self.togglebutton = ToggleButton(rect=pygame.Rect((80, 500),(250, 50)), text="Toggle spawn", manager=self.manager)
        self.time_delta = 0.0


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

            self._process_events()
            self._clear_screen()
            self._draw_objects()
            #self.window_surface.blit(self.background, (0,0))
            pygame.display.flip()
            #pygame.display.update()
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
            pymunk.Segment(static_body, (0, 0), (window_w, 0), 0.0),
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
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self._running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pygame.image.save(self._screen, "bouncing_balls.png")
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                self.togglebutton.toggle()
                print(self.togglebutton.get_state())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.togglebutton.get_state():
                    shapes.create_ball(self, pygame.mouse.get_pos())
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
        
        self.manager.draw_ui(self._screen)


if __name__ == "__main__":
    game = ToggleButtonExample()
    game.run()
