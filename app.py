import flask
from flask import Flask, request, render_template
import store
from flask_smorest import abort

app = Flask(__name__)

aStore = store.Store('Arthur Store')
aStore.add_item('chair', 150)
aStore.add_item('white paint', 15)
aStore.add_item('water purifier', 170)

cheapStore = store.Store('Cheap Store')
cheapStore.add_item('chair', 100)
cheapStore.add_item('door', 30)
cheapStore.add_item('sink', 50)

storelist = [aStore, cheapStore]


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
    for s in storelist:
        if data["name"] == s.name:
            return 'this store already exists, try other one'

    newStore = store.Store(data["name"])
    newStore.add_item(data['item']['itemName'], data['item']['price'])
    storelist.append(newStore)
    return return_stores(), 201


    #how do i get data from the json

@app.route('/stores')
def return_stores():
    response = []
    for s in storelist:
        response.append({s.name: s.return_items()})
    return response, 201

@app.route('/store/<name>')
def return_store(name):
    for i in storelist:
        if i.name == name:
            return {i.name: i.return_items()}, 201
    return 'no store with this name', 404

@app.route('/store/<name>/addItem', methods=['POST'])
def addItem(name):
    data = request.get_json()
    itemsAdded = []
    storeExists = False
    for s in storelist:
        if s.name == name:
            storeExists = True
            for i in data['item']:
                s.add_item(i['itemName'], i['price'])
                itemsAdded.append(f'added {i["itemName"]}')
    if storeExists:
        return itemsAdded
    return 'store doesnt exist'

if __name__ == '__main__':
    app.run(port=5001, debug=True)
#hello