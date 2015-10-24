from serializable import Serializable
from buffalo import utils
from subMap import SubMap
from mapManager import MapManager

import os
import pygame

class Tile(Serializable,object):
    LOADED_SURFACES = dict()
    def __init__(self,pos=(0,0,0),type_id=0,collisionEnabled=False,buildingInternal=False,roofType=0,heightLevel=0,**kwargs):
        self.pos = pos
        self.type_id = type_id
        self.surface = utils.empty_surface((SubMap.TILE_SIZE,SubMap.TILE_SIZE))
        self.collisionEnabled = collisionEnabled
        self.buildingInternal=buildingInternal
        self.roofType=roofType
        self.inside=False
        self.heightLevel=heightLevel
        self.render()

    def render(self):
        renderID = self.type_id
        if self.buildingInternal and not self.inside:
            renderID = self.roofType
        self.surface = Tile.loadSurfaceForId(renderID)

    def onCollision(self,pc=None):
        pass

    @staticmethod
    def loadSurfaceForId(_id):
        if _id in Tile.LOADED_SURFACES.keys():
            return Tile.LOADED_SURFACES[_id]
        IMG_FILE = os.path.join(os.path.join(*list(['tiles','assets'] + [str(_id) + ".png"])))
        try:
            surface = pygame.image.load(IMG_FILE)
            Tile.LOADED_SURFACES[_id] = surface
            return surface
        except Exception as e:
            print("Error: Tile image for item \"" + str(_id) + "\" does not exist.")
            print(e)
            IMG_FILE = os.path.join(os.path.join(*list(['tiles','assets'] + ["error.png"])))
            surface = pygame.image.load(IMG_FILE)
            Tile.LOADED_SURFACES[_id] = surface
            return surface
