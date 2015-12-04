

class Entity(object):
    entityIDCounter = 0
    
    def __init__(self, x, y):
        self.name = Entity.entityIDCounter
        Entity.entityIDCounter += 1
        self.x = x
        self.y = y
        #self.quadtree+=self
    
    def move_X(self, move_x):
        self.x += move_x
    
    def move_Y(self, move_y):
        self.y += move_y
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @x.setter
    def x(self, x):
        self._x = x
        #self.quadtree.update()
        
    @y.setter
    def y(self, y):
        self._y = y
        #self.quadtree.update()
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        return self.name == other.name
    
    def get_rect(self):
        return self.rect
    
    