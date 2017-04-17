from buffalo import utils
from craftingUI import CraftingUI
from inventory import Inventory
from recipe import Recipe
from recipeManager import RecipeManager
from item import Item

utils.init()

def test_init():
	i = Inventory()
	c = CraftingUI(i)
	assert c.inventory == i
	assert len(c.tileRects) == len(RecipeManager.RECIPES)
	assert len(c.tileRecipes) == len(RecipeManager.RECIPES)

def test_fail_recipe():
	i = Inventory()
	c = CraftingUI(i)
	r = RecipeManager.getRecipe("pickaxe")
	assert r.canCraft(i) == False

def test_success_recipe():
	i = Inventory()
	c = CraftingUI(i)
	i.addItem(Item("stick",quantity=1))
	i.addItem(Item("stone",quantity=5))
	r = RecipeManager.getRecipe("pickaxe")
	assert r.canCraft(i) == True
	
