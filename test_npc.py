from buffalo import utils
from npc import NPC
# from enemy import Enemy
# from friendly import Friendly
# from trader import Trader

utils.init()
isWorking = False
# A = NPC()
B = NPC(name="b", fPos=(650.0,650.0), 15, 2)
C = NPC(name="c", fPos=(800.0,800.0), 20, 3)
npcs = [B, C]
 
for npc in npcs:
    NPC.load_sprites()
    NPC.move_X(4)
    NPC.move_Y(3)
    NPC.detectCollision(npcs)
    NPC.blit_sprite()
     
NPC.update()    
isWorking = True
assert isWorking
print True
