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
from craftingUI import CraftingUI
from hotbarUI import HotbarUI
from subMap import SubMap
from tradingUI import TradingUI
from stair import Stair
from soundEngine import SoundEngine
from menu import Menu

from playerCharacter import PlayerCharacter
from friendly import Friendly
from enemy import Enemy
from trader import Trader

class GameTestScene(Scene):
    def __init__(self, pc_name):
        Scene.__init__(self)
        self.BACKGROUND_COLOR = (0, 0, 0, 255)
        PluginManager.loadPlugins()
        Camera.init()
        self.enemy = Enemy(name="monster", fPos=(0.0,0.0)) # Example enemy
        self.friendly = Friendly(name="villager", fPos=(0.0,0.0)) # Example friendly npc
        self.trader = Trader(name="merchant", fPos=(0.0,0.0)) # Example trader
        self.npcs = [self.enemy, self.friendly, self.trader]
        self.pc = Saves.unstore(pc_name, "characters")
        Camera.lock(self.pc)
        self.UIManager = GUIManager()
        self.UIManager.guiScreens.append(InventoryUI(self.pc.inventory, self.UIManager))
        self.UIManager.guiScreens.append(CraftingUI(self.pc.inventory))
        hb = HotbarUI(self.pc.inventory, self.UIManager)
        self.UIManager.guiScreens.append(hb)
        self.UIManager.alwaysOnGUIs.append(hb)
        self.UIManager.updateGUIs()

        SoundEngine.playMusic("BlipStream.wav")

        s = SubMap(10,10,5)
        from tile import Tile 
        t = Tile((5,9,0),2,collisionEnabled=False,buildingInternal=True,roofType=2)
        for x in range(10):
            for y in range(10):
                newTile = Tile(pos=(x,y,0),type_id=0,collisionEnabled=False,buildingInternal=True,roofType=1)
                if x == 0 or x == 9 or y == 0 or y == 9:
                    newTile.buildingInternal = False
                    newTile.type_id = 1
                    newTile.collisionEnabled = True
                s.addTile(newTile)
        for x in range(10):
            for y in range(10):
                newTile = Tile(pos=(x,y,1),type_id=5,collisionEnabled=False,buildingInternal=True,roofType=1)
                if x == 0 or x == 9 or y == 0 or y == 9:
                    newTile.buildingInternal = False
                    newTile.type_id = 1
                    newTile.collisionEnabled = True
                s.addTile(newTile)
        s.addTile(t)
        stair = Stair()
        stair.pos = (1,2,0)
        stair.collisionEnabled=True
        stair.buildingInternal=True
        stair.roofType=1
        stair.type_id = 4
        stair2 = Stair()
        stair2.pos = (4,2,1)
        stair2.collisionEnabled=True
        stair2.buildingInternal=True
        stair2.roofType=1
        stair2.type_id = 4
        stair2.isUp = False
        s.addTile(stair2)
        s.addTile(stair)
        s.toFile()
        MapManager.activeMap.submaps.append(s)

    def on_escape(self):
        Saves.store(self.pc)
        utils.set_scene(
            Menu()
        )
        SoundEngine.stopAllSounds()
        #sys.exit()

    def update(self):
        keys = pygame.key.get_pressed()
        subMaps = MapManager.activeMap.submaps
        self.pc.update(keys, subMaps)
        for npc in self.npcs:
            if npc.__class__.__name__ is "Enemy":
                npc.update(self.pc.fPos)
            elif npc.__class__.__name__ is "Friendly":
                npc.update()
            elif npc.__class__.__name__ is "Trader":
                npc.update(self.pc.inventory, self.UIManager)
        self.UIManager.update()
        Camera.update()

    def blit(self):
        Camera.blitView()
        for npc in self.npcs:
            npc.blit(utils.screen)
        self.pc.blit(utils.screen)
        self.UIManager.blit(utils.screen, (0,0))