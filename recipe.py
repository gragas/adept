from item import Item
import yaml
import os

class Recipe():
    BASE_PATH = ["recipes"]

    def __init__(self,name):
        self.name = name
        self.info = dict()
        #Parse YML
        RECIPE_FILE = os.path.join(os.path.join(*list(Recipe.BASE_PATH + [name + ".yml"])))
        try:
            with open(RECIPE_FILE, "r") as iFile:
                self.info = yaml.load(iFile.read())

                #Load recipe attributes
                self.components = self.info["components"]
                self.requirements = self.info["requirements"]
                self.products = self.info["products"]
        except Exception as e:
            print("Error: Problem with recipe: " + self.name + "\n")
            print(e)

    def recipeUnlocked(self):
        """
        Eventually, the player should only see recipes that they have the stats to be able to craft.
        """
        return True

    def canCraft(self, inventory):
        """
        Checks to see if the player has the correct items in their inventory and is at the right crafting location
        """
        # if self.requirements["tool"] != "" and self.requirements["tool"] != station_type:
        #     return false

        for item in self.components.keys():
            if inventory.getTotalItemQuantity(item) < self.components[item]:
                return False
        #TODO: Also do a check for character's skills
        return True
        
