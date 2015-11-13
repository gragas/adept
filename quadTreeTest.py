from quadTree import QuadTree
from Entity import Entity
#from quadTreeManager import

a, b, c, d, e= Entity
a.x, a.y = 0, 0
b.x, b.y = 2, 3
c.x, c.y = 5, 6
d.x, d.y = 1, 0
e.x, e.y = 0, 4
entityList = [a, b, c, d, e]

QuadTree.__init__(entityList, 0, 32, 0, 32)
QuadTree.add_entity(a)
QuadTree.add_entity(b)
QuadTree.add_entity(c)
QuadTree.add_entity(d)
QuadTree.add_entity(e)
test_intersect_rect = QuadTree.intersect_rect(a, 2, 3)
print test_intersect_rect

a.move_X(3)
a.move_Y(1)
test_intersect_circ = QuadTree.intersect_circle(a, 3)
print test_intersect_circ
QuadTree.merge()

QuadTree.find_nearest_neighbor(a)

c.move_X(30)
QuadTree.update()
start = (0, 4)
end = (1, 2)
e.find_path(start, end)
print e.x + ', ' + e.y
QuadTree.hit(entityList, b)
QuadTree.findCollision(entityList)
print entityList

for e in entityList:
    e.move_X(1)
    e.move_Y(1)
    
QuadTree.update()
QuadTree.findCollision(entityList)
