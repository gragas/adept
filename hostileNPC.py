from buffalo import utils
import pygame, sys
from pygame import *
from color import *
from math import random


class HostileNPC(pygame.sprite.Sprite):

      
    def __init__(self, name, fPos, health, speed, size, screen):
        pygame.sprite.Sprite.__inite__(self)
        self.size = size
        self.image = pygame.Surface((size,size))
        self.screen = screen
        self.fPos = fPos
        self.rect = self.image.get_rect()
        self.image.fill((0,0,0))
        self.alive = True;
        self.health = health
        self.speed = speed
        self.xv, self yv. = random.randrange(0, 10), random.randrange(0, 10)
        


    def update(self):
        x, y = self.fPos
        x += self.xv
        y += self.yv
        self.fPos = x, y
        self.health -= damage;
        if(self.health == 0):
            self.alive = False;
        self.pos  = int(self.fPos[0]), int(self.fPos[1])
        

    def blit(self, dest):
        (if self.alive == True):
            x, y = self.pos
            dest.blit(self.surface, (x, y))
