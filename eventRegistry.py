class EventRegistry:
	LISTENERS = list()

	@staticmethod
	def registerEvent(event):
		if not isinstance(event, Event):
			raise TypeError
			return
		if len(EventRegistry.LISTENERS) == 0:
			return
		for listener in EventRegistry.LISTENERS:
			if listener[1] == event.type:
				listener[0](event)

	@staticmethod
	def getEvents():
		return EventRegistry.EVENTS

	@staticmethod
	def registerListener(func,_type):
		if func is None or not callable(func):
			raise NotImplementedError
			return
		EventRegistry.LISTENERS.append((func,_type))

	@staticmethod
	def clearListeners():
		EventRegistry.LISTENERS = list()

class Event:
	def __init__(self, _type, info):
		if not isinstance(_type,str) or not isinstance(info,dict):
			raise TypeError
			return
		self.type = _type
		self.info = info