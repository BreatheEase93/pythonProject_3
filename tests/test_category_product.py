import pytest

from classes.category_product import CategoryProductIterator


def test_iterator_with_multiple_products(category_smartphones):
    """Проверка итераторного перебора товаров в категории с несколькими товарами"""
    iterator = CategoryProductIterator(category_smartphones)

    # Прверяем первую итерацию
    first_pass = list(iterator)
    assert len(first_pass) == 3
    assert first_pass[0].name == "Samsung Galaxy C23 Ultra"
    assert first_pass[1].name == "Iphone 15"
    assert first_pass[2].name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(iterator)
