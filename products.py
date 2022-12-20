class Product:
    def __init__(self, price, count, seller, name):
        self._price = price
        self.count = count
        self._seller = seller
        self.name = name

    def get_price(self):
        return self._price

    def get_seller(self):
        return self._seller

class Book(Product):
    def __init__(self, author, price, count, seller, name):
        super().__init__(price, count, seller, name)
        self.author = author


class Phone(Product):
    def __init__(self, model, price, count, seller, name):
        super().__init__(price, count, seller, name)
        self.model = model


products_in_stock = []
