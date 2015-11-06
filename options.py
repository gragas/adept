import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.button import Button

class Options(Scene):

    def on_escape(self):
        """
        Go back to the main menu.
        """
        self.go_to_main_menu()

    def update(self):
        pass

    def blit(self):
        pass

    def __init__(self):
        super().__init__()
        self.BACKGROUND_COLOR = (0, 177, 50, 255)
        self.buttons.add(
            Button(
                (10, utils.SCREEN_H - 10),
                "Back",
                invert_y_pos=True,
                func=self.go_to_main_menu,
            )
        )

    def go_to_main_menu(self):
        utils.set_scene(
            Menu()
        )

from menu import Menu
