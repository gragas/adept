from guiManager import GUIManager
from buffalo import utils
from nose.tools import assert_raises
import pygame

utils.init()

def test_init():
	g = GUIManager()

class Test_GUI:
	def __init__(self):
		self.mouse = False
		self.updated = False
		self.surface = None
		self.pos = (0,0)

	def mouseDown(self,loc):
		self.mouse = True

	def update(self):
		self.updated = True

class GUI_with_keyboard(Test_GUI):
	def handleKeyboardPress(self,keys):
		self.keys = keys


def test_bad_gui_object():
	g = GUIManager()
	assert_raises(NotImplementedError,g.registerGUI,'test')
	assert_raises(UserWarning, g.registerGUI, Test_GUI())

def test_ok_gui_object():
	t = Test_GUI()
	t.surface = utils.empty_surface((1,1))
	g = GUIManager()
	g.registerGUI(t)

def test_deregister():
	t = Test_GUI()
	t.surface = utils.empty_surface((1,1))
	g = GUIManager()
	g.registerGUI(t)
	length = len(g.guiScreens)
	g.deregisterGUI(t)
	assert len(g.guiScreens) == length - 1

def test_deregister_always_on():
	t = Test_GUI()
	t.surface = utils.empty_surface((1,1))
	g = GUIManager()
	g.registerAlwaysOnGUI(t)
	length = len(g.alwaysOnGUIs)
	g.deregisterGUI(t)
	assert len(g.alwaysOnGUIs) == length - 1

def test_keyboard_response():
	t = GUI_with_keyboard()
	t.surface = utils.empty_surface((1,1))
	g = GUIManager()
	g.registerGUI(t)
	g.sendKeyboardPresses()
	keys = pygame.key.get_pressed()
	assert t.keys == keys

def test_mouse_down_true():
	t = Test_GUI()
	t.surface = utils.empty_surface((1,1))
	pygame.mouse.set_pos((0,0))
	g = GUIManager()
	g.registerGUI(t)
	g.handleMouseEvent()
	assert t.mouse is True

def test_mouse_down_false():
	t = Test_GUI()
	t.surface = utils.empty_surface((1,1))
	pygame.mouse.set_pos((10,10))
	g = GUIManager()
	g.registerGUI(t)
	g.handleMouseEvent()
	assert t.mouse is False

def test_update():
	t = Test_GUI()
	t.surface = utils.empty_surface((1,1))
	g = GUIManager()
	g.registerGUI(t)
	g.updateGUIs()
	assert t.updated
	
