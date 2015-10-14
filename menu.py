import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.button import Button

class Menu(Scene):

    def on_escape(self):
        exit()

    def update(self):
        pass

    def blit(self):
        pass

    def __init__(self):
        Scene.__init__(self)
        self.BACKGROUND_COLOR = (177, 0, 50, 255)
        Button.DEFAULT_BG_COLOR = (100, 100, 100, 255)
        self.labels.add(
            Label(
                (5, 5),
                "Adept 0.0 Alpha <-> September 2015",
            )
        )
        self.labels.add(
            Label(
                utils.SCREEN_M,
                "",
                font="default48",
                x_centered=True,
                y_centered=True,
            )
        )
        self.buttons.add(
            Button(
                (utils.SCREEN_W / 2, utils.SCREEN_H / 2 + 100),
                "Create New Character",
                x_centered=True,
                y_centered=True,
            )
        )        
        self.buttons.add(
            Button(
                (utils.SCREEN_W / 2, utils.SCREEN_H / 2 + 160),
                "New Solo Game",
                x_centered=True,
                y_centered=True,
            )
        )
        self.buttons.add(
            Button(
                (utils.SCREEN_W / 2, utils.SCREEN_H / 2 + 220),
                "Load Solo Game",
                x_centered=True,
                y_centered=True,
            )
        )
        self.buttons.add(
            Button(
                (utils.SCREEN_W - 10, utils.SCREEN_H - 10),
                "Join Multiplayer Game",
                invert_x_pos=True,
                invert_y_pos=True,
            )
        )
        self.buttons.add(
            Button(
                (utils.SCREEN_W / 2, utils.SCREEN_H / 2 + 280),
                "Options",
                x_centered=True,
                y_centered=True,
                func=self.go_to_options,
            )
        )
        self.buttons.add(
            Button(
                (utils.SCREEN_W / 2, utils.SCREEN_H / 2 + 340),
                "Exit",
                x_centered=True,
                y_centered=True,
                func=exit,
            )
        )
        self.buttons.add(
            Button(
                (10, utils.SCREEN_H - 10),
                "Select Character",
                invert_y_pos=True,
                func=self.go_to_selectCharacter,
            )
        )

    def go_to_selectCharacter(self):
        utils.set_scene(
            SelectCharacter()
        )

    def go_to_options(self):
        utils.set_scene(
            Options()
        )

<<<<<<< HEAD
from selectcharacter import SelectCharacter
=======
from selectCharacter import SelectCharacter
from gameTestScene import GameTestScene
>>>>>>> fd4daf2a30e5444dfc8aa9503fe217f43fb4db6c
from options import Options
