from item import Item
import random
from floatingText import FloatingText,FloatingTextManager

class Inventory():

    def __init__(self, **kwargs):

        self.INV_SIZE_X = 10
        self.INV_SIZE_Y = 3

        self.items = [[None]*self.INV_SIZE_Y for _ in range(self.INV_SIZE_X)]
        self.hotbar = [None]*self.INV_SIZE_X
        self.hotbarSelection = 0

        self.items[0][0] = Item("dagger")
        self.items[0][0].quantity = 2
        self.items[1][0] = Item("book")
        self.items[1][0].quantity = 10
        self.items[2][0] = Item("test")
        self.update()

    def addItem(self, item):
        for x in range(self.INV_SIZE_X):
            if self.hotbar[x] == None and isinstance(item, Item):
                self.hotbar[x] = item
                return
        for x in range(self.INV_SIZE_X):
            for y in range(self.INV_SIZE_Y):
                if self.items[x][y] == None and isinstance(item, Item):
                    self.items[x][y] = item
                    return


    def addItemQuantity(self,item, quantity):
        pass

    def removeItem(self, item):
        for x in range(self.INV_SIZE_X):
            if self.hotbar[x] == item:
                self.hotbar[x] = None
                return
        for x in range(self.INV_SIZE_X):
            for y in range(self.INV_SIZE_Y):
                if self.items[x][y] == item:
                    self.items[x][y] = None
                    return

    def removeItemQuantity(self, item, quantity):
        quantityRemoved = 0;
        for x in range(self.INV_SIZE_X):
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
        for x in range(self.INV_SIZE_X):
            for y in range(self.INV_SIZE_Y):
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
        for x in range(self.INV_SIZE_X):
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
        for x in range(self.INV_SIZE_X):
            for y in range(self.INV_SIZE_Y):
                if self.items[x][y] is not None:
                    if self.items[x][y].name == item:
                        quantity += self.items[x][y].quantity
        for x in range(self.INV_SIZE_X):
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
        for x in range(self.INV_SIZE_X):
            for y in range(self.INV_SIZE_Y):
                if self.items[x][y] is not None and self.items[x][y].quantity <= 0:
                    self.items[x][y] = None
                if self.items[x][y] is not None:
                    self.items[x][y].update()
        for x in range(self.INV_SIZE_X):
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
            FloatingTextManager.ACTIVE_FLOATING_TEXTS.append(FloatingText(
                    "+" + str(item.quantity) + " " + item.name,
                    (self.playerCharacter().fPos[0], self.playerCharacter().fPos[1] + offsetY),
                    vert_speed = -1,
                    hor_speed = -1,
                    alpha_decay = 5,
                    lifetime = 50))
            offsetY += offsetPerNotification
