import pygame
import pygame_textinput
#window size

pygame.display.set_caption('Physics Tutorial')
input = pygame_textinput.TextInputVisualizer()
window = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()



#myrec = pygame.Rect((20,20),(50,100))
#inbox = pygame.draw.rect( (20, 20), (255, 255, 255), (50, 100))

while True:

    backcolor = (255,255,0)
    window.fill(backcolor)

    events = pygame.event.get()

    # Feed it with events every frame
    input.update(events)
    # Blit its surface onto the screen
    
    window.blit(input.surface, (10, 10))

    #used to close program
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()
    clock.tick(30)