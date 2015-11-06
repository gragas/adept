from item import Item
import pygame
import unittest
from buffalo import utils
import random

utils.init()

class TestItem:
    def test_init(self):   
        i = Item("axe")
        assert i.name == "axe"
        assert i.quantity == 1

    def test_unknown_item(self):
    	i = Item(str(random.random))
    	assert i.surface is not None