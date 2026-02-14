from typing import Union

from classes.lawngrass import LawnGrass
from classes.product import Product
from classes.smartphone import Smartphone


class Order:
    """Класс для представления заказа"""

    def __init__(self, product: Union[Product, Smartphone, LawnGrass], quantity: int) -> None:
        """Инициализация заказа"""
        self.product = product
        self.quantity = quantity
        self.total_price = self.calculate_total()

    def calculate_total(self) -> float:
        """Рассчитывает итоговую стоимость заказа."""
        return self.product.price * self.quantity

    def __repr__(self) -> str:
        """Представление заказа для отладки"""
        return f"Order(" f"product={repr(self.product)}, " f"quantity={self.quantity})"
