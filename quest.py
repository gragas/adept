class Quest:
	def __init__():
		self.name = ''
		self.id = 0
		self.description = ''
		self.stage = 0
		self.stages = dict()
		self.state = QuestState.NOT_STARTED

	def onCompletion():
    	raise NotImplementedError

    def onStart():
        raise NotImplementedError

	def handleEvent():
		pass

class QuestState():
	NOT_STARTED = 0
	IN_PROGRESS = 1
	COMPLETED = 2
	FAILED = 3