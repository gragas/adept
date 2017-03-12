import os, re

from mapManager import MapManager

class Map:
    def __init__(self, name, BASE_PATH_LIST):
        self.name = name
        self.BASE_PATH_LIST = BASE_PATH_LIST
        self.pathlist = MapManager.BASE_PATH + [self.name,]
        self.path = os.path.join(*self.pathlist)
        self.precedence = 0
        self.seed = 0
        path = os.path.join(*list(self.pathlist + ["properties.txt"]))
        if not os.path.isfile(path):
            print ("[Map] Error: No properties.txt found at \"" + path + "\". Creating an empty one.")
            if not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            with open(path, 'w+') as pfile:
                pass
        with open(os.path.join(*list(MapManager.BASE_PATH + [self.name, "properties.txt"]))) as mfile:
            for line in mfile:
                words = line.split()
                if len(words) >= 2:
                    if words[0] == "precedence":
                        try:
                            self.precedence = int(words[1])
                        except:  # If the second word can't be converted to an int
                            pass # Then don't do anything; keep precedence of 0
                    if words[0] == "seed":
                        try:
                            self.seed = float(words[1])
                        except:
                            pass
        self.loadChunkFiles()

    def loadChunkFiles(self):
        LOAD_PATH = self.pathlist + ["chunks"]
        if not os.path.exists(os.path.join(*LOAD_PATH)):
            print("[Map] Error: No chunks folder found. Creating an empty one.")
            os.makedirs(os.path.join(*LOAD_PATH))
        files = [f for f in os.listdir(os.path.join(*LOAD_PATH)) if os.path.isfile(os.path.join(*list(LOAD_PATH + [f])))]
        self.chunk_files = [os.path.join(*list(LOAD_PATH + [f])) for f in files if len(f) >= 9 and f[-6:] == ".chunk"]

#    def isChunkLoaded(self, x, y):
#        for chunkFile in self.chunk_files:
#            parsedName = re.split(r'\s+|[,.]\s*', chunkFile)
#            if parsedName[0] == str(x) and parsedName [1] == str(y):
#                return True
#        return False

#    def loadChunk(self, chunkx, chunky):
#        #Search loaded chunks to see if the desired chunk already exists
#        for chunkFile in self.chunk_files:
#            parsedName = re.split(r'\s+|[,.]\s*', chunkFile)
#            if parsedName[0] == str(chunkx) and parsedName [1] == str(chunky):
#                loadedChunk = Chunk(chunkx, chunky)
#                loadedChunk.path = chunkFile
#                loadedChunk.fromFile(chunkx, chunky)
#                return loadedChunk
#        #If the desired chunk does not exist, tell Chunk to create one
#        genChunk = Chunk(chunkx, chunky)
#        genChunk.generateDataAndDefs()
#        genChunk.toFile()
#        self.loadChunks()
#        return Chunk(chunkx,chunky)
