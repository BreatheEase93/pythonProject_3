from classes.product import Product


def test_init_product(product_samsung):
    """Тест для инициирования в класс Product"""
    assert product_samsung.name == "Samsung Galaxy C23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


def test_new_product_class_method(product_samsung_new, product_samsung_price_up, product_samsung_price_dp):
    """Тест для классового метода new_product"""

    product1 = Product.new_product(product_samsung_new)
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.price == 180000.0
    assert product1.quantity == 5

    product2 = Product.new_product(product_samsung_price_up)
    assert product2.name == "Samsung Galaxy S23 Ultra"
    assert product2.price == 200000.0
    assert product2.quantity == 8

    product3 = Product.new_product(product_samsung_price_dp)
    assert product3.name == "Samsung Galaxy S23 Ultra"
    assert product3.price == 200000.0
    assert product3.quantity == 12




def test_price_setter_increase(mock_input):
    """Тест сеттера цены при повышении"""
    product = Product("Samsung Galaxy S23", "256GB, Серый цвет, 100MP камера", 100000.0, 5)

    product.price = 110000
    assert product.price == 110000

    product.price = -110000
    assert product.price == 110000

    with mock_input(["y"]):
        product.price = 80000
        assert product.price == 80000

    with mock_input(["sdfsdf"]):
        product.price = 70000
        assert product.price == 80000


def test_price_str(product_samsung_ne, product_samsung_price_u):
    """Тест __str__ и __add__"""
    assert str(product_samsung_ne) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product_samsung_price_u) == "Samsung Galaxy S23 Ultra, 200000.0 руб. Остаток: 3 шт."
    expected_sum = (
        product_samsung_ne.quantity * product_samsung_ne.price
        + product_samsung_price_u.quantity * product_samsung_price_u.price
    )
    assert (product_samsung_ne + product_samsung_price_u) == expected_sum
