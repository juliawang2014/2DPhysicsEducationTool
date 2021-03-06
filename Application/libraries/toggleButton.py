import pygame_gui

class ToggleButton():
    def __init__(self, rect, text1, text2, manager, object_id):
        self.rect = rect
        self.text1 = text1
        self.text2 = text2
        self.manager = manager
        self.toggled = True
        self.object_id = object_id

        self.button = pygame_gui.elements.UIButton(self.rect, text1, self.manager, object_id=self.object_id)

    def pressed(self):
        return self.button.check_pressed()

    def toggle(self):
        self.toggled = not self.toggled
        if self.toggled:
            self.button.set_text(self.text1)
        else:
            self.button.set_text(self.text2)

    def get_state(self):
        return self.toggled