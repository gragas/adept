import math
import os
import os.path

import pygame

from buffalo import utils

from camera import Camera
from character import Character

class NPC(Character):

    # Superclass for every non-player character
    # Animation is pretty much copied from PlayerCharacter (with some changes to save space)
    # The sprites are the same leafeon as the PlayerCharacter, I was just too lazy
    # To find animated sprites for anything else
    # For testing purposes, the Enemy follows you, Friendly goes around randomly, and
    # Trader just stands there

    def __init__(self, name=None, fPos=None, size=None, level=None, **kwargs):
        self.level = level if level is not None else 0
        Character.__init__(self, name=name, fPos=fPos, size=size, spawn=kwargs.get('spawn'))
        self.speed = kwargs.get('speed') if kwargs.get('speed') is not None else .1
        self.surface = utils.empty_surface(self.size)
        self.pos = int(self.fPos[0]),int(self.fPos[1])
        self.direction = None
        self.sprites = {
            "i": list(), # idle
            "r": list(), # right
            "l": list(), # left
            "u": list(), # up
            "d": list(), # down
        }
        self.load_sprites()
        self.sprite_key  = "i"
        self.sprite_indx = 0
        self.blit_sprite()
        self.sprite_counter = 0
        self.animation_delta = int((1.0 / self.speed) * 10.5)

    # General movement method for all NPCs. Takes a direction and goes
    def move(self, direction=0):
        if direction is not None:
            x, y = self.fPos
            xv = self.speed * math.cos(direction) * utils.delta
            yv = self.speed * math.sin(direction) * utils.delta
            x += xv
            y += yv
            self.fPos = x, y
            self.pos = int(self.fPos[0]),int(self.fPos[1])
            if yv > 0 and abs(yv) > abs(xv):
                self.direction = "d"
            elif xv > 0 and abs(xv) > abs(yv):
                self.direction = "r"
            elif yv < 0 and abs(yv) > abs(xv):
                self.direction = "u"
            elif xv < 0 and abs(xv) > abs(yv):
                self.direction = "l"
        else:
        	self.direction = None

    def update(self):
        if self.sprite_key is not "u" and self.direction is "u":
            self.sprite_indx = 0
            self.sprite_key = "u"
            self.blit_sprite()
        elif self.sprite_key is not "d" and self.direction is "d":
            self.sprite_indx = 0
            self.sprite_key = "d"
            self.blit_sprite()
        elif self.sprite_key is not "l" and self.direction is "l":
            self.sprite_indx = 0
            self.sprite_key = "l"
            self.blit_sprite()
        elif self.sprite_key is not "r" and self.direction is "r":
            self.sprite_indx = 0
            self.sprite_key = "r"
            self.blit_sprite()
        elif self.sprite_key is not "i" and self.direction is None:
            self.sprite_indx = 0
            self.sprite_key = "i"
            self.blit_sprite()

        self.sprite_counter += utils.delta

        if self.sprite_counter > self.animation_delta:
            self.sprite_counter = 0
            self.sprite_indx += 1
            self.sprite_indx %= len(self.sprites[self.sprite_key])
            self.blit_sprite()

    def blit(self, dest):
        x, y = self.pos
        dest.blit(self.surface, (x - Camera.pos[0], y - Camera.pos[1]))

    def load_sprites(self):
        for key in self.sprites.keys():
            path = os.path.join(os.path.join("sprites", self.name), key)
            if not os.path.exists(path):
                continue
            files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]
            files = [f for f in files if len(f) > 4 and unicode(f[:-4],"utf-8").isnumeric()]
            files = [f for f in files if f[-4:] == ".png"]
            for f in sorted(files): # sorted alphanumerically (NOT numerically)
                url = os.path.join(
                    os.path.join("sprites", self.name),
                    key,
                    f,
                )
                self.sprites[key].append(pygame.image.load(url))

    def blit_sprite(self):
        self.sprite = self.sprites[self.sprite_key][self.sprite_indx]
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(self.sprite, (0, 0))
