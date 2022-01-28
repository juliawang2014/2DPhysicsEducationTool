import pygame
import pygame_gui

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
