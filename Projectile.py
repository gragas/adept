import pygame

from Entity import Entity
import random
from quadTree import QuadTree
from inventory import Inventory

RED = (255, 0, 0)

class Projectile (Entity, QuadTree):
    x_velocity, y_velocity = 5, 5
    
    def __init__(self):
        super.__init__()
        self.image = pygame.Surface([15, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = Entity.x
        self.y = Entity.y
        Inventory.removeItem(self, Inventory.items[3][0])
    
    def findCollision(self, projectileList):
        self.pList = projectileList
        super.__init(self, self.pList, 0, 32, 0, 32)
        for p in projectileList:
            if p.intersect_circle(self, 1) == self.intersect_circle(self, 1):
                self.pList.remove(p)
            else:
                pass
        
    def update(self): # moves projectile and keeps track of it
        x_velocity, y_velocity = random.randint(5, 10), random.randint(5, 10)
        # x_start, y_start = random.randint(1, 31), random.randint(1, 31)
        Entity.move_X(self, x_velocity)
        Entity.move_Y(self, y_velocity)
        for proj in self.pList:
            proj.move_X(self, x_velocity)
            proj.move_Y(self, y_velocity)