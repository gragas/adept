from buffalo import utils
from playerConsole import PlayerConsole
from playerConsole import EventText
from playerConsole import TextWrapper
import pygame

utils.init()
PlayerConsole.init()

ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum lobortis ac enim vel feugiat. Duis ac metus id est lobortis euismod. Vestibulum finibus est eget odio rhoncus consequat. Vestibulum sed lectus justo. Aenean fringilla mi et ultricies condimentum. Donec sapien quam, congue vitae felis at, bibendum tincidunt purus. Nulla in nunc consequat, laoreet nibh non, pulvinar eros. Quisque at justo mauris."

def test_event_text():
    e = EventText("test",(1,2,3,4))
    assert e.text == 'test'
    assert e.color == (1,2,3,4)

def test_text_wrapper():
    myfont = pygame.font.SysFont("monospace", 15)
    global ipsum
    assert len(TextWrapper.wrap_line(ipsum,myfont,10)) == 414
    assert len(TextWrapper.wrap_line(ipsum,myfont,100)) == 50
    assert len(TextWrapper.wrap_line(ipsum,myfont,250)) == 17

def test_register_text():
    currLen = len(PlayerConsole.TEXT_EVENTS)
    PlayerConsole.registerNewEvent("test")
    assert len(PlayerConsole.TEXT_EVENTS) == currLen + 1
    assert isinstance(PlayerConsole.TEXT_EVENTS[0], EventText)

def test_flash_on():
    PlayerConsole.flashOn()
    assert PlayerConsole.ALPHA == 255
    assert PlayerConsole.ALPHA_COUNTER == 0

def test_update():
    PlayerConsole.flashOn()
    PlayerConsole.update()
    assert PlayerConsole.ALPHA_COUNTER == 1
    tray_size = PlayerConsole.tray.surface.get_size()
    PlayerConsole.ALPHA_COUNTER = PlayerConsole.ALPHA_WAIT + 1
    PlayerConsole.update()
    #Test tray 'deletion' upon timeout
    assert PlayerConsole.tray.surface.get_size != tray_size

def test_render_labels_one_text():
    PlayerConsole.flashOn()
    PlayerConsole.clearTextEvents()
    PlayerConsole.registerNewEvent('test')
    texts, height =  PlayerConsole.renderTextLabels()
    assert len(texts) == 1
    assert height <= PlayerConsole.tray.surface.get_height()
    assert PlayerConsole.renderTextsToSurface(texts,height).get_size() == (PlayerConsole.tray.surface.get_width(),height)

def test_render_labels_overload():
    PlayerConsole.flashOn()
    PlayerConsole.clearTextEvents()
    global ipsum
    for x in range(5):
        PlayerConsole.registerNewEvent(ipsum)
    texts, height =  PlayerConsole.renderTextLabels()
    assert len(texts) == 14
    print PlayerConsole.tray.surface.get_height()
    assert height <= PlayerConsole.tray.surface.get_height()
    assert PlayerConsole.renderTextsToSurface(texts,height).get_size()[0] == PlayerConsole.tray.surface.get_width()
    assert PlayerConsole.renderTextsToSurface(texts,height).get_size()[1] <= PlayerConsole.tray.surface.get_height()
