from serializable import Serializable

class Skill(Serializable):

	DEFAULT_LEVEL = 1
	DEFAULT_EXPERIENCE = 0

	def __init__(self, name, level=None, experience=None):
		self.name = name
		self.level = level if level is not None else Skill.DEFAULT_LEVEL
		self.experience = experience if experience is not None else Skill.DEFAULT_EXPERIENCE

	def gainXP(self, amount):
		self.experience += amount
		if self.experience >= 500*self.level:
			self.level += 1
			self.experience %= (500*self.level)
			
