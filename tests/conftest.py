from unittest.mock import patch

import pytest

from classes.category import Category
from classes.lawngrass import LawnGrass
from classes.product import Product
from classes.smartphone import Smartphone


@pytest.fixture()
def product_samsung():
    """Фикстура Product"""
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def category_smartphones():
    products_data = [
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        },
        {
            "name": "Iphone 15",
            "description": "512GB, Gray space",
            "price": 210000.0,
            "quantity": 8,
        },
        {
            "name": "Xiaomi Redmi Note 11",
            "description": "1024GB, Синий",
            "price": 31000.0,
            "quantity": 14,
        },
    ]

    products = [Product.new_product(data) for data in products_data]

    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации,"
        " но и получение дополнительных функций для удобства жизни",
        products=products,
    )


@pytest.fixture()
def product_samsung_new():
    """Фикстура Product"""
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


@pytest.fixture()
def product_samsung_price_up():
    """Фикстура Product цена повышена"""
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 200000.0,
        "quantity": 3,
    }


@pytest.fixture()
def product_samsung_price_dp():
    """Фикстура Product цена снижена"""
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 150000.0,
        "quantity": 4,
    }


@pytest.fixture
def mock_input():
    """Фикстура для мока функции input()"""

    def _mock_input(input_values):
        return patch('builtins.input', side_effect=input_values)

    return _mock_input


@pytest.fixture()
def product_samsung_ne():
    """Фикстура Product"""
    return Product(
        **{
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )


@pytest.fixture()
def product_samsung_price_u():
    """Фикстура Product цена повышена"""
    return Product(
        **{
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 200000.0,
            "quantity": 3,
        }
    )


@pytest.fixture()
def smartphone_product_1():
    """Фикстура Smartphone(Product)"""
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    return smartphone


@pytest.fixture()
def smartphone_product_2():
    """Фикстура Smartphone(Product)"""
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    return smartphone2


@pytest.fixture()
def smartphone_product_3():
    """Фикстура Smartphone(Product)"""
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    return smartphone3


@pytest.fixture()
def lawn_grass_product_1():
    """Фикстура LawnGrass(Product)"""
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

    return grass1


@pytest.fixture()
def lawn_grass_product_2():
    """Фикстура LawnGrass(Product)"""
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    return grass2
