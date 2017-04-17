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
			if listener[1] == event.type or (listener[2] and event.type.startswith(listener[1])):
				listener[0](event)

	@staticmethod
	def getEvents():
		return EventRegistry.EVENTS

	"""
	Listener Parameters:
		-func: Callback function to be called when event is triggered
		-_type: String that codes for a certain event. By convention, should be in the format:
			'module_specificEvent'
			ex: 'inventory_add_item'
		-flexible_type: If true, will trigger if the event type starts with the _type parameter:
			ex: _type = 'inventory', flexible_type = True: func will be called for any 'inventory_x' event
	"""
	@staticmethod
	def registerListener(func,_type,flexible_type=False):
		if func is None or not callable(func):
			raise NotImplementedError
			return
		EventRegistry.LISTENERS.append((func,_type,flexible_type))

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
		
