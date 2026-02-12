def test_init_smartphone(smartphone_product_1):
    """Тест для инициализации класса Smartphone"""
    assert smartphone_product_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_product_1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_product_1.price == 180000.0
    assert smartphone_product_1.quantity == 5
    assert smartphone_product_1.efficiency == 95.5
    assert smartphone_product_1.model == "S23 Ultra"
    assert smartphone_product_1.memory == 256
    assert smartphone_product_1.color == "Серый"