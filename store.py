import marshmallow
import uuid

class Store:
    def __init__(self, name):
        self.__id = 's' +uuid.uuid4().hex
        self.__name = name
        self.__items = {}

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, item):
        self.__items[item.id] = item



class StoreController:
    def __init__(self):
        self.__stores = {}

    @property
    def stores(self):
        return self.__stores

    def register(self, store):
        self.__stores[store.id] = store
        return self

    def add_item_to_store(self, item, store):

        self.__stores[store.id].items = item

    def remove_item_from_store(self, item, store):
        if item.id in self.__stores[store.id].items.keys():
            self.__stores[store.id].items[item.id].pop()

class ItemController: #will contain all items registered to all stores
    def __init__(self):
        self.__items = {}
        self.__itemsStore = [] #link the item to know in which stores they are available


    @property
    def itemStore(self):
        return self.__itemsStore
    @itemStore.setter
    def itemStore(self, item, store):
        self.__itemsStore[item.id].append(store)
    @property
    def item(self):
        return self.__items
    def addItem(self, item):
        self.__items[item.id] = item
        return 'added item successfully'

    def removeItem(self, item):
        try:
            self.__items.pop(item.id)
        except:
            return 'item not found'



class Item:
    def __init__(self, name: str, price:float):
        self.__id = uuid.uuid4().hex
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name:str):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price:float):
        self.__price = price

    @property
    def id(self):
        return self.__id


s = StoreController()
arthur = Store('arthur')
s.register(arthur)
i = Item('itemDOIS', 302)
s.add_item_to_store(i, arthur)
print(s.stores[arthur.id].name)
print(arthur.items[i.id])