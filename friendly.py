import math
import random

import pygame

from buffalo import utils

from npc import NPC

# Overarching class for all Friendly NPCs. For now they just move randomly

class Friendly(NPC):

    def __init__(self, name=None, fPos=None, speed=None, **kwargs):
        speed = speed if speed is not None else .05
        NPC.__init__(self, name=name, fPos=fPos, speed = speed, spawn=kwargs.get("spawn"))
        self.currentDirection = random.random() * 2 * math.pi
        self.friendlyList+=self

    def update(self):
        self.currentDirection += random.random() * .5 - .25
        self.move(self.currentDirection)
        NPC.update(self)
        NPC.detectCollision(self, self.friendlyList)