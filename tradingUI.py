import pygame
import os
from buffalo import utils
from item import Item

# User interface for trading with NPCs
# Similar to the crafting UI, with some minor differences
# The biggest thing is that it only appears when you "talk to" (read click on)
# A trader NPC and disappears when you leave that window, and only contains a 
# Limited number of trades

class TradingUI:

	BUTTON_SIZE = 32
	PADDING = 6

	def __init__(self, inventory, tradeSet):
		self.tradeSet = tradeSet
		self.inventory = inventory
		self.surface = utils.empty_surface((228,500))
		self.surface.fill((100,100,100,100))
		self.pos = (utils.SCREEN_W / 2 + self.surface.get_width() / 2 + 350, utils.SCREEN_H / 2 - 150)
		self.tileRects = list()
		self.tileTrades = list()
		self.updateTradeTable()

	def updateTradeTable(self):
		self.surface = utils.empty_surface((228,500))
		self.surface.fill((100,100,100,100))
		self.tileRects = list()
		self.tileTrades = list()
		tradeTiles = list()
		total_y = 0
		for t in self.tradeSet:
			newTile = self.generateTradeTile(t)
			tradeTiles.append(newTile)
			self.tileRects.append(pygame.Rect(0, total_y, newTile.get_width(), newTile.get_height()))
			self.tileTrades.append(t)
			total_y += newTile.get_height()
		newSurface = utils.empty_surface((228, total_y))
		newSurface.fill((100,100,100,255))
		currY = 0
		for surf in tradeTiles:
			newSurface.blit(surf, (0, currY))
			currY += surf.get_height()
		self.surface = newSurface

	def generateTradeTile(self, trade):
		y_length = 36 * (len(trade.price.keys()) / 3) + 78;
		newScreen = utils.empty_surface((228, y_length))

		for num, item in enumerate(trade.price.keys()):
			x = ((num % 3) * TradingUI.BUTTON_SIZE) + TradingUI.PADDING
			y = ((num / 3) * TradingUI.BUTTON_SIZE) + TradingUI.PADDING
			itemSurface = pygame.Surface.copy(Item(item, quantity = trade.price[item]).surface)
			if self.inventory.getTotalItemQuantity(item) < trade.price[item]:
				itemSurface.fill(pygame.Color(255,0,0,250)[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)
			newScreen.blit(itemSurface, (x,y))

		for num, item in enumerate(trade.goods.keys()):
			x = 192 - (((num % 2) * TradingUI.BUTTON_SIZE) + TradingUI.PADDING)
			y = ((num / 2) * TradingUI.BUTTON_SIZE) + TradingUI.PADDING
			newScreen.blit(Item(item, quantity = trade.goods[item]).surface, (x,y))

		path = os.path.join(os.path.join(*list(['assets'] + ['items'] + ["arrow.png"])))
		arrowSurface = pygame.image.load(path)
		newScreen.blit(arrowSurface,(114, (newScreen.get_height() / 2) - arrowSurface.get_height() / 2))

		myfont = pygame.font.SysFont("monospace", 15)
		color = (255,255,0)
		if not trade.canTrade(self.inventory):
			color = (255,0,0)
		label = myfont.render(str(trade.name), 1, color)
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
				 clickedTrade = self.tileTrades[self.tileRects.index(tile)]
				 if not clickedTrade.canTrade(self.inventory):
				 	return
				 for item in clickedTrade.price.keys():
				 	self.inventory.removeItemQuantity(item, clickedTrade.price[item])
				 for item in clickedTrade.goods.keys():
				 	newItem = Item(item)
				 	newItem.quantity = clickedTrade.goods[item]
				 	self.inventory.addItem(newItem)
				 self.inventory.update()
				 self.updateTradeTable()
				 return
