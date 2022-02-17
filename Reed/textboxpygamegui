import pygame
import pygame_gui
import pymunk
import pymunk.pygame_util
from pygame_gui.elements import UITextEntryLine
from pygame_gui.elements import UITextBox

from pygame_gui import UIManager

pygame.init()

pygame.display.set_caption('Physics Tutorial')
window = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()

circlesz = pygame.Surface((200,200))

backcolor = pygame.Surface((1000,600))
backcolor.fill(pygame.Color('#FFFF00'))

guimanager = pygame_gui.UIManager((1000,200))

text_box = UITextEntryLine(
     relative_rect=pygame.Rect(100, 100, 200, 50),
     manager=guimanager)

#size1 = text_box.get_text()
#print(size1)
size = ""

circsize = 100

text_box_update = UITextBox(
        html_text=size,
        relative_rect=pygame.Rect(400, 100, 100, 50),
        manager=guimanager)


#pygame.draw.circle(circlesz, (255,255,255), (400,200), 100)

##PYMUNK-----------
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

    # Shapes that exist in the world
    self._balls: List[pymunk.Circle] = []
    self._rects: List[pymunk.Poly] = []
    # Execution control
    self._running = True

#### PYMUNK-----

while True:
    time_delta = clock.tick(60)/1000.0
    #used to close program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            print("Entered text:", event.text)
            pygame.draw.circle(circlesz, (255,255,255), (100,100), int(event.text),10)
            text_box_update.full_redraw()
            text_box_update.append_html_text(event.text)
            
        guimanager.process_events(event)

    newSize = text_box.get_text()
    if (size != newSize):
        size = newSize
        print(size)

    #pygame.draw.circle(circlesz, (255,255,255), (100,100), 100,10)
    #pygame.draw.rect(400, 100, 200, 100) 
    guimanager.update(time_delta)

    window.blit(backcolor, (0,0))
    window.blit(circlesz, (200,200))
    guimanager.draw_ui(window)

    pygame.display.update()