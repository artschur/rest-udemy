from flask.views import MethodView
from flask_smorest import Blueprint, abort


from store import *

from flask import request
blp = Blueprint('store', __name__, description="Operations on stores", url_prefix='/store')


@blp.route("/<string:uid>")
class Storebp(MethodView):
    def get(self, uid):
        store_schema = StoreSchema()
        try:
            store = s.stores[uid]  # Get the store object by its ID
            return store_schema.dump(store)
        except KeyError:
            abort(404)

    def delete(self, uid):
        del s.stores[uid]
        return 'store deleted'

    def put(self, uid):
        data = request.get_json()
        try:
            s.stores[uid].name = data['name']
            return f"{s.stores[uid]} changed successfully to {data['name']}"
        except KeyError:
            return abort(404)


@blp.route("/add")
class StoreAdd(MethodView):
    def post(self):
        store_schema = StoreSchema(many=True)
        data = request.get_json()
        s.register(store.Store(data['store']['name']))
        return store_schema.dump(s.stores)


@blp.route("")
class Store(MethodView):
    def get(self):
        store_schema = StoreSchema(many=True)  # Since it's a list of stores, we set many=True
        store_list = list(s.stores.values())  # Extracting the store objects (values of the dictionary)
        return store_schema.dump(store_list)

@blp.route("/<uid>/items")
class StoreItem(MethodView):
    def post(self, uid):
        data = request.get_json()
        new = Item(data['item']['name'], data['item']['price'])
        i.addItem(new)
        s.add_item_to_store(new, s.stores[uid], i)
        return f'{data['item']['name']} added to store {uid}'


    def get(self, uid):
        itemSchema = ItemSchema(many=True)
        item_list = list(s.stores[uid].inventory.values())
        return itemSchema.dump(item_list)

@blp.route("/<uid>/items/<itemuid>")
class StoreDeleteItem(MethodView):
    def delete(self, uid, itemuid):
        itemschema = ItemSchema(many=True)
        del s.stores[uid].inventory[itemuid]
        return itemschema.dump(s.stores[uid].inventory)

