from inventory import Inventory
from item import Item
import pygame
import unittest
from buffalo import utils
import os

utils.init(
            caption='Adept',
            fullscreen=True
        )

class TestCharacter:
    def init(self):
        from createCharacter import CreateCharacter
        self.c = CreateCharacter()

    def tear_down(self):
        pass

    def test_creation(self):
        self.init()

    def test_saveing(self):
        self.init()
        self.c.characterName.label.text = "Test"
        self.c.create_character()
        assert os.path.isfile(os.path.join("characters","Test")) is True
        if os.path.isfile(os.path.join("characters","Test")) is True:
            os.remove(os.path.join("characters","Test"))
        if len(os.listdir(os.path.join("characters"))) is 0:
            os.rmdir(os.path.join(os.path.join("characters")))

    def test_surface(self):
        from playerCharacter import PlayerCharacter
        char = PlayerCharacter()
        assert char.surface is not None

    def test_inventory_pc_reference(self):
        from playerCharacter import PlayerCharacter
        char = PlayerCharacter()
        assert char.inventory.playerCharacter() == char

    def test_serialize(self):
        from playerCharacter import PlayerCharacter
        from serializable import Serializable
        char = PlayerCharacter()
        j = char.serialize()
        decoded = Serializable.deserialize(j)
        assert char.name == decoded.name
        assert decoded.inventory is not None
        assert decoded.surface is not None
