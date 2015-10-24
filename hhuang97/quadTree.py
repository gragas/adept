from Entity import Entity
import math

class QuadTree(object):
    # make a quadtree for each chunk based on chunk loading
    class Node(object):
        splitThreshold = 8 # maximum number of entities that can be in a leaf
        
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
            
        def subdivide(self):
            # recursive call to subdivide until there are few enough entities in a leaf
            center_x = (self.min_x + self.max_x) / 2
            center_y = (self.min_y + self.max_y) / 2
            self.NE = QuadTree.Node(self.eList, center_x+1, self.max_x, self.min_y, center_y)
            self.NW = QuadTree.Node(self.eList, self.min_x, center_x, self.min_y, center_y)
            self.SE = QuadTree.Node(self.eList, center_x+1, self.max_x, center_y+1, self.max_y)
            self.SW = QuadTree.Node(self.eList, self.min_x, center_x, center_y+1, self.max_y)
            
        def intersect_circle(self, Entity, radius):
            # finds all entities within a circle of radius 'radius' given a specific entity
            NEcorner_x, NEcorner_y = Entity.x + radius, Entity.y - radius
            SWcorner_x, SWcorner_y = Entity.x - radius, Entity.y + radius
            self.eList_circle = self.eList
            for e in self.eList_circle: # checks points in a square inscribing the circle
                # keep all points inside the square
                if e.x < NEcorner_x & e.x > SWcorner_x:
                    if e.y > NEcorner_y & e.y < SWcorner_y:
                        pass
                    else:
                        self.eList_circle.remove(e)
            for e in self.eList_circle: # check points inside circle after having been filtered by square
                if math.sqrt((Entity.x - e.x)**2 + (Entity.y - e.y)**2) <= radius:
                    pass
                else:
                    self.eList_circle.remove(e)
            self.eList = self.eList_circle
        
        def intersect_rect(self, Entity, x_range, y_range):
            # finds all entities within rectangle of width x_range*2 and length y_range*2 of given entity
            self.eList_rect = self.eList
            for e in self.eList_rect:
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
                    self.eList_rect.remove(e)
            self.eList = self.eList_rect
        
        def merge(self, eList_rect, eList_circle):
            """
            TODO: merge points from eList_rect and eList_circle, take out repeats
            """
            pass