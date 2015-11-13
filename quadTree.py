from Entity import Entity
import math

class Node(object):
    splitThreshold = 4 # maximum number of entities that can be in a leaf
        
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
        self.NE = Node(self.eList, center_x+1, self.max_x, self.min_y, center_y)
        self.NW = Node(self.eList, self.min_x, center_x, self.min_y, center_y)
        self.SE = Node(self.eList, center_x+1, self.max_x, center_y+1, self.max_y)
        self.SW = Node(self.eList, self.min_x, center_x, center_y+1, self.max_y)
        branch = self.NE | self.NW | self.SE | self.SW
        self.branches.append(branch)
            
    def contains(self, x, z):
        x0, x1, z0, z1 = self.rect
        if x >= x0 and x <= x1 and z >= z0 and z <= z1:
            return True
        return False

class QuadTree(object):
    """
    TODO:
    wrapper methods for public interface
    go up far enough to include node with old and new positions (?)
    """
    
    def __init__(self, parent):
        self.parent = parent
        self.children = [None,None,None,None]
        self.branches = []
        
        
    def hit(self, entities, Entity):
        # when an entity moves, node redraws only when the entity goes to the edge of a node
        self.entities = entities
        for e in self.entities:
            if e.intersect_rect(Entity, 16, 16):
                QuadTree.redraw_nodes()
            else:
                pass
    
    def subdivide_entities(self):
        for e in self.entityList:
            for b in self.branches:
                if b.get_rect().colliderect(Entity.get_rect()):
                    b.add_entity(e)
    
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
        
    def merge(self):
        QuadTree.merger(self.eList_rect, self.eList_circle)    
    
    
    def merger(self, eList_rect, eList_circle):
        # merges entities obtained from two intersect methods and removes duplicates
        in_rectList = set(self.eList_rect)
        in_circList = set(self.eList_circle)
        unique = in_rectList - in_circList
        self.eList = in_circList + list(unique)
    
    def findCollision(self, entities):
        self.entList = entities
        self.collideList = self.entList
        QuadTree.__init(self, self.collideList, 0, 32, 0, 32)
        for e in self.entList:
            if e.intersect_circle(self, 1) == self.intersect_circle(self, 1):
                self.projectileList.remove(e)
            else:
                pass
        for e in self.entList:
            self.entList.remove(e)
    
    def find_nearest_neighbor(self, Entity):
        n = 1
        for e in self.eList:
            self.closestNeighbor = e.intersect_circle(Entity, n)
            if len(self.closestNeighbor == 0):
                n+=1
            elif len(self.closestNeighbor) >= 1: # found closest neighbor(s)
                break
            else: # random cases?
                continue
    
    def get_rect(self):
        return self.rect
    
    def redraw_nodes(self):
        Node.subdivide()
    
    def add_entity(self, Entity):
        self.entityList.append(Entity)
        
    def remove_entity(self, Entity):
        # remove entity and remove redundant nodes (delete empty nodes)
        self.entityList.remove(Entity)
        
    def remove_entity_nodes(self, Entity):
        QuadTree.remove_entity(self, Entity)
        Node.subdivide()
        
    def transfer_entity(self, Entity, QuadTree):
        # remove entity and add to another quadtree [WIP]
        QuadTree.remove_entity_nodes(self, Entity)
        q = QuadTree
        q.__init__(q.parent)
        q.add_entity(Entity)
    
    def update(self):
        # updates quadtree and recursively redraws nodes 
        if len(self.entityList) > Node.splitThreshold:
            self.subdivide_entities()
            self.Node.subdivide()
            for b in self.branches:
                b.update()
        else:
            self.findCollision(self.entityList)
    
    
    """
    Below methods are used for path finding using A* algorithm
    https://en.wikipedia.org/wiki/A*_search_algorithm
    """
    
    # wrapper method for A* search
    def find_path(self, source, destination):
        source = self.quadtree.cell_at(*source)
        destination = self.quadtree.cell_at(*destination)
        path = self.quadtree.a_star_search(source, destination) + [destination]
        points = [source.center]
        for i, cell in enumerate(path):
            try:
                next_path = path[i+1]
            except IndexError:
                points.append(cell.center)
                break
            if cell.top == next_path.bottom:
                if cell.width < next_path.width:
                    points.append(cell.midtop)
                else:
                    points.append(next_path.midbottom)
            elif cell.bottom == next_path.top:
                if cell.width < next_path.width:
                    points.append(cell.midbottom)
                else:
                    points.append(next_path.midtop)
            elif cell.right == next_path.left:
                if cell.height < next_path.height:
                    points.append(cell.midright)
                else:
                    points.append(next_path.midleft)
            elif cell.left == next_path.right:
                if cell.height < next_path.height:
                    points.append(cell.midleft)
                else:
                    points.append(next_path.midright)
        return points
    
    def a_star_search(self, start, end):
        closed = set()
        g_score = {start: 0}
        h_score = {start: (start.center - end.center)}
        f_score = {start: h_score[start]}
        came_from = {}

        def reconstruct_path(node):
            if node in came_from:
                return reconstruct_path(came_from[node]) + [node]
            else:
                return [node]
        
        while f_score:
            l = [(v, k) for k, v in f_score.entities()]
            l.sort()
            x = l[0][1]
            if x is end:
                return reconstruct_path(came_from[end])
            del f_score[x]
            closed.add(x)
            for y in x.neighbors():
                if y in closed:
                    continue
                tentative_g_score = g_score[x] + (x.center - y.center)
                if y not in f_score:
                    tentative_is_better = True
                elif tentative_g_score < g_score[y]:
                    tentative_is_better = True
                else:
                    tentative_is_better = False
                if tentative_is_better:
                    came_from[y] = x
                    g_score[y] = tentative_g_score
                    h_score[y] = y.center - end.center
                    f_score[y] = g_score[y] + h_score[y]
        raise ValueError('cannot find path')