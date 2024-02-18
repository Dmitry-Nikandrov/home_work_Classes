import pathlib, json
from classes import *

def load_json(filename):
    '''зaгружает данные из файла json'''
    url = pathlib.Path(__file__).parent.joinpath(filename)
    with open(pathlib.Path(__file__).parent.joinpath(url), 'r') as file:
        return json.load(file)


def create_Cat(load_list):
    '''создает экземляры клаcreate_Catсса Category из загруженного файла json и выводит их свойства на печать'''
    category = []
    for i in load_list:
        Cat = Category(i['name'], i['description'], i['products'][0]['name'])
        category.append(Cat)
    return category
print(create_Cat(load_json('operations.json')))
print(create_Cat(load_json('operations.json'))[1].name)

#create_Cat(load_json('operations_test.json'))
def create_Prod(load_list):
    '''создает экземляры класса Product из загруженного файла json и выводит их свойства на печать'''
    products = []
    for category in load_list:
        for i in category['products']:
            Prod = Product(i['name'], i['description'], i['price'], i['quantity'])
            products.append(Prod)
    return products
print(load_json('operations.json'))

def count_Cat(load_list):
    '''вычисляет количество категорий в экземлпряах клаcса Category'''
    category = []
    for i in load_list:
        category.append(i['name'])
    return len(category)



def count_Prod(load_list):
    '''вычисляет количество продуктов в экземлпряах клаcса Prod'''
    products = []
    for category in load_list:
        for i in category['products']:
            products.append(i['name'])
    return len(products)

