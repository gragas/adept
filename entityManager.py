from quadTree import QuadTree, Node

class EntityManager(QuadTree):
    
    def __init__(self, entityList):
        self.entityList = entityList
        Node.__init__(entityList, 0, 32, 0, 32) # size of a chunk
        QuadTree.__init__(entityList)
        for e in self.entityList:
            QuadTree.add_entity(e)
            
    def collision(self, Entity):
        QuadTree.update()
        QuadTree.findCollision(self.entityList)
        for e in self.entityList:
            if QuadTree.find_nearest_neighbor(e) == Entity:
                pass
            else:
                continue
    
    def add_entity(self, Entity):
        QuadTree.add_entity(Entity)
        
    def remove_entity_nodes(self, Entity):
        QuadTree.remove_entity_nodes(Entity)
        
    