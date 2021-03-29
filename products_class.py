import csv
from typing import List


class Product:
    def __init__(self, name: str, price: float, discount: float):
        self.name = name
        self.price = price
        self.discount = discount

    @property
    def name(self):
        return self.name

    @property
    def price(self):
        return self.price

    @property
    def discount(self):
        return self.discount

    @price.setter
    def price(self, value):
        self._price = value

    @name.setter
    def name(self, value):
        self._name = value

    @discount.setter
    def discount(self, value):
        self._discount = value

    def __repr__(self):
        return f"{self.name, self.price, self.discount}"


class ProductProvider:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _fetch_from_file(self) -> List[Product]:
        products = []
        try:
            with open(self.db_path, "r") as fd:
                reader = csv.reader(fd)
                for line in reader:
                    if line:
                        product = Product(str(line[0]), float(line[1]), float(line[2]))
                        products.append(product)
        except IOError as ie:
            print(f'Problem while reading from product database. More info {ie.args}')
        return products

    def get_products(self) -> List[Product]:
        return self._fetch_from_file()


if __name__ == "__main__":
    prodotto = ProductProvider("./products_base.csv")
    print(prodotto.get_products())
