import pygame_gui

class ToggleButton():
    def __init__(self, rect, text, manager):
        self.rect = rect
        self.text = text
        self.manager = manager
        self.toggled = False

        pygame_gui.elements.UIButton(self.rect, self.text, self.manager)
    
    def toggle(self):
        self.toggled = not self.toggled
    
    def get_state(self):
        return self.toggled