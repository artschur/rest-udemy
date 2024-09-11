import flask
from flask import Flask, request, render_template

from flask_smorest import abort
from store import *
#
app = Flask(__name__)

store_schema = StoreSchema()
s = StoreController()
i = ItemController()
aStore = Store('a')
lStore = Store('lucas')
s.register(lStore)
s.register(aStore)
leite = Item(name='leite', price=1.0)
suco = Item(name='suco', price=5.0)
i.addItem(leite)
i.addItem(suco)
s.add_item_to_store(suco, aStore)
s.add_item_to_store(suco, lStore)
s.add_item_to_store(leite, aStore)




# @app.route('/store/<name>/<item>', methods=['GET'])
# def storeItem(name, item):
#     if meth
#     newStore = store.Store(name)
#     newStore.add_item(item)
#     storelist.append(newStore)
#     return {newStore.name:newStore.return_items()}

@app.route('/addstore', methods=['POST'])
def addStore():
    data = request.get_json()
    s.register(Store(data['store']['name']))
    return s.stores


    #how do i get data from the json

@app.route('/stores')
def return_stores():
    store_schema = StoreSchema(many=True)  # Since it's a list of stores, we set many=True
    store_list = list(s.stores.values())   # Extracting the store objects (values of the dictionary)
    return store_schema.dump(store_list)

@app.route('/store/<uid>')
def return_store(uid):
    store_schema = StoreSchema()
    try:
        store = s.stores[uid]  # Get the store object by its ID
        return store_schema.dump(store)
    except KeyError:
        abort(404)

@app.route('/store/<uid>/addItem', methods=['POST'])
def addItem(uid):
    data = request.get_json()
    new = Item(data['item']['name'], data['item']['price'])
    i.addItem(new)
    s.add_item_to_store(new, s.stores[uid])

@app.route('/store/<uid>/items', methods=['GET'])
def return_items(uid):
    itemSchema = ItemSchema(many=True)
    item_list = list(s.stores[uid].inventory.values())
    return itemSchema.dump(item_list)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
#hello