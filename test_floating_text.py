from floatingText import FloatingText
from floatingText import FloatingTextManager
from nose.tools import assert_raises
from buffalo import utils

utils.init()

def test_init_defaults():
    t = FloatingText("test",(0,0))
    assert t.color == (0,0,0,255)
    assert t.vert_speed == 0
    assert t.hor_speed == 0
    assert t.lifetime == -1
    assert t.font_size == 15
    assert t.alpha_decay == 0
    assert t.font == 'comicsans'

class FakeFloatingText(FloatingText):
    def __init__(self):
        super(FakeFloatingText, self).__init__("test",(0,0))
        
        self.updated = False
        self.rendered = False

    def update(self):
        self.updated = True

    def render(self):
        self.rendered = True

def test_manager_calls():
    t = FakeFloatingText()
    FloatingTextManager.registerFloatingText(t)
    FloatingTextManager.update()
    assert t.updated
    FloatingTextManager.render()
    assert t.rendered

def test_register_fText():
    t = FloatingText("test",(0,0))
    FloatingTextManager.registerFloatingText(t)

def test_bad_fText_register():
    assert_raises(TypeError, FloatingTextManager.registerFloatingText, 'test')

def test_alpha_decay_removal():
    t = FloatingText("test",(0,0))
    FloatingTextManager.registerFloatingText(t)
    currLen = len(FloatingTextManager.ACTIVE_FLOATING_TEXTS)
    FloatingTextManager.update()
    assert len(FloatingTextManager.ACTIVE_FLOATING_TEXTS) == currLen
    t.alpha = -1
    FloatingTextManager.update()
    assert len(FloatingTextManager.ACTIVE_FLOATING_TEXTS) == currLen - 1

def test_lifetime_removal():
    t = FloatingText("test",(0,0))
    t.lifetime = 5000
    FloatingTextManager.registerFloatingText(t)
    currLen = len(FloatingTextManager.ACTIVE_FLOATING_TEXTS)
    FloatingTextManager.update()
    assert len(FloatingTextManager.ACTIVE_FLOATING_TEXTS) == currLen
    t.lifetime_counter = 5001
    FloatingTextManager.update()
    assert len(FloatingTextManager.ACTIVE_FLOATING_TEXTS) == currLen - 1
    
