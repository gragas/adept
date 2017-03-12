import os

class MapManager:
    """
    Manages chunks and map loading
    """

    BASE_PATH    = ["maps"] # BASE_PATH is a list version of the base path in
                            # which MapManager will search for chunks. For example,
                            # if the base path should be maps/otherfolder/ then
                            # BASE_PATH should equal ["maps", "otherfolder"]
    maps          = []      # Maps is a list of all Map's found in within BASE_PATH
    activeMap     = None    # activeMap is the active map // lol

    loadedChunks  = [[None]*5 for _ in range(5)]

    # LC_WIDTH and LC_HEIGHT are the maximum width and height
    # of loadedChunks, which contains Chunk's loaded into memory
    LC_WIDTH      = len(loadedChunks[0])
    LC_HEIGHT     = len(loadedChunks)

    @staticmethod
    def loadMaps():
        """
        loadMaps loads all the maps that are checked in the plugins manager file
        """
        for name in PluginManager.mapNames:
            MapManager.loadMap(name)
        MapManager.maps.sort(key=lambda m: m.precedence)
        MapManager.activeMap = MapManager.maps[0]

    @staticmethod
    def loadMap( map_name ):
        """
        loadMap takes one string map_name and attempts to load the corresponding map
        """
        CHUNK_PATH_LIST = MapManager.BASE_PATH + [map_name, "chunks"]
        MapManager.maps.append(Map(map_name, CHUNK_PATH_LIST))

    # Reloads loaded chunks in grid around central chunk (inputs use chunk coordinates)
    @staticmethod
    def loadChunks(centralx, centraly):
        ybegin = centraly - int(MapManager.LC_HEIGHT/2)
        yend   = centraly + int(MapManager.LC_HEIGHT/2)
        xbegin = centralx - int(MapManager.LC_WIDTH/2)
        xend   = centralx + int(MapManager.LC_WIDTH/2)
        for LCy, chunky in enumerate(range(ybegin, yend)):
            for LCx, chunkx in enumerate(range(xbegin, xend)):
                MapManager.loadedChunks[LCy][LCx] = Chunk(chunkx, chunky)
        camera.Camera.c_offset = centralx, centraly
        

from Map import Map
from pluginManager import PluginManager
from chunk import Chunk
import camera