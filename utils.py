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
        print(Cat.name)
        print(Cat.description)
        print(Cat.product)
        print('\n')
    return category

create_Cat(load_json('operations_test.json'))
def create_Prod(load_list):
    '''создает экземляры класса Product из загруженного файла json и выводит их свойства на печать'''
    products = []
    for category in load_list:
        for i in category['products']:
            Prod = Product(i['name'], i['description'], i['price'], i['quantity'])
            products.append(Prod)
            print(Prod.name)
            print(Prod.description)
            print(Prod.price)
            print(Prod.amount)
            print('\n')
        return products.append(Prod)

def count_Cat(load_list):
    '''вычисляет количество категорий в экземлпряах клаcса Category'''
    category = []
    for i in load_list:
        category.append(i['name'])
    print(f'Количество категорий - {len(category)}')
    return len(category)

print(pathlib.Path(__file__).parent.joinpath('operations.json'))
print(load_json('operations.json'))
print(count_Cat(load_json('operations.json')))


def count_Prod(load_list):
    '''вычисляет количество продуктов в экземлпряах клаcса Prod'''
    products = []
    for category in load_list:
        for i in category['products']:
            products.append(i['name'])
    return f'Количество уникальных продуктов - {len(products)}'

print(count_Prod(load_json('operations.json')))
print(create_Prod(load_json('operations.json')))