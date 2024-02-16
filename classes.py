class Product:
  name: str
  discription: str
  price: float
  amount: int
  def __init__ (self, name, discription, price, amount):
    self.name = name
    self.discription = discription
    self.price = price
    self.amount = amount


class Category:
  name: str
  discription: str
  goods: list
  total_categoris = len()
  total_products = 0
  def __init__ (self, name, discription, product):
      self.name = name
      self.discription = discription
      self.product = product





category_fruit = Category("Фрукты", "Сезонные", ["Яблоки","Вкусные", 89.91, 120])
print(category_fruit.product)