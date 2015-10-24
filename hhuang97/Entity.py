#import serializable

class Entity():
    def __init__(self, x, y, hp, stat):
        #self.name = ""
        self.x_pos = x
        self.y_pos = y
        self.health = hp
        self.attack = stat
        self.health_max = max
    """    
    def take_damage(self, character, attack):
        damage = min(max(character - attack, 0), character.health)
        character.health = character.health - damage
        return character.health
        
    def do_damage(self, enemy, attack):
        damage = min(max(enemy - attack, 0), enemy.health)
        enemy.health = enemy.health - damage
        return enemy.health
    
    def gain_exp(self, exp, level_up, level):
        self.exp += exp
        self.level_up = level_up
        level_up = level_up - exp
        if exp > level_up:
            level = level + 1
        return level
    """
    def move_X(self, current_x, move_x):
        return current_x + move_x
    
    def move_Y(self, current_y, move_y):
        return current_y + move_y
    
    def get_X(self, x):
        return x
    
    def get_Y(self, y):
        return y
    """
    def collision(self, other):
        #collide = other.collision(self)
        #above is infinite recursive call
        collide = False
        return collide
    
    def remove_entity(self, entityID):
        #need dictionary to get comprehensive list of where to delete entity
        entityID = 0
        return entityID
    
    def add_entity(self, x, y, hp, stats, c):
        return Entity.__init__(x, y, hp, stats)

    def entity_properties(self, x, y, move, health):
        return Entity.__init__(x, y, health, move)
    
    
    class Player(): #marks entity as player
        def __init__(self, character_ID):
            self.character_ID = character_ID
    """