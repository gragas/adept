from buffalo import utils
from recipeManager import RecipeManager
from nose.tools import with_setup
import pygame


def init():
	utils.init()

def teardown():
	utils.end = True
	pygame.quit()

@with_setup(init,teardown)
def test_manager():
	RecipeManager.loadRecipes()
	assert len(RecipeManager.RECIPES) > 0
	
