from classes.category import Category


def test_init_category(category_smartphones):
    """Тест для инициирования в класс Category"""
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == (
        "Смартфоны, как средство не только коммуникации," " но и получение дополнительных функций для удобства жизни"
    )

    expected_output = (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 10 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )
    assert category_smartphones.products == expected_output

    assert Category.category_count == 1
    assert Category.product_count == 3

    empty_category = Category("Тест", "Описание", [])
    assert empty_category.products == "В категории нет товаров"
    assert str(category_smartphones) == "Смартфоны, количество продуктов: 32 шт."
    assert len(category_smartphones.get_products_list()) == 3
