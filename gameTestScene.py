import sys

import pygame
from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label

from saves import Saves
from chunk import Chunk
from camera import Camera
from mapManager import MapManager
from pluginManager import PluginManager
from inventoryUI import InventoryUI
from inventory import Inventory
from guiManager import GUIManager

from playerCharacter import PlayerCharacter

class GameTestScene(Scene):
    def __init__(self, pc):
        Scene.__init__(self)
        self.BACKGROUND_COLOR = (0, 0, 0, 255)
        PluginManager.loadPlugins()
        Camera.init()
        pc = Saves.unstore(pc, "characters")
        self.pc = pc if pc is not None else PlayerCharacter(
                Inventory(),
                name="Sean",
                fPos=(float(utils.SCREEN_M[0]), float(utils.SCREEN_M[1])),
                size=(32, 64),
                speed=.25,
                color=(255,0,0,255),
            )
        self.labels.add(
            Label(
                (5,5),
                "Location",
                x_centered=True,
                y_centered=True,
            )
        )
        Camera.lock(self.pc)
        self.UIManager = GUIManager()
        self.UIManager.guiScreens.append(InventoryUI(self.pc.inventory, self.UIManager))
        self.UIManager.updateGUIs()


    def on_escape(self):
        Saves.store(self.pc)
        sys.exit()

    def update(self):
        keys = pygame.key.get_pressed()
        self.pc.update(keys)
        self.UIManager.update()
        Camera.update()

    def blit(self):
        Camera.blitView()
        self.UIManager.blit(utils.screen, (0,0))
        self.pc.blit(utils.screen)
