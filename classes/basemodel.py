from abc import ABC, abstractmethod


class BaseModel(ABC):
    """Абстрактный базовый класс для моделей Order и Category"""

    def __init__(self):
        """Базовый конструктор"""
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """Абстрактный метод для строкового представления объекта"""
        pass

    def __str__(self) -> str:
        """Базовый метод строкового представления объекта для пользователя"""
        return self.__repr__()
