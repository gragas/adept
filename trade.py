from item import Item
import yaml
import os

# Pretty simple, money is exchanged for goods and services. Similar to recipes

class Trade():
	BASE_PATH = ["trades"]

	def __init__(self, name):
		self.name = name
		self.info = dict()
		TRADE_FILE = os.path.join(os.path.join(*list(Trade.BASE_PATH + [name + ".yml"])))
		try:
			with open(TRADE_FILE, "r") as iFile:
				self.info = yaml.load(iFile.read())

				self.price = self.info["price"]
				self.goods = self.info["goods"]
		except Exception as e:
			print("Error: Problem with trade: " + self.name + "\n")
			print(e)

	def canTrade(self, inventory):
		for item in self.price.keys():
			if inventory.getTotalItemQuantity(item) < self.price[item]:
				return False
		return True