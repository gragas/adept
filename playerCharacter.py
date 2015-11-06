import os
import os.path
import weakref

import pygame
import pygame.image

from buffalo import utils

from camera import Camera
from character import Character
from chunk import Chunk

from inventory import Inventory
from skill import Skill
from subMap import SubMap

class PlayerCharacter(Character):

    DEFAULT_NAME  = "Unnamed PlayerCharacter"
    DEFAULT_SIZE  = 32, 32
    DEFAULT_SPEED = 0.02
    DEFAULT_FPOS  = (
        float(Chunk.CHUNK_WIDTH * Chunk.TILE_SIZE / 2 - DEFAULT_SIZE[0] / 2),
        float(Chunk.CHUNK_HEIGHT * Chunk.TILE_SIZE / 2 - DEFAULT_SIZE[1]),
        )
    DEFAULT_COLOR      = (170,170,170,255) # Added for testing purposes
    DEFAULT_SPRITE_URL = os.path.join("sprites", "paul_asl",)

    #**kwargs here allows for an object to be created with a dictionary for input, which basically allows an object to be created from the deserialize method
    def __init__(self, inventory, name=None, fPos=None, zLevel=0, size=None, speed=None, **kwargs):
        name = name if name is not None else PlayerCharacter.DEFAULT_NAME #These could probably be rewritten with kwargs
        fPos = fPos if fPos is not None else PlayerCharacter.DEFAULT_FPOS
        size = size if size is not None else PlayerCharacter.DEFAULT_SIZE
        self.level = kwargs.get('level') if kwargs.get('level') is not None else 1
        self.experience = kwargs.get('experience') if kwargs.get('experience') is not None else 0
        Character.__init__(self, name=name, fPos=fPos, size=size, spawn=kwargs.get('spawn'))
        self.speed = speed if speed is not None else PlayerCharacter.DEFAULT_SPEED
        self.swordSkill = kwargs.get('swordSkill') if kwargs.get('swordSkill') is not None else Skill(name="SwordSkill") #Example setup for a skill
        self.bowSkill = kwargs.get('bowSkill') if kwargs.get('bowSkill') is not None else Skill(name="BowSkill")
        self.xv, self.yv = 0.0, 0.0
        self.surface = utils.empty_surface(self.size)
        self.inventory = inventory
        self.inventory.playerCharacter = weakref.ref(self)
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
        self.zLevel = zLevel

    def update(self, keys, submaps):

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

        
        
        ##TODO: Make Collisions less "sticky"
        for submap in submaps:
            #Collision Logic
            collideRect = pygame.Rect(submap.pos[0],submap.pos[1],submap.size[0]*SubMap.TILE_SIZE, submap.size[1]*SubMap.TILE_SIZE)
            pcRect = pygame.Rect((self.fPos[0]+6, self.fPos[1]), (self.surface.get_size()[0]-6,self.surface.get_size()[0])) #Manually using only the x component of self.surface necessary b/c for some reason the sprite has size (32,64) 
            #pcRect = self.surface.get_bounding_rect().move(self.fPos)  
            if collideRect.colliderect(pcRect):
                submap.handleCollision(submap.getTileAtCoord(pcRect.center),self) 
                newRect = pcRect.move(( self.xv * utils.delta, self.yv * utils.delta )) 
                for tile in submap.tileMap:
                    if tile.collisionEnabled and tile.pos[2] == self.zLevel:
                        tileRect = pygame.Rect( submap.pos[0] + tile.pos[0] * SubMap.TILE_SIZE, submap.pos[1] + tile.pos[1] * SubMap.TILE_SIZE, SubMap.TILE_SIZE, SubMap.TILE_SIZE )
                        if tileRect.colliderect(newRect):
                            #Collision Detected between player and rect
                            if tile.onCollision(pc=self) is not None:
                                submap.render(self.zLevel)
                            #X-Velocity Logic
                            if pcRect.center[0] < tileRect.midleft[0] and self.xv > 0:
                                self.xv = 0
                            elif pcRect.center[0] > tileRect.midright[0] and self.xv < 0:
                                self.xv = 0
                            #Y-Velocity Logic
                            if pcRect.center[1]  < tileRect.midbottom[1] and self.yv > 0:
                                self.yv = 0
                            elif pcRect.center[1] > tileRect.midtop[1] and self.yv < 0:
                                self.yv = 0
                                
        x,y = self.fPos
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

    def gainXP(self, amount):
        self.experience += amount
        if self.experience >= 100*self.level:
            self.level += 1
            self.experience %= (100*self.level)

    def load_sprites(self):
        for key in self.sprites.keys():
            path = os.path.join(PlayerCharacter.DEFAULT_SPRITE_URL, key)
            if not os.path.exists(path):
                continue
            files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]
            files = [f for f in files if len(f) > 4 and unicode(f[:-4],"utf-8").isnumeric()]
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
