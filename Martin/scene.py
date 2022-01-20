#import pygame module 
from numpy import true_divide
import pygame
import button
pygame.init()


X = 1000
Y = 600
#Background color is rbg color number.
White = (255,255,255)
Red = (255,0,0)
Blue = (202, 228, 241)
Black = (0,0,0)
background_color = (Blue)

#fps variable
clock = pygame.time.Clock()

#Dimensions of the screen for the scene 
screen = pygame.display.set_mode((X,Y))

#Set the caption of screen
pygame.display.set_caption('2DPhysicsEducationTool')

#set the color of scene 
screen.fill(background_color)

#information for font on the screen:
font1 = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 24)
font1Color = (Black)
text1 = font1.render('2D Physics Education Tool', True, font1Color)



start_img = pygame.image.load('img/start_btn.png').convert_alpha()
exit_img = pygame.image.load('img/quit_btn.jpg').convert_alpha()

#button instances
start_button = button.Button(100, 200, start_img, 0.45)
exit_button = button.Button(550, 200, exit_img, 0.35)



def physics_selector():
    print('physics selector')
    X = 1000
    Y = 600
    screen = pygame.display.set_mode((X,Y))
    pygame.display.set_caption("Select Physics Simulation")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((20, 20, 40))
    screen.blit(background,[0,0])
    #background_color = (White)
   # screen.fill(background_color)
    #screen.blit(screen,[0,0])
    pygame.display.flip()


pygame.display.flip()

running = True
#game loop here: 

while running:
    clock.tick(60)

    screen.blit(text1,(350,20))
    if start_button.draw(screen) == True:
        print("Start")
        physics_selector()
    if exit_button.draw(screen) == True:
        running = False
    #for loop for the event queue
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False
        

        pygame.display.update()