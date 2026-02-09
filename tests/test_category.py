

def test_init_product(product_smartphones):
    """Тест для инициирования в класс Product"""
    assert product_smartphones.name == "Смартфоны"
    assert product_smartphones.description == ("Смартфоны, как средство не только коммуникации,"
                                               " но и получение дополнительных функций для удобства жизни")
    assert product_smartphones.products == [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      },
      {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }
    ]