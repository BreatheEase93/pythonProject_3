import pytest

from classes.product import Product


def test_product_initialization(product_samsung):
    """Тест инициализации продукта"""
    assert product_samsung.name == "Samsung Galaxy C23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


def test_product_initialization_value_error():
    """Тест инициализации продукта ValueError"""
    with pytest.raises(ValueError, match='Товар с нулевым количеством не может быть добавлен'):
        Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0)
