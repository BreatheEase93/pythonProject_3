from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация объекта BaseProduct"""
        self.name = name
        self.description = description
        self._price = price  # Используем _price (одно подчеркивание) для доступа из наследников
        self.quantity = quantity

    @property
    @abstractmethod
    def price(self) -> float:
        """Геттер для цены"""
        pass
