import os

import json

from serializable import Serializable

class Saves: #Only partially implemembted- only works for PlayerCharacters

	#Because we want the user to be able to play on whatever world they want with whatever character
	#they want, characters have to be stored independently of everything else
	#We need to implement an aspect of this for things like the map, item locations, npc locations, 
	#And everything that has to do with the world state in a different location.

	@staticmethod
	def store(obj): #Currently only works for player characters
		serialization = obj.serialize()
		if obj.__class__.__name__ == "PlayerCharacter":
			if not os.path.isdir("characters"):
				os.makedirs("characters")
			with open(os.path.join("characters", obj.name), 'w+') as f:
				json.dump(serialization, f)
		else:
			pass #Needs to be implemented for saving the map and world state

	@staticmethod
	def unstore(name, path): #Currently only works for player characters
		if os.path.isfile(os.path.join(path, name)):
			with open(os.path.join(path, name), 'r') as f:
				saved = json.load(f)
			return Serializable.deserialize(saved)
		return None