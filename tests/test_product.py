def test_init_product(product_samsung):
    """Тест для инициирования в класс Product"""
    assert product_samsung.name == "Samsung Galaxy C23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5
