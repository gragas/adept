import pygame
from buffalo import utils
from inventoryUI import InventoryUI

class HotbarUI:

	BUTTON_SIZE = 32
	PADDING = 6

	def __init__(self,inventory, manager):
		self.inventory = inventory
		self.resetSurface()
		self.pos = (utils.SCREEN_W / 2 - self.surface.get_width() / 2, utils.SCREEN_H - self.surface.get_height() - 10)
		self.itemRects = list()
		self.guiManager = manager
		self.selectedIndex = 0

	def resetSurface(self):
		self.surface = utils.empty_surface((self.inventory.INV_SIZE_X * (InventoryUI.BUTTON_SIZE + InventoryUI.PADDING) + InventoryUI.PADDING,
			1 * (InventoryUI.BUTTON_SIZE + InventoryUI.PADDING) + InventoryUI.PADDING))
		self.surface.fill((100,100,100,255))

	def getGUIPosFromItemPos(self, pos):
		newX = (pos[0] * (InventoryUI.BUTTON_SIZE + InventoryUI.PADDING)) + InventoryUI.PADDING
		newY = (pos[1] * (InventoryUI.BUTTON_SIZE + InventoryUI.PADDING)) + InventoryUI.PADDING
		return (newX, newY)

	def getItemPosFromMousePos(self, pos):
		relPos = (pos[0] - self.pos[0], pos[1] - self.pos[1])
		itemX = int((relPos[0] - InventoryUI.PADDING) / (InventoryUI.BUTTON_SIZE + InventoryUI.PADDING))
		itemY = int((relPos[1] - InventoryUI.PADDING) / (InventoryUI.BUTTON_SIZE + InventoryUI.PADDING))
		return (itemX, itemY)

	def update(self):
		self.resetSurface()
		for x in range(0,self.inventory.INV_SIZE_X):
			iSurface = utils.empty_surface((InventoryUI.BUTTON_SIZE,InventoryUI.BUTTON_SIZE))
			#Default color
			iSurface.fill((0,0,0,100))

			#Blit surface (default to empty surface)
			if x == self.inventory.hotbarSelection:
				selectedSurface = utils.empty_surface((self.surface.get_height()-8, self.surface.get_height()-8))
				selectedSurface.fill((255,0,0,255))
				self.surface.blit(selectedSurface, (self.getGUIPosFromItemPos((x,0))[0] - 2,self.getGUIPosFromItemPos((x,0))[1] - 2))
				if self.inventory.hotbar[x] is not None:
					backgroundSurface = utils.empty_surface((InventoryUI.BUTTON_SIZE,InventoryUI.BUTTON_SIZE))
					backgroundSurface.fill((0,0,0,100))
					self.surface.blit(backgroundSurface, self.getGUIPosFromItemPos((x,0)))

			#Load item icons from inventory
			if self.inventory.hotbar[x] != None:
				iSurface = self.inventory.hotbar[x].surface

			self.surface.blit(iSurface, self.getGUIPosFromItemPos((x,0)))

	def getItemFromGUIPos(self, pos):
		for x in range(0,self.inventory.INV_SIZE_X):
			if self.inventory.hotbar[x] != None:
				itemRect = pygame.Rect(self.getGUIPosFromItemPos((x,0)), (InventoryUI.BUTTON_SIZE,InventoryUI.BUTTON_SIZE))
				if itemRect.collidepoint(pos):
					return self.inventory.hotbar[x]
		return None

	def mouseDown(self,pos):
		if self.guiManager.draggedItem == None:
			item = self.getItemFromGUIPos(pos)
			self.guiManager.draggedItem = item
			self.inventory.removeHotbarItem(item)
		else:
			#Replaced by item at location, else None
			self.guiManager.draggedItem = self.inventory.placeItemInHotbar(self.guiManager.draggedItem, self.getItemPosFromMousePos(pygame.mouse.get_pos()))
		self.update()

	def handleKeyboardPress(self, keys):
		if keys[pygame.K_1]:
			self.inventory.hotbarSelection = 0
			self.update()
			return True
		if keys[pygame.K_2]:
			self.inventory.hotbarSelection = 1
			self.update()
			return True
		if keys[pygame.K_3]:
			self.inventory.hotbarSelection = 2
			self.update()
			return True
		if keys[pygame.K_4]:
			self.inventory.hotbarSelection = 3
			self.update()
			return True
		if keys[pygame.K_5]:
			self.inventory.hotbarSelection= 4
			self.update()
			return True
		if keys[pygame.K_6]:
			self.inventory.hotbarSelection = 5
			self.update()
			return True
		if keys[pygame.K_7]:
			self.inventory.hotbarSelection = 6
			self.update()
			return True
		if keys[pygame.K_8]:
			self.inventory.hotbarSelection = 7
			self.update()
			return True
		if keys[pygame.K_9]:
			self.inventory.hotbarSelection = 8
			self.update()
			return True
		if keys[pygame.K_0]:
			self.inventory.hotbarSelection = 9
			self.update()
			return True

	def blit(self, dest, pos):
		dest.blit(self.surface, pos)
