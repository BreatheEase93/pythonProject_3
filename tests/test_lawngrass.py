def test_init_lawn_grass(lawn_grass_product_1):
    """Тест для инициализации класса LawnGrass"""
    assert lawn_grass_product_1.name == "Газонная трава"
    assert lawn_grass_product_1.description == "Элитная трава для газона"
    assert lawn_grass_product_1.price == 500.0
    assert lawn_grass_product_1.quantity == 20
    assert lawn_grass_product_1.country == "Россия"
    assert lawn_grass_product_1.germination_period == "7 дней"
    assert lawn_grass_product_1.color == "Зеленый"
