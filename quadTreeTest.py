from entityManager import EntityManager
from Entity import Entity

a, b, c, d, e = Entity
a.x, a.y = 0, 0
b.x, b.y = 2, 3
c.x, c.y = 5, 6
d.x, d.y = 1, 0
e.x, e.y = 0, 4
entityList = [a, b, c, d, e]

EntityManager.__init__(entityList, 0, 32, 0, 32)
EntityManager.add_entity(a)
EntityManager.add_entity(b)
EntityManager.add_entity(c)
EntityManager.add_entity(d)
EntityManager.add_entity(e)
test_intersect_rect = EntityManager.intersect_rect(a, 2, 3)
print test_intersect_rect

a.move_X(3)
a.move_Y(1)
test_intersect_circ = EntityManager.intersect_circle(a, 3)
print test_intersect_circ
EntityManager.merge()

EntityManager.find_nearest_neighbor(a)

c.move_X(30)
EntityManager.update()
start = (0, 4)
end = (1, 2)
e.find_path(start, end)
print e.x + ', ' + e.y
EntityManager.hit(entityList, b)
EntityManager.findCollision(entityList)
print entityList

for e in entityList:
    e.move_X(1)
    e.move_Y(1)
    
EntityManager.update()
EntityManager.findCollision(entityList)

print entityList
print True

