from serializable import Serializable
from buffalo import utils
from subMap import SubMap
from mapManager import MapManager
from chunk import Chunk

import os
import pygame

class Tile(Serializable, object):
    LOADED_SURFACES = dict()
    def __init__(
            self,
            pos=(0,0,0),
            type_id=0,
            collisionEnabled=False,
            buildingInternal=False,
            roofType=0,
            heightLevel=0,
            **kwargs
    ):
        self.pos = pos
        self.type_id = type_id
        self.surface = utils.empty_surface((SubMap.TILE_SIZE,SubMap.TILE_SIZE))
        self.collisionEnabled = collisionEnabled
        self.buildingInternal=buildingInternal
        self.roofType=roofType
        self.inside=False
        self.heightLevel=heightLevel
        self.use_images = kwargs.get('use_images') if kwargs.get('use_images') is not None else True
        self.base_color = kwargs.get('base_color') if kwargs.get('base_color') is not None else (100, 180, 0, 255)
        self.mean_temp = kwargs.get('mean_temp') if kwargs.get('mean_temp') is not None else 70 # degrees Fahrenheit
        self.var_temp = kwargs.get('var_temp') if kwargs.get('var_temp') is not None else 10 # degrees Fahrenheit
        self.mean_hum = kwargs.get('mean_hum') if kwargs.get('mean_hum') is not None else 0.3 # percent / 100
        self.var_hum = kwargs.get('var_hum') if kwargs.get('var_hum') is not None else 0.1 # percent / 100
        self.mean_nc = kwargs.get('mean_nc') if kwargs.get('mean_nc') is not None else 100 # grams
        self.var_nc = kwargs.get('var_nc') if kwargs.get('var_nc') is not None else 50 # grams
        self.render()

    def render(self):
        if self.use_images:
            renderID = self.type_id
            if self.buildingInternal and not self.inside:
                renderID = self.roofType
            self.surface = Tile.loadSurfaceForId(renderID)
        else:
            self.surface = utils.empty_surface((32, 32))
            self.surface.fill(self.base_color)

    def onCollision(self,pc=None):
        pass

    @staticmethod
    def loadSurfaceForId(_id):
        if _id in Tile.LOADED_SURFACES.keys():
            return Tile.LOADED_SURFACES[_id]
        IMG_FILE = os.path.join(os.path.join(*list(['assets','tiles'] + [str(_id) + ".png"])))
        try:
            surface = pygame.image.load(IMG_FILE)
            Tile.LOADED_SURFACES[_id] = surface
            return surface
        except Exception as e:
            print("Error: Tile image for item \"" + str(_id) + "\" does not exist.")
            print(e)
            IMG_FILE = os.path.join(os.path.join(*list(['assets'] + ["error.png"])))
            surface = pygame.image.load(IMG_FILE)
            Tile.LOADED_SURFACES[_id] = surface
            return surface
