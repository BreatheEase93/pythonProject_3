class Product:
    """Класс для представления разработчиков"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициирование объекта class Product"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
