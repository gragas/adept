from buffalo import utils
from biome import Biome
from nose.tools import with_setup
import pygame

def init():
	utils.init()

@with_setup(init)
def test_init():
	b = Biome.GenerateBiomeDefs()
	assert len(b) >= 9
	
