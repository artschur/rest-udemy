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
s.add_item_to_store(suco, aStore, i)
s.add_item_to_store(suco, lStore, i)
s.add_item_to_store(leite, aStore, i)




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

@app.get('/store/<uid>')
def return_store(uid):
    store_schema = StoreSchema()
    try:
        store = s.stores[uid]  # Get the store object by its ID
        return store_schema.dump(store)
    except KeyError:
        abort(404)


@app.delete('/store/<uid>')
def delete_store(uid):
    del s.stores[uid]
    return 'store deleted'

@app.put('/store/<uid>')
def update_store(uid):
    data = request.get_json()
    try:
        s.stores[uid].name = data['name']
        return f"{s.stores[uid]} changed successfully to {data['name']}"
    except KeyError:
        return abort(404)

@app.post('/store/<uid>/addItem')
def addItem(uid):
    data = request.get_json()
    new = Item(data['item']['name'], data['item']['price'])
    i.addItem(new)
    s.add_item_to_store(new, s.stores[uid], i)
    return f'{data['item']['name']} added to store {uid}'

@app.get('/store/<uid>/items')
def return_items(uid):
    itemSchema = ItemSchema(many=True)
    item_list = list(s.stores[uid].inventory.values())
    return itemSchema.dump(item_list)


@app.get('/items/<itemuid>')
def return_item_by_id(itemuid):
    itemschema = ItemSchema()
    try:
        return itemschema.dump(i.items[itemuid])
    except KeyError:
        abort(404)

@app.put('/items/<itemuid>')
def update_item(itemuid):
    item_data = request.get_json()
    if "price" not in item_data or "name" not in item_data:
        abort(400, message="Missing 'price' and 'name' fields")
    itemschema = ItemSchema()
    try:
        item = i.items[itemuid]
        item.name = item_data["name"]
        item.price = item_data["price"]
        #updates the dicts
        return itemschema.dump(item)
    except KeyError:
        abort(404)


@app.delete('/items/<itemuid>')
def delete_item(itemuid):
    try:
        item = i.items[itemuid]  # Find the item
        i.removeItem(item)  # Remove it from ItemController and all stores
        return f'Item deleted successfully from stores', 200
    except KeyError:
        abort(404, message="Item not found")


if __name__ == '__main__':
    app.run(port=5001, debug=True)
#hello

