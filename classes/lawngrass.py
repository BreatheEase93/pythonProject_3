from classes.base_product import BaseProduct
from classes.mixins import ProductReprMixin
from classes.product import Product


class LawnGrass(Product):
    """Класс для 'Трава газонная', подкласс Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Инициирование объекта class LawnGrass"""
        BaseProduct.__init__(self, name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
        ProductReprMixin.__init__(self)

    def __repr__(self):
        """Представление объекта для отладки"""
        return (
            f"{self.__class__.__name__}("
            f"'{self.name}', "
            f"'{self.description}', "
            f"{self.price}, "
            f"{self.quantity}, "
            f"'{self.country}', "
            f"'{self.germination_period}', "
            f"'{self.color}')"
        )
