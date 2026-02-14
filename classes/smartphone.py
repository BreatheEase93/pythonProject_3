from classes.base_product import BaseProduct
from classes.mixins import ProductReprMixin
from classes.product import Product


class Smartphone(Product):
    """Класс для 'смартфононов', подкласс Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Инициирование объекта class Smartphone"""
        BaseProduct.__init__(self, name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        ProductReprMixin.__init__(self)

    def __repr__(self):
        return (
            f"Smartphone("
            f"'{self.name}', "
            f"'{self.description}', "
            f"{self.price}, "
            f"{self.quantity}, "
            f"{self.efficiency}, "
            f"'{self.model}', "
            f"{self.memory}, "
            f"'{self.color}')"
        )
