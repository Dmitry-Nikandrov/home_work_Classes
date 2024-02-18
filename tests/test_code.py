from classes import *
import pytest
from utils import *

@pytest.fixture
def Product_apple():
    return Product('яблоко', 'свежее', 59.99, 120)

def test_init(Product_apple):
    assert Product_apple.name == 'яблоко'
    assert Product_apple.description == 'свежее'
    assert Product_apple.price == 59.99
    assert Product_apple.amount == 120

@pytest.fixture
def Category_phone():
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации", [{
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      }])


def test_cat(Category_phone):
    assert Category_phone.name == 'Смартфоны'
    assert Category_phone.description == "Смартфоны, как средство не только коммуникации"
    assert Category_phone.product == [{
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      }]




@pytest.fixture
def test_list():
    return [{'name': 'Смартфоны', 'description': 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни', 'products': [{'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 180000.0, 'quantity': 5}, {'name': 'Iphone 15', 'description': '512GB, Gray space', 'price': 210000.0, 'quantity': 8}, {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий', 'price': 31000.0, 'quantity': 14}]}, {'name': 'Телевизоры', 'description': 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником', 'products': [{'name': '55 QLED 4K', 'description': 'Фоновая подсветка', 'price': 123000.0, 'quantity': 7}]}]


def test_load_json():
    assert load_json('operations_test.json') == [{"name": "Смартфоны","description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни","products": [{"name": "Samsung Galaxy C23 Ultra","description": "256GB, Серый цвет, 200MP камера","price": 180000.0,"quantity": 5}]}]

def test_count_Prod(test_list):
    assert count_Prod(test_list) == 4

def test_create_Prod(test_list):
    assert create_Prod(test_list)[0].name == 'Samsung Galaxy C23 Ultra'
    assert create_Prod(test_list)[1].name == 'Iphone 15'
    assert create_Prod(test_list)[2].description == '1024GB, Синий'



def test_create_Cat(test_list):
    assert create_Cat(test_list)[0].name == 'Смартфоны'
    assert create_Cat(test_list)[0].description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert create_Cat(test_list)[1].product == '55 QLED 4K'
    assert create_Cat(test_list)[1].name == 'Телевизоры'

def test_count_Cat(test_list):
    assert count_Cat(test_list) == 2

