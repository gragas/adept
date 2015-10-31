from quest import Quest

class QuestManager(Serializible):
	ACTIVE_QUESTS = list()
	COMPLETED_QUESTS = list()

	@staticmethod
	def HandleEvent(event):
		for q in QuestManager.ACTIVE_QUESTS:
			q.update

	@staticmethod
	def startQuest(quest):
		quest.onStart()
		QUESTS.append(quest)


