import math
import random

import pygame

from buffalo import utils

from npc import NPC

class Enemy(NPC):

    # Class for anything hostile. For now it just follows the player around,
    # There's not enough in the game in terms of health, damage, and item usage
    # To have actual combat

    def __init__(self, name=None, fPos=None, **kwargs):
        speed = kwargs.get("speed") if kwargs.get("speed") is not None else .05
        NPC.__init__(self, name=name, fPos=fPos, speed=speed, spawn=kwargs.get("spawn"))
        self.enemyList+=self

    def update(self, target):
        # If it's close enough to the player it won't move
        # If it's too far away it will stop trying
        if self.fPos[0] != target[0] and math.hypot(self.fPos[1]-target[1], self.fPos[0]-target[0]) > 32 and math.hypot(self.fPos[1]-target[1], self.fPos[0]-target[0]) < 600:
            # Some fancy trig to get the direction it needs to go to follow the player
            angle = math.atan((self.fPos[1]-target[1])/(self.fPos[0]-target[0]))
            if self.fPos[0] - target[0] > 0:
                angle = math.pi + angle
            self.move(angle)
        else:
            self.move(None)

        NPC.update(self)
        NPC.detectCollision(self, self.enemyList)
