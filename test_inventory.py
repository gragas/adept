from buffalo import utils
from inventory import Inventory
from item import Item
from eventRegistry import EventRegistry
import random

class TestInventory:
	def __init__(self):
		self.called = False

	def test_init(self):
		i = Inventory()
		assert len(i.items) == 10
		assert len(i.items[0]) == 3
		assert i.hotbarSelection == 0

	def test_add_item(self):
		i = Inventory()
		print 1
		t = Item("test")
		print 2
		i.addItem(t)
		print 3
		assert i.hotbar[0] == t
		for x in range(100):
			i.addItem(Item(str(random.random())))
		assert i.items[0][0] is not None
		assert i.items[9][2] is not None

	def test_instantiation(self):
		i = Inventory()
		d = Inventory()
		assert i != d
		assert i.hotbar is not d.hotbar
		assert i.items is not d.items

	def remListener(self,event):
		self.called = True

	def test_rem_item(self):
		EventRegistry.registerListener(self.remListener,"inv_remove_quantity")
		i = Inventory()
		t = Item("test",quantity=10)
		i.addItem(t)
		assert i.hotbar[0] == t
		i.removeItemQuantity("test",5)
		print i.hotbar[0].quantity
		assert i.hotbar[0].quantity == 5
		assert self.called == True

	def test_place_item(self):
		i = Inventory()
		t = Item("test")
		i.placeItem(t, (2,2))
		assert i.items[2][2] == t

	def test_item_quantity_total(self):
		quantity1 = int(random.random() * 10) + 1
		quantity2 = int(random.random() * 10) + 1
		t1 = Item("test", quantity1)
		t2 = Item("test", quantity2)

		i = Inventory()
		i.addItem(t1)
		i.placeItem(t2, (2,2))

		assert i.getTotalItemQuantity("test") == quantity1 + quantity2