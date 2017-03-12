import os
import os.path

import pygame
import pygame.image

from buffalo import utils

from camera import Camera
from character import Character
from chunk import Chunk

from inventory import Inventory

class PlayerCharacter(Character):

    DEFAULT_NAME  = "Unnamed PlayerCharacter"
    DEFAULT_SIZE  = 32, 32
    DEFAULT_SPEED = 0.02
    DEFAULT_FPOS  = (
        float(Chunk.CHUNK_WIDTH * Chunk.TILE_SIZE / 2 - DEFAULT_SIZE[0] / 2),
        float(Chunk.CHUNK_HEIGHT * Chunk.TILE_SIZE / 2 - DEFAULT_SIZE[1]),
        )
    DEFAULT_COLOR      = (170,170,170,255) # Added for testing purposes
    DEFAULT_SPRITE_URL = os.path.join("sprites", "deep_elf",)

    #**kwargs here allows for an object to be created with a dictionary for input, which basically allows an object to be created from the deserialize method
    def __init__(self, inventory, name=None, fPos=None, size=None, speed=None, **kwargs):
        name = name if name is not None else PlayerCharacter.DEFAULT_NAME #These could probably be rewritten with kwargs
        fPos = fPos if fPos is not None else PlayerCharacter.DEFAULT_FPOS
        size = size if size is not None else PlayerCharacter.DEFAULT_SIZE
        Character.__init__(self, name=name, fPos=fPos, size=size)
        self.speed = speed if speed is not None else PlayerCharacter.DEFAULT_SPEED
        self.xv, self.yv = 0.0, 0.0
        self.surface = utils.empty_surface(self.size)
        self.inventory = inventory
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
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        self.idle = False
        self.animation_delta = int((1.0 / self.speed) * 10.5)

    def update(self, keys):

        w, a, s, d = (
            keys[pygame.K_w],
            keys[pygame.K_a],
            keys[pygame.K_s],
            keys[pygame.K_d],
        )
        
        if w:
            self.yv += -self.speed
        if s:
            self.yv += self.speed
        if d:
            self.xv += self.speed
        if a:
            self.xv += -self.speed

        if abs(self.xv) + abs(self.yv) > self.speed:
            self.xv /= 1.4142135 # / sqrt(2)
            self.yv /= 1.4142135 # / sqrt(2)

        x, y = self.fPos
        x += self.xv * utils.delta
        y += self.yv * utils.delta
        self.fPos = x, y
        self.pos  = int(self.fPos[0]), int(self.fPos[1])
        self.xv, self.yv = 0.0, 0.0

        if not self.moving_up and w and not(a or s or d):
            self.moving_up = True
            self.moving_down = False
            self.moving_right = False
            self.moving_left = False
            self.idle = False
            self.sprite_indx = 0
            self.sprite_key = "u"
            self.blit_sprite()
        if not self.moving_down and s and not(a or w or d):
            self.moving_up = False
            self.moving_down = True
            self.moving_right = False
            self.moving_left = False
            self.idle = False
            self.sprite_indx = 0
            self.sprite_key = "d"
            self.blit_sprite()
        if not self.moving_left and a and not(w or s or d):
            self.moving_up = False
            self.moving_down = False
            self.moving_right = False
            self.moving_left = True
            self.idle = False
            self.sprite_indx = 0
            self.sprite_key = "l"
            self.blit_sprite()
        if not self.moving_right and d and not(a or s or w):
            self.moving_up = False
            self.moving_down = False
            self.moving_right = True
            self.moving_left = False
            self.idle = False
            self.sprite_indx = 0
            self.sprite_key = "r"
            self.blit_sprite()
        if not self.idle and not(a or s or w or d):
            self.moving_up = False
            self.moving_down = False
            self.moving_right = False
            self.moving_left = False
            self.idle = True
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
        cx, cy = Camera.pos
        dest.blit(self.surface, (x - cx, y - cy))

    def load_sprites(self):
        for key in self.sprites.keys():
            path = os.path.join(PlayerCharacter.DEFAULT_SPRITE_URL, key)
            if not os.path.exists(path):
                continue
            files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]
            files = [f for f in files if len(f) > 4 and f[:-4].isnumeric()]
            files = [f for f in files if f[-4:] == ".png"]
            for f in sorted(files): # sorted alphanumerically (NOT numerically)
                url = os.path.join(
                    PlayerCharacter.DEFAULT_SPRITE_URL,
                    key,
                    f,
                )
                self.sprites[key].append(pygame.image.load(url))

    def blit_sprite(self):
        self.sprite = self.sprites[self.sprite_key][self.sprite_indx]
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(self.sprite, (0, 0))
