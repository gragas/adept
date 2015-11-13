import pygame

from Entity import Entity
import random
from quadTree import QuadTree
from inventory import Inventory

RED = (255, 0, 0)

class Projectile (Entity, QuadTree):
    
    def __init__(self):
        super.__init__()
        self.image = pygame.Surface([15, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = Entity.x
        self.y = Entity.y
        Inventory.removeItem(self, Inventory.items[3][0]) # removes an arrow from inventory
    
    def findCollision(self, projectileList):
        self.projectileList = projectileList
        self.pList = self.projectileList
        super.__init(self, self.pList, 0, 32, 0, 32) # initialize within a chunk
        for p in projectileList: # find projectiles within radius 1 of each other
            if p.intersect_circle(self, 1) == self.intersect_circle(self, 1):
                self.projectileList.remove(p)
            else:
                pass
        for p in self.projectileList:
            p.removeProjectile()
        
    def removeProjectile(self):
        for p in self.projectileList:
            # remove projectile from screen
            pass
        
    def update(self): # moves projectile and keeps track of it
        x_velocity, y_velocity = random.randint(5, 10), random.randint(5, 10)
        Entity.move_X(self, x_velocity)
        Entity.move_Y(self, y_velocity)
        for proj in self.pList:
            proj.move_X(self, x_velocity)
            proj.move_Y(self, y_velocity)