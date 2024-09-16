from flask_smorest import Blueprint, abort
from store import *
from flask.views import MethodView
from flask import request

blp = Blueprint('item', __name__, url_prefix='/items')


@blp.route('/<string:uid>')
class Itembp(MethodView):
    def get(self, uid):
        itemschema = ItemSchema()
        try:
            return itemschema.dump(i.items[uid])
        except KeyError:
            abort(404)

    def put(self, uid):
        item_data = request.get_json()
        if "price" not in item_data or "name" not in item_data:
            abort(400, message="Missing 'price' and 'name' fields")
        itemschema = ItemSchema()
        try:
            item = i.items[uid]
            item.name = item_data["name"]
            item.price = item_data["price"]
            # updates the dicts
            return itemschema.dump(item)
        except KeyError:
            abort(404)

    def delete(self, uid):
        try:
            item = i.items[uid]  # Find the item
            i.removeItem(item)  # Remove it from ItemController and all stores
            return f'Item deleted successfully from stores', 200
        except KeyError:
            abort(404, message="Item not found")
