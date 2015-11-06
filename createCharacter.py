import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.button import Button
from buffalo.input import Input
from buffalo.option import Option

from inventory import Inventory
from saves import Saves
from playerCharacter import PlayerCharacter

class CreateCharacter(Scene):

        def on_escape(self):
                self.go_to_main_menu()

        def update(self):
                pass

        def blit(self):
                pass

        def __init__(self):
                super(CreateCharacter, self).__init__()
                self.BACKGROUND_COLOR = (177, 0, 50, 255)
                Button.DEFAULT_BG_COLOR = (100, 100, 100, 255)
                self.labels.add(
                        Label(
                                (utils.SCREEN_W / 2 - 75, utils.SCREEN_H / 2 - 60),
                                "Name: ",
                                y_centered=True,
                                x_centered=True,
                        )
                )
                self.characterName  = Input(
                                (utils.SCREEN_W / 2, utils.SCREEN_H / 2 - 60),
                                "name",
                                y_centered=True,
                                x_centered=True,
                        )
                self.inputs.add(self.characterName)
                self.labels.add(
                        Label(
                                (utils.SCREEN_W / 2 - 75, utils.SCREEN_H / 2),
                                "Speed: ",
                                y_centered=True,
                                x_centered=True,
                        )
                )
                self.speed = Option(
                                (utils.SCREEN_W / 2, utils.SCREEN_H / 2),
                                [str(n) for n in list(range(10,50))],
                                x_centered=True,
                                y_centered=True,
                        )
                self.options.add(self.speed)
                self.buttons.add(
                        Button(
                                (utils.SCREEN_W / 2, utils.SCREEN_H / 2 + 60),
                                "Create",
                                x_centered=True,
                                y_centered=True,
                                func=self.create_character,
                        )
                )
                self.buttons.add(
                        Button(
                                (utils.SCREEN_W / 2, utils.SCREEN_H / 2 + 120),
                                "Exit",
                                x_centered=True,
                                y_centered=True,
                                func = self.go_to_main_menu,
                        )
                )

        def go_to_main_menu(self):
                utils.set_scene(
                        Menu()
                )
        def create_character(self):
                if self.characterName.selected:
                        self.characterName.deselect()
                Saves.store(
                        PlayerCharacter(
                                Inventory(),
                                name=self.characterName.label.text,
                                speed = (float(self.speed.label.text) / 100),
                        )
                )
                self.go_to_main_menu()

from menu import Menu
