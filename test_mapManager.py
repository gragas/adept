from mapManager import MapManager
from buffalo import utils
#from nose.tools import with_setup

utils.init()

isLoaded = False

MapManager.loadMaps()
MapManager.soft_load(0)
MapManager.hard_load(1)

for c in MapManager.loaded_chunks:
    MapManager.get_soft_load_reader_thread()
    MapManager.soft_load_reader()
    MapManager.offload_old_chunks()

isLoaded = True
assert isLoaded
