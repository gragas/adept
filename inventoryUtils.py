from inventory import Inventory
from eventRegistry import EventRegistry
from playerConsole import PlayerConsole
from camera import Camera
from item import Item
from floatingText import FloatingTextManager
from floatingText import FloatingText

class InventoryUtils:
    @staticmethod
    def init():
        EventRegistry.registerListener(InventoryUtils.add_item_listener,"inv_add")
        EventRegistry.registerListener(InventoryUtils.craft_listener,"craft")

    @staticmethod
    def add_item_listener(event):
        #PlayerConsole.registerNewEvent("+" + str(event.info["item"].quantity) + " " + str(event.info['item'].name))
        pass

    @staticmethod
    def craft_listener(event):
        offsetY = 0
        offsetPerNotification = 10
        playerCharacter = Camera.character

        if playerCharacter is None:
            return
        for item in event.info['recipe'].products:
            item = Item(item)
            item.quantity = event.info['recipe'].products[item.name]
            FloatingTextManager.registerFloatingText(FloatingText(
                       "+" + str(item.quantity) + " " + item.name,
                       (playerCharacter.fPos[0], playerCharacter.fPos[1] + offsetY),
                       vert_speed = -1,
                       hor_speed = -1,
                       alpha_decay = 5,
                       lifetime = 50))
            offsetY += offsetPerNotification
            PlayerConsole.registerNewEvent("You crafted " + str(item.quantity) + " " + item.name + "(s)!", color=(255,0,0,255))
            
