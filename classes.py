class Product:
    name: str
    description: str
    price: float
    amount: int

    def __init__(self, name, description, price, amount):
        self.name = name
        self.description = description
        self.price = price
        self.amount = amount


class Category:
    name: str
    description: str
    product: list
    total_categoris = 0
    total_products = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product
