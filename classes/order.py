from classes.basemodel import BaseModel
from classes.error.p_roduct_1quantity_error import ProductQuantityError
from classes.product import Product


class Order(BaseModel):
    """Класс для представления заказа"""

    def __init__(self, products: list) -> None:
        """Инициализация заказа"""
        self.products = []
        self.total_price = 0.0

        # Добавляем товары с проверкой количества
        for product in products:
            try:
                self.add_product(product)
                print(f"Товар '{product.name}' успешно добавлен в заказ")
            except ProductQuantityError as e:
                print(f"Ошибка: {e}")
            finally:
                print(f"Добавление товара '{product.name if hasattr(product, 'name')else 'неизвестный'}' завершена")

        self.total_price = self.calculate_total()

    def add_product(self, product: Product) -> None:
        """Добавляет товар в заказ с проверкой количества"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")

        # Проверяем количество товара
        if product.quantity <= 0:
            raise ProductQuantityError(f"Нельзя добавить в заказ товар '{product.name}' с нулевым количеством")

        self.products.append(product)

    def calculate_total(self) -> float:
        """Рассчитывает итоговую стоимость заказа."""
        total = 0.0
        for product in self.products:
            total += product.price * product.quantity
        return total

    def __repr__(self) -> str:
        """Представление заказа для отладки"""
        products_info = ", ".join([f"{p.name} (x{p.quantity})" for p in self.products])
        return f"Order(products=[{products_info}], total_price={self.total_price})"
