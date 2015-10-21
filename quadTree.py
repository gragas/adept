from Entity import Entity
import math

class QuadTree(object):
    # one quadtree for each chunk
    
    class Node(object):
        splitThreshold = 8 # max number of entities that can be in a leaf
        
        def __init__(self, entityList, min_x, max_x, min_y, max_y):
            # bounds are inclusive
            self.min_x = min_x
            self.max_x = max_x
            self.min_y = min_y
            self.max_y = max_y
            if len(entityList) > QuadTree.Node.splitThreshold:
                self.isLeaf = False
            else:
                self.isLeaf = True
                self.eList = [e for e in entityList if Entity.x <= self.max_x & Entity.x >= self.min_x
                              & Entity.y >= self.min_x & Entity.y <= self.max_y]
            
        def split_node(self):
            center_x = (self.min_x + self.max_x) / 2
            center_y = (self.min_y + self.max_y) / 2
            self.NE = QuadTree.Node(self.eList, center_x+1, self.max_x, self.min_y, center_y)
            self.NW = QuadTree.Node(self.eList, self.min_x, center_x, self.min_y, center_y)
            self.SE = QuadTree.Node(self.eList, center_x+1, self.max_x, center_y+1, self.max_y)
            self.SW = QuadTree.Node(self.eList, self.min_x, center_x, center_y+1, self.max_y)
            
        def intersect_circle(self, Entity, radius):
            # finds all entities within rectangle of width x_range*2 and length y_range*2
            for e in self.eList:
                if math.sqrt((Entity.x-e.x)**2 + (Entity.y-e.y)**2) < radius:
                    pass
                else:
                    self.eList.remove(e)
            return self.eList
        
        def intersect_rect(self, Entity, x_range, y_range):
            for e in self.eList:
                if Entity.x + x_range > e.x:
                    if Entity.y + y_range > e.y:
                        pass
                    elif Entity.y - y_range < e.y:
                        pass
                elif Entity.x - x_range < e.x:
                    if Entity.y + y_range > e.y:
                        pass
                    elif Entity.y - y_range < e.y:
                        pass
                else:
                    self.eList.remove(e)
            return self.eList
        
        