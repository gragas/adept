import os
from recipe import Recipe

class RecipeManager:
	RECIPES = list()

	@staticmethod
	def loadRecipes():
		RecipeManager.RECIPES = list()
		files =  os.listdir(os.path.join(*list(Recipe.BASE_PATH)))
		for f in files:
			if(f.split('.')[0] != ""):
				newRecipe = Recipe(f.split('.')[0])
				RecipeManager.RECIPES.append(newRecipe)