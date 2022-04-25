# #Reed Code

import pygame_gui
from pygame_gui.elements import UITextEntryLine
from pygame_gui.elements import UITextBox
from pygame_gui.elements import UIHorizontalSlider
from pygame_gui.windows import UIColourPickerDialog
# Reed Code

from typing import List

import pygame
import pygame_gui
import pymunk
import pymunk.pygame_util
import libraries.shapes as shapes
import globals
import libraries.formulaDisplay as fDisplay
import libraries.toggleButton as toggleButton
import sys

GUI_background = pygame.image.load('img/4999GUIbackground.png')

class Spring(object):
    def __init__(self) -> None:
    
        #remove sceneselector so it will initialize right later
        if "sceneselector" in sys.modules:
            sys.modules.pop('sceneselector')
        
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
        self._joints: List[pymunk.PinJoint] = []
        # Execution control
        self._running = True
        self._pause = False
        # GUI
        self._font = pygame.font.SysFont("Arial", 16)
        self._guimanager = pygame_gui.UIManager((1200,700),'themes/GUI_Theme.json')
        self._backcolor = pygame.Surface((1200,100))
        self.console_text = ""
        self._custom_color = pygame.Color(0,0,0)
        self._color_choice = None
        self.ui_window1 = None
        self._shape_selected = "Circle"
        self._attachment_points = []
        self._point_a = None
        self._point_b = None
        self._mass = 10.0
        self._friction = 0.9
        self._elasticity = 0.95
        self._size_text_x = "Radius"
        self._size_text_y = ""
        self._GUI()
        # Mouse interaction
        self.shape_being_dragged = None
        self.queried_item = None
        self.rotate_amount = 1.0
        self._new_angle = 0.0

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
            self._screen.blit(GUI_background, (0,0))
            self._screen.blit(source=self._font.render(self._size_text_x, True, pygame.Color("White")), dest=(570, 37))
            self._screen.blit(source=self._font.render(self._size_text_y, True, pygame.Color("White")), dest=(570, 70))
            self._screen.blit(source=self._font.render("Size sliders", True, pygame.Color("White")), dest=(715, 17))
            self._guimanager.draw_ui(self._screen)
            if self.queried_item is not None:
                r = self.queried_item.radius + 10
                p = pymunk.pygame_util.to_pygame(self.queried_item.body.position, self._screen)
                pygame.draw.circle(self._screen, pygame.Color("red"), p, int(r), 6)
                self.console_text = "Velocity: {0} Mass: {1} Elasticity: {2} Friction: {3}".format(
                    str(fDisplay.display_values(self.queried_item.body, "velocity")), 
                    str(fDisplay.display_values(self.queried_item.body, "mass")),
                    str(self.queried_item.elasticity),
                    str(self.queried_item.friction))
                self.console_output.set_text(self.console_text)
            pygame.display.update()
            pygame.display.set_caption("2DPhysicsEducationTool- Spring Simulation")

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
            pymunk.Segment(static_body, (window_w-250, 0), (window_w-250, window_h), 0.0),
            pymunk.Segment(static_body, (0, window_h), (window_w, window_h), 0.0),
        ]
        for line in static_lines:
            line.elasticity = 0.95
            line.friction = 0.9
        self._space.add(*static_lines)
        shapes.create_static_circle((200, 200))
        shapes.create_static_circle((400, 200))
        shapes.create_static_circle((600, 200))
        shapes.create_static_circle((800, 200))
        shapes.create_static_rect((200, 350), 25, 25)
        shapes.create_static_rect((400, 350), 25, 25)
        shapes.create_static_rect((600, 350), 25, 25)
        shapes.create_static_rect((800, 350), 25, 25)
    
    def _reset(self):
        for j in self._joints:
            self._space.remove(j)
        for s in self._space.shapes:
            self._space.remove(s)
        self._add_static_scenery()

    def _process_events(self) -> None:
        """
        Handle game and events like keyboard input. Call once per frame only.
        :return: None
        """
        for event in pygame.event.get():
            self._guimanager.process_events(event)
            if event.type == pygame.QUIT:
                self._running = False
                import sceneselector
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self._running = False
                import sceneselector
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_p) or (event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self._pause_button):
                self._pause = not self._pause
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self._reset()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self._color_choice is not None or self.ui_window1 is not None:
                    pass
                elif event.button == 4:
                    self.rotate_shape_left()
                elif event.button == 5:
                    self.rotate_shape_right()
                elif pygame.mouse.get_pos()[1] >= 100 and pygame.mouse.get_pos()[0] <= pygame.display.Info().current_w - 250:
                    self.on_mouse_press(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 4 or event.button == 5:
                    pass
                else:
                    self.on_mouse_release()
            elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                self.update_values()
            elif event.type == pygame_gui.UI_BUTTON_PRESSED and self.toggle_query.pressed():
                self.toggle_query.toggle()
            elif event.type == pygame_gui.UI_BUTTON_PRESSED and self.toggle_spawn.pressed():
                self.toggle_spawn.toggle()
            elif event.type == pygame_gui.UI_BUTTON_PRESSED and self.toggle_kinematic.pressed():
                self.toggle_kinematic.toggle()
            elif event.type == pygame_gui.UI_BUTTON_PRESSED and self._color_button.check_pressed():
                self._color_choice = UIColourPickerDialog(rect=pygame.Rect(450,50, 390, 390),manager=self._guimanager,object_id='textb', visible=1)
                self._color_button.disable()
            elif event.type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED:
                self._custom_color = self._color_choice.current_colour
            elif (event.type == pygame_gui.UI_WINDOW_CLOSE and event.ui_element == self._color_choice):
                self._color_button.enable()
                self._color_choice = None
            elif (event.type == pygame_gui.UI_WINDOW_CLOSE and event.ui_element == self.ui_window1):
                self.ui_window1 = None
            elif event.type == pygame_gui.UI_BUTTON_PRESSED and self._circle_button.check_pressed():
                self._shape_selected = "Circle"
                self._size_text_x = "Radius"
                self._size_text_y = ""
            elif event.type == pygame_gui.UI_BUTTON_PRESSED and self._square_button.check_pressed():
                self._shape_selected = "Square"
                self._size_text_x = "Width"
                self._size_text_y = "Height"
            elif event.type == pygame_gui.UI_BUTTON_PRESSED and self._tri_button.check_pressed():
                self._shape_selected = "Triangle"
                self._size_text_x = "Width"
                self._size_text_y = "Height"
            elif event.type == pygame_gui.UI_BUTTON_PRESSED and self._line_button.check_pressed():
                self._shape_selected = "Attach"
                self._size_text_x = "Stiffness"
                self._size_text_y = "Damping"
            elif event.type == pygame_gui.UI_BUTTON_PRESSED and self._quit_button.check_pressed():
                self._running = False
                import sceneselector
            elif event.type == pygame_gui.UI_BUTTON_PRESSED and self._menu_button.check_pressed():
                info_message = """ To use the scene, change the mass to the mass you would like a ball and click enter.
                After click on the ball icon on the side and right click to spawn a ball on the pre spawned cubes. Do this for 4 balls, feel free to change the mass of each one.
                After click on the spring icon(bottom right of the 4) change the damping and stiffness sliders to change the effects of the spring before spawning them in.
                To add the spring, right click on each circle and a spring will connect them.
                Click on the spawn mode button and it will change to delete. click on a shape that is not the spring then Right click the cubes below and watch the spring work!
                Keyboard shortcuts: p to pause, r to reset
                Right click to delete shapes.
                """
                self.ui_window1 = pygame_gui.windows.UIMessageWindow(html_message=info_message,rect=pygame.Rect((400, 150), (300, 300)), manager=self._guimanager, object_id="Messagebx")

        self.on_mouse_motion()
            
    def update_values(self):
        try:
            num_grav = float(self._gravity_box.get_text())
        except:
            grav = ''
        else:
            grav = num_grav

        try:
            num_elas = float(self._elas_box.get_text())
        except:
            elas = ''
        else:
            elas = num_elas
        
        try:
            num_fric = float(self._friction_box.get_text())
        except:
            fric = ''
        else:
            fric = num_fric
        
        try:
            num_mass = float(self._mass_box.get_text())
        except:
            mass = ''
        else:
            mass = num_mass

        if grav == '':
            grav_value = 0.0
        else:
            grav_value = float(grav)
            
        self._space.gravity = (0.0, grav_value)

        if elas == '':
            self._elasticity = 0.0
        else:
            self._elasticity = float(elas)

        if fric == '':
            self._friction = 0.0
        else:
            self._friction = float(fric)
        
        if mass == '':
            self._mass = 1.0
        else:
            self._mass = float(mass)

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

        #textboxes and buttons for main gui
        self._backcolor.fill(pygame.Color('#1d1135'))
        
        #Text 1
        text_box = UITextBox(html_text="Gravity",relative_rect=pygame.Rect(50, 17, 100, 35),manager=self._guimanager,object_id='textb')

        #first text box
        self._gravity_box = UITextEntryLine(relative_rect=pygame.Rect(50,50, 100, 35),manager=self._guimanager,object_id='entryb')
        self._gravity_box.set_text("900")

        #text 2
        text_box = UITextBox(html_text="Mass",relative_rect=pygame.Rect(150, 17, 100, 35),manager=self._guimanager,object_id='textb')

        #second text box
        self._mass_box = UITextEntryLine(relative_rect=pygame.Rect(150,50, 100, 35),manager=self._guimanager,object_id='entryb')
        self._mass_box.set_text("10")
        #text 3
        text_box = UITextBox(html_text="Elasticity",relative_rect=pygame.Rect(250, 17, 100, 35),manager=self._guimanager,object_id='textb')

        #third text box
        self._elas_box = UITextEntryLine(relative_rect=pygame.Rect(250,50, 100, 35),manager=self._guimanager,object_id='entryb')
        self._elas_box.set_text("0.95")
        #text 4
        text_box = UITextBox(html_text="Friction",relative_rect=pygame.Rect(350, 17, 100, 35),manager=self._guimanager,object_id='textb')

        #fourth text box
        self._friction_box = UITextEntryLine(relative_rect=pygame.Rect(350,50, 100, 35),manager=self._guimanager,object_id='entryb')
        self._friction_box.set_text('0.9')
        #text 5
        self._color_button = pygame_gui.elements.UIButton(text="Color",relative_rect=pygame.Rect(450, 17, 100, 35),manager=self._guimanager,object_id='toggleButton')

        #second text box
        #self._color_choice = UIColourPickerDialog(rect=pygame.Rect(450,50, 390, 390),manager=self._guimanager,object_id='textb', visible=0)

        self._size_slider_x = UIHorizontalSlider(relative_rect=pygame.Rect((630, 37), (250, 25)), start_value=25, value_range=[1, 100], manager=self._guimanager, object_id='button')
        self._size_slider_y = UIHorizontalSlider(relative_rect=pygame.Rect((630, 70), (250, 25)), start_value=25, value_range=[1, 100], manager=self._guimanager, object_id='button')

        #Shapes buttons
        self._circle_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((975, 250), (100, 100)),text='',manager=self._guimanager,object_id='circleButton')
        self._square_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1075, 250), (100, 100)),text='',manager=self._guimanager,object_id='squareButton')
        self._tri_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((975, 350), (100, 100)),text='',manager=self._guimanager,object_id='triButton')
        self._line_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1075, 350), (100, 100)),text='',manager=self._guimanager,object_id='lineButton')
        #Pause Button
        self._pause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((900, 25), (100, 50)),text='Pause',manager=self._guimanager,object_id='button')

        #Info Button
        self._menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1000, 25), (100, 50)),text='Info',manager=self._guimanager,object_id='button')
        
        #Quit Button
        self._quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1100, 25), (100, 50)),text='Quit',manager=self._guimanager,object_id='button')

        self.console_output = pygame_gui.elements.UITextBox(html_text="", relative_rect=pygame.Rect((950, 450), (250, 250),), manager=self._guimanager, object_id="textb")

        self.toggle_query = toggleButton.ToggleButton(rect=pygame.Rect((950,100),(250,50)), text1="Query Mode: On", text2="Move Mode: On", manager=self._guimanager, object_id="toggleButton")
        self.toggle_spawn = toggleButton.ToggleButton(rect=pygame.Rect((950,150),(250,50)), text1="Spawn Mode: On", text2="Destroy Mode: On", manager=self._guimanager, object_id="toggleButton")
        self.toggle_kinematic = toggleButton.ToggleButton(rect=pygame.Rect((950,200),(250,50)), text1="Kinematic Shapes: On", text2="Static Shapes: On", manager=self._guimanager, object_id="toggleButton")

    def on_mouse_press(self, event):
        
        self._point_a = pygame.mouse.get_pos()
        shape_list = self._space.point_query(self._point_a, 1, pymunk.ShapeFilter())
        
        size_x = self._size_slider_x.get_current_value()
        size_y = self._size_slider_y.get_current_value()

        if len(shape_list) > 0:
            if self._shape_selected == "Attach":
                self._attachment_points.append(shape_list[0])
                if len(self._attachment_points) == 2:
                    a = self._attachment_points[0]
                    b = self._attachment_points[1]
                    if a.shape != b.shape:
                        #joint = pymunk.PinJoint(a.shape.body, b.shape.body)
                        joint = pymunk.DampedSpring(a.shape.body, b.shape.body, (0,0), (0,0), 5, size_x, size_y)
                        self._space.add(joint)
                        self._joints.append(joint)
                    self._attachment_points.clear()
            #Destroy
            elif not self.toggle_spawn.get_state() or event.button == 3:
                self._space.remove(shape_list[0].shape)
            else:
                #Query shape
                if self.toggle_query.get_state():
                    self.shape_being_dragged = None
                    self.queried_item = shape_list[0].shape
                #Drag shape
                else:
                    self.queried_item = None
                    self.shape_being_dragged = shape_list[0]
        #Spawn shapes
        elif self.toggle_spawn.get_state():
            #Spawn kinematic shapes
            if self.toggle_kinematic.get_state():
                if self._shape_selected == "Circle":
                    shapes.create_ball(self, self._point_a, 
                        color=self._custom_color, 
                        radius=size_x,
                        elasticity=self._elasticity,
                        friction=self._friction,
                        mass=self._mass)
                elif self._shape_selected == "Square":
                    shapes.create_rectangle(self, self._point_a, 
                        size_x=size_x, 
                        size_y=size_y,
                        elasticity=self._elasticity,
                        friction=self._friction,
                        mass=self._mass,
                        color=self._custom_color)
                elif self._shape_selected == "Triangle":
                    shapes.create_triangle(self, self._point_a, 
                        size_x=size_x, 
                        size_y=size_y,
                        elasticity=self._elasticity,
                        friction=self._friction,
                        mass=self._mass,
                        color=self._custom_color)
            #Spawn static shapes
            else:
                if self._shape_selected == "Circle":
                    shapes.create_static_circle(self._point_a, 
                        color=self._custom_color, 
                        radius=size_x)
                elif self._shape_selected == "Square":
                    shapes.create_static_rect(self._point_a,
                        color=self._custom_color,
                        size_x=size_x,
                        size_y=size_y)
                elif self._shape_selected == "Triangle":
                    shapes.create_static_triangle(self._point_a,
                        color=self._custom_color,
                        size_x=size_x,
                        size_y=size_y)

    def rotate_shape_left(self):
        if self.shape_being_dragged is not None:
            self.shape_being_dragged.shape.body.angle += self.rotate_amount
            self._new_angle = self.shape_being_dragged.shape.body.angle
    
    def rotate_shape_right(self):
        if self.shape_being_dragged is not None:
            self.shape_being_dragged.shape.body.angle -= self.rotate_amount
            self._new_angle = self.shape_being_dragged.shape.body.angle

    def on_mouse_release(self):
        self.shape_being_dragged = None
        self._new_angle = 0.0

    def on_mouse_motion(self):
        if self.shape_being_dragged is not None and not self.toggle_query.get_state():
            self.shape_being_dragged.shape.body.position = pygame.mouse.get_pos()
            self.shape_being_dragged.shape.body.velocity = 0, 0
            if self.shape_being_dragged.shape.body.angle != self._new_angle:
                self.shape_being_dragged.shape.body.angle = self._new_angle

if __name__ == "__main__":
    game = Spring()
    game.run()

