import os

import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.button import Button
from buffalo.option import Option

from saves import Saves

class Menu(Scene):

    def on_escape(self):
        print(self.characterOption.label.text)
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
                (10, utils.SCREEN_H - 10),
                "Create New Character",
                invert_y_pos = True,
                func=self.go_to_createCharacter
            )
        )
        self.buttons.add(
            Button(
                (utils.SCREEN_W / 2, utils.SCREEN_H / 2 + 160),
                "New Solo Game",
                x_centered=True,
                y_centered=True,
                func = self.go_to_gameTestScene
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
        self.characterOption = Option(
                (utils.SCREEN_W / 2, utils.SCREEN_H / 2 + 100),
                [character for character in os.listdir("characters")],
                x_centered=True,
                y_centered=True,
            )
        self.options.add(self.characterOption)

    def go_to_createCharacter(self):
        utils.set_scene(
            CreateCharacter()
        )
    def go_to_options(self):
        utils.set_scene(
            Options()
        )
    def go_to_gameTestScene(self):
        utils.set_scene(
            GameTestScene(self.characterOption.label.text)
        )

from createCharacter import CreateCharacter
from gameTestScene import GameTestScene
from options import Options
