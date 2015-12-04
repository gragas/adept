from mapManager import MapManager
from buffalo import utils
#from nose.tools import with_setup

utils.init()

isLoaded = False

MapManager.loadMaps()
MapManager.soft_load((0, 0))
MapManager.hard_load((1, 1))


MapManager.get_soft_load_reader_thread()
MapManager.soft_load_reader()
MapManager.offload_old_chunks()

isLoaded = True
assert isLoaded
