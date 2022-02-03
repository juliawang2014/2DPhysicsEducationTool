import pygame
import pygame_gui

from pygame_gui.elements import UIHorizontalSlider

from pygame_gui import UIManager


pygame.init()

pygame.display.set_caption('Physics Tutorial')
window = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()

backcolor = pygame.Surface((1000,600))
backcolor.fill(pygame.color('#FFFF00'))

guimanager= pygame_gui.UIManager((1000,600))

circslide = UIHorizontalSlider(pygame.Rect((500,100),0,(0,100)),manager=guimanager)

while True:
    time_delta = clock.tick(60)/1000.0
    #used to close program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        guimanager.process_events(event)

    guimanager.update(time_delta)

    window.blit(backcolor, (0,0))
    guimanager.draw_ui(window)

    pygame.display.update()

#set caption for title
pygame.display.set_caption('Physics Tutorial')

#set size for screen
window = pygame.display.set_mode((1000,600))

while True:

    #fill background color
    backcolor = (255,255,0)
    window.fill(backcolor)

    events = pygame.event.get()

    #used to close program
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()

