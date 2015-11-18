from eventRegistry import EventRegistry
from eventRegistry import Event
from nose.tools import assert_raises

def test_event_init():
	d = dict()
	d["quality"] = 5
	e = Event("test_event",d)
	assert e.type == "test_event"
	assert e.info["quality"] == 5

def test_event_initialization_type_error():
	assert_raises(TypeError, Event, 5, dict())
	assert_raises(TypeError, Event, "", "")

def test_event_registry_blocking_bad_objects():
	assert_raises(TypeError, EventRegistry.registerEvent,5)

def test_event_registry_successful_register():
	e = Event("test",dict())
	EventRegistry.registerEvent(e)
	EventRegistry.clearListeners()

class TestListener:
	def handleEvent(self,event):
		self.result = True

def test_correct_listener():
	l = TestListener()
	EventRegistry.registerListener(l.handleEvent,"test")
	e = Event("test",dict())
	EventRegistry.registerEvent(e)
	assert hasattr(l, 'result') and l.result == True
	EventRegistry.clearListeners()

def test_incorrect_listener():
	e = Event("test",dict())
	EventRegistry.registerEvent(e)
	l = TestListener()
	assert_raises(NotImplementedError, EventRegistry.registerListener,"test","test")
	EventRegistry.clearListeners()
