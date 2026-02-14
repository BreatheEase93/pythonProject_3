import io
from contextlib import redirect_stdout

from classes.mixins import ProductReprMixin
from classes.smartphone import Smartphone


def test_smartphone_repr_mixin_output():
    f = io.StringIO()
    with redirect_stdout(f):
        # Включаем печать для этого теста
        ProductReprMixin.verbose_creation = True
        Smartphone(
            "Samsung G Ultra", "256GB, Серый цвет, 200MP камера",
            180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
        )
        ProductReprMixin.verbose_creation = False

    output = f.getvalue().strip()
    expected = ("Создан объект: Smartphone('Samsung G Ultra', '256GB, Серый цвет,"
                " 200MP камера', 180000.0, 5, 95.5, 'S23 Ultra', 256, 'Серый')")
    assert output == expected
