import pygame
from buffalo import utils
from recipeManager import RecipeManager
from item import Item
import pygame
import os

class CraftingUI:

    BUTTON_SIZE = 32
    PADDING = 6

    def __init__(self, inventory):
        self.inventory = inventory
        self.surface  = utils.empty_surface((228,500))
        self.surface.fill((100,100,100,100))
        self.pos = (utils.SCREEN_W / 2 - self.surface.get_width() / 2 - 350, utils.SCREEN_H / 2 - 150)
        self.tileRects = list()
        self.tileRecipes = list()
        self.updateRecipeTable()

    def updateRecipeTable(self):
        self.surface  = utils.empty_surface((228,500))
        self.surface.fill((100,100,100,100))
        self.tileRects = list()
        self.tileRecipes = list()
        recipeTiles = list()
        total_y = 0
        RecipeManager.loadRecipes()
        for r in RecipeManager.RECIPES:
            newTile = self.generateRecipeTile(r)
            recipeTiles.append(newTile)
            self.tileRects.append(pygame.Rect(0,total_y, newTile.get_width(), newTile.get_height()))
            self.tileRecipes.append(r)
            total_y += newTile.get_height()
        newSurface = utils.empty_surface((228, total_y))
        newSurface.fill((100,100,100,255))
        currY = 0
        for surf in recipeTiles:
            newSurface.blit(surf, (0, currY))
            currY += surf.get_height()
        self.surface = newSurface


    def generateRecipeTile(self, recipe):
        y_length = 36 * (len(recipe.components.keys()) / 3) + 78;
        newScreen = utils.empty_surface((228, y_length))
        """
        Components Rendering
        """
        for num, item in enumerate(recipe.components.keys()):
            x = ((num % 3) * CraftingUI.BUTTON_SIZE) + CraftingUI.PADDING
            y = (((num / 3)) * CraftingUI.BUTTON_SIZE) + CraftingUI.PADDING
            itemSurface = pygame.Surface.copy(Item(item, quantity=recipe.components[item]).surface)
            #Shade items red if they aren't available for recipe
            if self.inventory.getTotalItemQuantity(item) < recipe.components[item]:
                itemSurface.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
                itemSurface.fill(pygame.Color(255,0,0,250)[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)
            newScreen.blit(itemSurface, (x,y))
        """
        Products Rendering
        """
        for num, item in enumerate(recipe.products.keys()):
            x =  192 - (((num % 2) * CraftingUI.BUTTON_SIZE) + CraftingUI.PADDING)
            y = (((num / 2)) * CraftingUI.BUTTON_SIZE) + CraftingUI.PADDING
            newScreen.blit(Item(item, quantity=recipe.products[item]).surface, (x,y))
        """
        Arrow Rendering
        """
        path = os.path.join(os.path.join(*list(Item.BASE_PATH +  ['assets'] + ["arrow.png"])))
        arrowSurface = pygame.image.load(path)
        newScreen.blit(arrowSurface,(114, (newScreen.get_height() / 2) - arrowSurface.get_height() / 2))
        """
        Label Rendering
        """
        myfont = pygame.font.SysFont("monospace", 15)
        color = (255,255,0)
        if not recipe.canCraft(self.inventory):
            color = (255,0,0)
        label = myfont.render(str(recipe.name), 1, color)
        newScreen.blit(label, (newScreen.get_width() - label.get_width() - 2, newScreen.get_height() - label.get_height() - 2))

        pygame.draw.rect(newScreen, (0,0,0,255), pygame.Rect(0,0,228, y_length), 1)
        return newScreen

    def blit(self, dest, pos):
        dest.blit(self.surface, pos)

    def update(self):
        pass

    def mouseDown(self, pos):
        for tile in self.tileRects:
            if(tile.collidepoint(pos)):
                clickedRecipe =  self.tileRecipes[self.tileRects.index(tile)]
                if not clickedRecipe.canCraft(self.inventory):
                    return
                for item in clickedRecipe.components.keys():
                    self.inventory.removeItemQuantity(item, clickedRecipe.components[item])
                for item in clickedRecipe.products.keys():
                    newItem = Item(item)
                    newItem.quantity = clickedRecipe.products[item]
                    self.inventory.addItem(newItem)
                self.inventory.update()
                self.updateRecipeTable()
                return
