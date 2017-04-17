import pygame

from buffalo import utils

from friendly import Friendly
from trade import Trade
from tradingUI import TradingUI
from npc import NPC
from camera import Camera

# Extension of friendly NPCs, offers items in exchange for other items. Makes the
# trade window appear when you click on him

class Trader(Friendly):
	def __init__(self, **kwargs):
		self.trades = [Trade("axe"), Trade("potion")]
		Friendly.__init__(self, name=kwargs.get("name"), fPos=kwargs.get("fPos"), speed=kwargs.get("speed"), spawn=kwargs.get("spawn"))
		self.active = False
		self.tradeUI = None

	def update(self, inventory, manager):
		if self.tradeUI is None:
			self.tradeUI = TradingUI(inventory, self.trades)

		if pygame.mouse.get_pressed()[0] and not self.active:
			traderRect = pygame.Rect(self.pos, self.size)
			mousePos = pygame.mouse.get_pos()
			mousePos = (mousePos[0] + Camera.pos[0], mousePos[1] + Camera.pos[1])
			if traderRect.collidepoint(mousePos):
				manager.active = True
				manager.registerGUI(self.tradeUI)
				self.active = True

		keys = pygame.key.get_pressed()
		if keys[pygame.K_e] and self.active:
			manager.deregisterGUI(self.tradeUI)
			self.active = False
			self.tradeUI = None
			
