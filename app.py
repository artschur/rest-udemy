from flask import Flask
from flask_smorest import Api
from store import *
from resources.bpitem import blp as ItemBlueprint
from resources.bpstore import blp as StoreBlueprint

#
app = Flask(__name__, root_path='/api')

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

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = 'Store api oop'
app.config["API_VERSION"] = 'V1'
app.config["OPENAPI_VERSION"] = "3.1.0"
app.config["OPENAPI_URL_PREFIX"] = '/'
app.config["OPENAPI_SWAGGER_UI_PATH"] = '/swagger-ui'
app.config["OPENAPI_SWAGGER_UI_URL"] = 'https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/'

api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)


if __name__ == '__main__':
    app.run(port=5001, debug=True)

#hello

