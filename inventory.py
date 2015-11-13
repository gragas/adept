from item import Item
import random
from floatingText import FloatingText,FloatingTextManager
from playerConsole import PlayerConsole
from serializable import Serializable
import weakref


class Inventory(Serializable):
    INV_SIZE_X = 10
    INV_SIZE_Y = 3

    def __init__(self, **kwargs):
        self.items = kwargs.get("items",[[None]*3 for _ in range(10)])
        self.hotbar = kwargs.get("hotbar",[None]*10)
        self.hotbarSelection = kwargs.get("hotbarSelection",0)

        #Creating a blank weakref
        o = Item()
        self.playerCharacter = weakref.ref(o)
        del(o)
        
        self.update()

    def addItem(self, item):
        for x in range(Inventory.INV_SIZE_X):
            if self.hotbar[x] != None and self.hotbar[x].name == item.name:
                self.hotbar[x].quantity += item.quantity
                return
            if self.hotbar[x] == None and isinstance(item, Item):
                self.hotbar[x] = item
                return
        for x in range(Inventory.INV_SIZE_X):
            for y in range(Inventory.INV_SIZE_Y):
                if self.items[x][y] != None and self.items[x][y].name == item.name:
                    self.items[x][y].quantity += item.quantity
                    return
                if self.items[x][y] == None and isinstance(item, Item):
                    self.items[x][y] = item
                    return

    def removeItem(self, item):
        for x in range(Inventory.INV_SIZE_X):
            if self.hotbar[x] == item:
                self.hotbar[x] = None
                return
        for x in range(Inventory.INV_SIZE_X):
            for y in range(Inventory.INV_SIZE_Y):
                if self.items[x][y] == item:
                    self.items[x][y] = None
                    return

    def removeItemQuantity(self, item, quantity):
        """
        NOTE: Takes an item NAME as the 'item' param, not an Item object.
        """
        quantityRemoved = 0;
        for x in range(Inventory.INV_SIZE_X):
            if self.hotbar[x] is not None and self.hotbar[x].name == item:
                currItem = self.hotbar[x]
                if currItem.quantity > quantity:
                    currItem.quantity -= quantity
                    quantityRemoved = quantity
                elif currItem.quantity <= quantity:
                    quantityRemoved += currItem.quantity
                    self.hotbar[x] = None 
                if(quantityRemoved >= quantity):
                    return
        for x in range(Inventory.INV_SIZE_X):
            for y in range(Inventory.INV_SIZE_Y):
                if self.items[x][y] is not None and self.items[x][y].name == item:
                    currItem = self.items[x][y]
                    if currItem.quantity > quantity:
                        currItem.quantity -= quantity
                        quantityRemoved = quantity
                    elif currItem.quantity <= quantity:
                        quantityRemoved += currItem.quantity
                        self.items[x][y] = None 
                    if(quantityRemoved >= quantity):
                        return

    def removeHotbarItem(self,item):
        for x in range(Inventory.INV_SIZE_X):
            if self.hotbar[x] == item:
                self.hotbar[x] = None
                return

    def placeItem(self, item, pos):
        if isinstance(item,Item):
            oldItem = self.items[int(pos[0])][int(pos[1])]
            self.items[int(pos[0])][int(pos[1])] = item
            return oldItem

    def placeItemInHotbar(self, item, pos):
        if isinstance(item,Item):
            oldItem = self.hotbar[pos[0]]
            self.hotbar[pos[0]] = item
            return oldItem
        

    def getTotalItemQuantity(self, item):
        """
        Gets total quantity held of a specific item accross all stacks within Inventory
        """
        quantity = 0;
        for x in range(Inventory.INV_SIZE_X):
            for y in range(Inventory.INV_SIZE_Y):
                if self.items[x][y] is not None:
                    if self.items[x][y].name == item:
                        quantity += self.items[x][y].quantity
        for x in range(Inventory.INV_SIZE_X):
            if self.hotbar[x] is not None:
                if self.hotbar[x].name == item:
                    quantity += self.hotbar[x].quantity
        return quantity


    def addItemToHotbar(item):
        for x in range(INV_SIZE_X):
            if hotbar[x] == None:
                hotbar[x] = item
                return

    def update(self):
        for x in range(Inventory.INV_SIZE_X):
            for y in range(Inventory.INV_SIZE_Y):
                if self.items[x][y] is not None and self.items[x][y].quantity <= 0:
                    self.items[x][y] = None
                if self.items[x][y] is not None:
                    self.items[x][y].update()
        for x in range(Inventory.INV_SIZE_X):
                if self.hotbar[x] is not None and self.hotbar[x].quantity <= 0:
                    self.hotbar[x] = None
                if self.hotbar[x] is not None:
                    self.hotbar[x].update()

    def craftingNotification(self,recipe):
        offsetY = 0
        offsetPerNotification = 10

        if self.playerCharacter() is None:
            return
        for item in recipe.products:
            item = Item(item)
            item.quantity = recipe.products[item.name]
#            FloatingTextManager.ACTIVE_FLOATING_TEXTS.append(FloatingText(
#                    "+" + str(item.quantity) + " " + item.name,
#                    (self.playerCharacter().fPos[0], self.playerCharacter().fPos[1] + offsetY),
#                    vert_speed = -1,
#                    hor_speed = -1,
#                    alpha_decay = 5,
#                    lifetime = 50))
            offsetY += offsetPerNotification
            PlayerConsole.registerNewEvent("You crafted " + str(item.quantity) + " " + item.name + "(s)!", (255,0,0,255))