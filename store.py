
stores = []


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item: str, price: int):
        self.items.append({item: price})

    def return_items(self):
        return self.items


