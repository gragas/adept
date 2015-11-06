import pygame

from buffalo import utils

from chunk import Chunk
from mapManager import MapManager

class Camera:
    """
    Manages what is drawn on the screen
    and how it is drawn
    """

    zoom = 1.0
    pos  = 0, 0
    fPos = float(pos[0]), float(pos[1])
    locked = False
    marker = fPos # marker represents the last position at which chunks were loaded
    c_offset = 0, 0 # represents the (x, y) tuple last passed to MapManager.loadChunks(...)

    @staticmethod
    def init():
        """
        TODO: Fix mapManager / Camera link so that chunks are dynamically loaded
        """
        for row in range(MapManager.LC_HEIGHT):
            for col in range(MapManager.LC_WIDTH):
                x, y = col - MapManager.LC_WIDTH // 2, row - MapManager.LC_HEIGHT // 2
                MapManager.loadedChunks[row][col] = Chunk(x, y)

    @staticmethod
    def lock(character):
        """
        Lock the camera to a Character
        """
        Camera.locked = True
        Camera.character = character
        Camera.update()
        

    @staticmethod
    def update():
        if Camera.locked:
            x, y = Camera.character.fPos
            x, y = x - utils.SCREEN_W // 2, y - utils.SCREEN_H // 2
            Camera.updatePos((x, y))
        if utils.dist(Camera.fPos, Camera.marker) > (Chunk.CHUNK_WIDTH * Chunk.TILE_SIZE / 3):
            x, y = Camera.character.fPos
            x = int(x // (Chunk.TILE_SIZE * Chunk.CHUNK_WIDTH))
            y = int(y // (Chunk.TILE_SIZE * Chunk.CHUNK_HEIGHT))            
            MapManager.loadChunks(x, y)
            Camera.marker = Camera.fPos
        

    @staticmethod
    def updatePos(fPos):
        """
        The argument passed MUST be a tuple of two floating-point values
        """
        Camera.fPos = fPos
        Camera.pos = int(Camera.fPos[0]), int(Camera.fPos[1])
        # if fPos is somewhere where must load chunks
        # then load the chunks

    @staticmethod
    def blitView():
        #Blits chunks
        rmult = Chunk.TILE_SIZE * Chunk.CHUNK_HEIGHT
        cmult = Chunk.TILE_SIZE * Chunk.CHUNK_WIDTH
        for rowindx, row in enumerate(MapManager.loadedChunks):
            for colindx, chunk in enumerate(row):
                x = colindx - MapManager.LC_WIDTH // 2 + Camera.c_offset[0]
                y = rowindx - MapManager.LC_HEIGHT // 2 + Camera.c_offset[1]
                chunk.blit(
                    utils.screen,
                    (cmult * x - Camera.pos[0], rmult * y - Camera.pos[1])
                )
        
        #Blits submaps
        for submap in MapManager.activeMap.submaps:
            submap.blit(utils.screen, (submap.pos[0] - Camera.pos[0], submap.pos[1] - Camera.pos[1]))
