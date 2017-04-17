from inventoryUI import InventoryUI
from hotbarUI import HotbarUI
from buffalo import utils
from inventory import Inventory
from guiManager import GUIManager
from item import Item

utils.init()

#####################
###INVENTORY TESTS###
#####################
def test_init_inventory():
	i = Inventory()
	g = GUIManager()
	ui = InventoryUI(i,g)
	assert ui.inventory
	assert ui.pos
	assert ui.itemRects is not None
	assert ui.guiManager
	assert ui.surface.get_size() == (ui.inventory.INV_SIZE_X * (InventoryUI.BUTTON_SIZE + InventoryUI.PADDING) + InventoryUI.PADDING,
		ui.inventory.INV_SIZE_Y * (InventoryUI.BUTTON_SIZE + InventoryUI.PADDING) + InventoryUI.PADDING)

def test_getGUIPosFromItemPos():
	i = Inventory()
	g = GUIManager()
	ui = InventoryUI(i,g)
	assert ui.getGUIPosFromItemPos((0,0)) == (6,6)
	assert ui.getGUIPosFromItemPos((3,3)) == (120,120)
	assert ui.getGUIPosFromItemPos((10,1)) == (386, 44)

def test_getItemFromGUIPos():
	i = Inventory()
	g = GUIManager()
	ui = InventoryUI(i,g)
	item1 = Item("1")
	item2 = Item("2")
	item3 = Item("3")
	i.items[0][0] = item1
	i.items[2][2] = item2
	i.items[5][1] = item3
	assert ui.getItemFromGUIPos(ui.getGUIPosFromItemPos((0,0))) == item1
	assert ui.getItemFromGUIPos(ui.getGUIPosFromItemPos((2,2))) == item2
	assert ui.getItemFromGUIPos(ui.getGUIPosFromItemPos((5,1))) == item3
	assert ui.getItemFromGUIPos(ui.getGUIPosFromItemPos((1,1))) is None

##################
###HOTBAR TESTS###
##################
def test_init_hotbar():
	i = Inventory()
	g = GUIManager()
	ui = HotbarUI(i,g)
	assert ui.inventory
	assert ui.pos
	assert ui.itemRects is not None
	assert ui.guiManager
	assert ui.selectedIndex == 0
	assert ui.surface.get_size() == (ui.inventory.INV_SIZE_X * (InventoryUI.BUTTON_SIZE + InventoryUI.PADDING) + InventoryUI.PADDING,
		1 * (InventoryUI.BUTTON_SIZE + InventoryUI.PADDING) + InventoryUI.PADDING)

def test_getGUIPosFromItemPos():
	i = Inventory()
	g = GUIManager()
	ui = HotbarUI(i,g)
	assert ui.getGUIPosFromItemPos((0,0)) == (6,6)
	assert ui.getGUIPosFromItemPos((3,3)) == (120,6)
	assert ui.getGUIPosFromItemPos((10,1)) == (386, 6)

def test_getItemFromGUIPos():
	i = Inventory()
	g = GUIManager()
	ui = HotbarUI(i,g)
	item1 = Item("1")
	item2 = Item("2")
	item3 = Item("3")
	i.hotbar[0] = item1
	i.hotbar[2] = item2
	i.hotbar[5] = item3
	assert ui.getItemFromGUIPos(ui.getGUIPosFromItemPos((0,0))) == item1
	assert ui.getItemFromGUIPos(ui.getGUIPosFromItemPos((2,2))) == item2
	assert ui.getItemFromGUIPos(ui.getGUIPosFromItemPos((5,1))) == item3
	assert ui.getItemFromGUIPos(ui.getGUIPosFromItemPos((1,1))) is None
	
