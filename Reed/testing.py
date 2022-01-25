import pygame
(width, height) = (1000, 600)
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Physics Tutorial')
backcolor = (255,255,0)
window.fill(backcolor)

pygame.display.flip()
#used to close program
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False