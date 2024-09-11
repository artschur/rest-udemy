from marshmallow import Schema, fields
import uuid
# Schema for the Item class


class ItemSchema(Schema):
    id = fields.Str(dump_only=True)  # Automatically generated, so only for output
    name = fields.Str(required=True)
    price = fields.Float(required=True)


# Schema for the Store class
class StoreSchema(Schema):
    id = fields.Str(dump_only=True)  # Automatically generated
    name = fields.Str(required=True)


class Store:
    def __init__(self, name):
        self.__id = 's' +uuid.uuid4().hex
        self.__name = name
        self.__inventory = {}

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def inventory(self):
        return self.__inventory

    @inventory.setter
    def inventory(self, item):
        self.__inventory[item.id] = item


class StoreController:
    def __init__(self):
        self.__stores = {}

    @property
    def stores(self):
        return self.__stores

    def register(self, store: Store):
        self.__stores[store.id] = store
        return self

    def add_item_to_store(self, item, store):
        self.__stores[store.id].inventory = item
        i.link_item_store(item,store)

    def remove_item_from_store(self, item, store):
        if item.id in self.__stores[store.id].items.keys():
            self.__stores[store.id].items[item.id].pop()


class ItemController:  # will contain all items registered to all stores
    def __init__(self):
        self.__items = {}
        self.__itemsStore = {}   #l ink the item to know in which stores they are available

    @property
    def itemStore(self):
        return self.__itemsStore

    def link_item_store(self, item, store):
        self.__itemsStore[item.id] = store

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
i = ItemController()
aStore = Store('a')
leite = Item(name='leite', price=1.0)
i.addItem(leite)
s.register(aStore)
lStore = Store('lucas')
s.register(lStore)
s.add_item_to_store(leite, aStore)


