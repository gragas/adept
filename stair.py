from tile import Tile

class Stair(Tile):
	def __init__(self,isUp=True,**kwargs):
		super(Stair, self).__init__(**kwargs)
		self.isUp = isUp
	

	def onCollision(self,pc=None):
		if pc is not None:
			if self.isUp:
				pc.zLevel += 1
			else:
				pc.zLevel -= 1
			return True
			
