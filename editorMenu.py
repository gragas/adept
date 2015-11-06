import sys

import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.button import Button

class EditorMenu(Scene):

    def on_escape(self):
        exit()

    def update(self):
        pass

    def blit(self):
        pass

    def __init__(self):
        Scene.__init__(self)
        self.BACKGROUND_COLOR = (255, 0, 150, 255)
        Button.DEFAULT_BG_COLOR = (0, 0, 255, 255)
        Button.DEFAULT_COLOR = (255, 0, 0, 255)
        Label.DEFAULT_COLOR = (0, 0, 255, 255)
        self.labels.add(
            Label(
                (5, 5),
                "Adept Editor",
                font="default18"
            )
        )

        def go_to_edit_map_test_scene():
            from editMapTestScene import EditMapTestScene
            utils.set_scene(
                EditMapTestScene()
            )

        self.buttons.add(
            Button(
                (int(utils.SCREEN_W / 2), int(utils.SCREEN_H / 2 + 150)),
                "Edit Map",
                font="default18",
                x_centered=True,
                y_centered=True,
                func=go_to_edit_map_test_scene,
            )
        )
        
        self.buttons.add(
            Button(
                (int(utils.SCREEN_W / 2), int(utils.SCREEN_H / 2 + 225)),
                "Edit Items",
                font="default18",
                x_centered=True,
                y_centered=True,
            )
        )
        self.buttons.add(
            Button(
                (int(utils.SCREEN_W / 2), int(utils.SCREEN_H / 2 + 300)),
                "Edit Containers",
                font="default18",
                x_centered=True,
                y_centered=True,
            )
        )

        self.buttons.add(
            Button(
                (int(utils.SCREEN_W / 2), int(utils.SCREEN_H / 2 + 375)),
                "Exit",
                font="default18",
                x_centered=True,
                y_centered=True,
                func=sys.exit,
            )
        )
