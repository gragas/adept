from enum import Enum
from buffalo import utils
import yaml
import os
import random

class Item():
    BASE_PATH = ["items"]

    def __init__(self,name,quantity=0,durability=1.0,**kwargs):
        """
        Static item information
        """
        self.name = name
        info = dict() #yaml files messed up json serialization, works as long as it's not a self. variable

        ITEM_FILE = os.path.join(os.path.join(*list(Item.BASE_PATH + [self.name + ".yml"])))
        try:
            with open(ITEM_FILE, "r") as iFile:
                info = yaml.load(iFile.read())
        except Exception as e:
            print("Error: Item " + str(_id) + " does not exist.")

        """
        Special Values per Type:
        ------------------------
            - Weapon:
                -Base Damage
                -Base Attack Speed
                -Durability per Use
                -Critical Chance
                -Critical Multiplier
            - Tool:
                -Base Damage
                -Base Attack Speed
                -Durability per Use
            - Quest:
                -Quest ID
            - Armor:
                -Body Part
                -Base Protection
            - Resource:
                -Resource Type
        ------------------------
        """

        """
        Instance variables
        """
        self.quantity = quantity
        self.durability = durability
        self.instanceID = random.random()
        self.surface = utils.empty_surface((35,35))
        self.surface.fill((random.random() * 255, random.random() * 255, random.random() * 255, 255))

class ItemType(Enum):
    WEAPON = 0
    TOOL = 1
    QUEST = 2
    ARMOR = 3
    RESOURCE = 4
    MISC = 5
