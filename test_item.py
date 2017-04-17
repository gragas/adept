from item import Item
import pygame
import unittest
from buffalo import utils
import random

utils.init()

class TestItem:
    def test_init(self):   
        i = Item("test")
        assert i.name == "test"
        assert i.quantity == 1
    	#assert i.info["maxQuantity"] == 99

    def test_unknown_item(self):
    	i = Item(str(random.random))
    	assert i.surface is not None

    def test_item_types(self):
    	from item import ItemType
    	assert ItemType.WEAPON == 0
    	assert ItemType.TOOL == 1
    	assert ItemType.QUEST == 2
    	assert ItemType.ARMOR == 3
    	assert ItemType.RESOURCE == 4

    def test_item_render(self):
    	i = Item("test")
    	i.renderItemQuantity()
    	
