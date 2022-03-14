import pygame
import pygame_gui
from pygame_gui.elements import UITextEntryLine
from pygame_gui.elements import UITextBox
from pygame_gui.core import ObjectID

from pygame_gui import UIManager

pygame.init()

pygame.display.set_caption('Physics Tutorial')
window = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()

backcolor = pygame.Surface((1000,100))
backcolor.fill(pygame.Color('#1d1135'))

guimanager = pygame_gui.UIManager((1000,600),'Reed/GUI/GUI_Theme.json')

#Text 1
text_box = UITextBox(html_text="Text1",relative_rect=pygame.Rect(50, 17, 100, 35),manager=guimanager,object_id='textb')

#first text box
frstBox = pygame.Rect(50,50, 100, 35)
text_box = UITextEntryLine(relative_rect=frstBox,manager=guimanager,object_id='entryb')

#text 2
text_box = UITextBox(html_text="Text2",relative_rect=pygame.Rect(150, 17, 100, 35),manager=guimanager,object_id='textb')

#second text box
scdBox = pygame.Rect(150,50, 100, 35)
text_box2 = UITextEntryLine(relative_rect=scdBox,manager=guimanager,object_id='entryb')

#text 3
text_box = UITextBox(html_text="Text3",relative_rect=pygame.Rect(250, 17, 100, 35),manager=guimanager,object_id='textb')

#third text box
thdBox = pygame.Rect(250,50, 100, 35)
text_box3 = UITextEntryLine(relative_rect=thdBox,manager=guimanager,object_id='entryb')

#text 4
text_box = UITextBox(html_text="Text4",relative_rect=pygame.Rect(350, 17, 100, 35),manager=guimanager,object_id='textb')

#fourth text box
fthBox = pygame.Rect(350,50, 100, 35)
text_box4 = UITextEntryLine(relative_rect=fthBox,manager=guimanager,object_id='entryb')

#text 5
text_box = UITextBox(html_text="Text5",relative_rect=pygame.Rect(450, 17, 100, 35),manager=guimanager,object_id='textb')

#second text box
fifBox = pygame.Rect(450,50, 100, 35)
text_box5 = UITextEntryLine(relative_rect=fifBox,manager=guimanager,object_id='entryb')

#Menu Button
menu_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((750, 25), (100, 50)),
                                             text='Pause',
                                             manager=guimanager,object_id='button')

#Quit Button
quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((850, 25), (100, 50)),
                                             text='Menu',
                                             manager=guimanager,object_id='button')

while True:
    time_delta = clock.tick(60)/1000.0
    #used to close program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    guimanager.update(time_delta)

    window.blit(backcolor, (0,0))
    
    guimanager.draw_ui(window)

    pygame.display.update()