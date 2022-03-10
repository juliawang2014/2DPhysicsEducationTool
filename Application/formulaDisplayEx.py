from typing import List
import globals

# Library imports
import pygame
import libraries.shapes as shapes
import libraries.formulaDisplay as fDisplay

# pymunk imports
import pymunk
import pymunk.pygame_util


class BouncyBalls(object):
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
        self.queried_item = None

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
            if self.queried_item is not None:
                print("Velocity " + str(fDisplay.display_values(self.queried_item, "velocity")))
                print("Angular Velocity " + str(fDisplay.display_values(self.queried_item, "angular_velocity")))
                print("Mass " + str(fDisplay.display_values(self.queried_item, "mass")))
                print("Moment " + str(fDisplay.display_values(self.queried_item, "moment")))
                print("Force " + str(fDisplay.display_values(self.queried_item, "force")))
                print("Angle " + str(fDisplay.display_values(self.queried_item, "angle")))
                print("Position " + str(fDisplay.display_values(self.queried_item, "position")))
                print("Center of Gravity " + str(fDisplay.display_values(self.queried_item, "center_of_gravity")))
                print("Torque " + str(fDisplay.display_values(self.queried_item, "torque")))
            self._process_events()
            self._clear_screen()
            self._draw_objects()
            pygame.display.flip()
            # Delay fixed time between frames
            self._clock.tick(50)
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.on_mouse_pressed()
    
    def on_mouse_pressed(self):
        shape_list = self._space.point_query(pygame.mouse.get_pos(), 1, pymunk.ShapeFilter())

        if len(shape_list) > 0:
            self.queried_item = shape_list[0].shape.body
        else:
            self.queried_item = None
            shapes.create_ball(self, pygame.mouse.get_pos())

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


if __name__ == "__main__":
    game = BouncyBalls()
    game.run()
