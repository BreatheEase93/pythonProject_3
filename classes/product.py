
from typing import Dict, Union

from classes.base_product import BaseProduct
from classes.mixins import ProductReprMixin


class Product(BaseProduct, ProductReprMixin):
    """Класс для представления товаров"""

    products_dict: Dict[str, 'Product'] = {}

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация объекта Product"""
        BaseProduct.__init__(self, name, description, price, quantity)
        ProductReprMixin.__init__(self)
        Product.products_dict[name] = self


    @classmethod
    def new_product(cls, product_data: Dict[str, Union[str, float, int]]) -> 'Product':
        """Класс-метод, который принимает на вход параметры товара в словаре
        и возвращает созданный объект класса Product"""
        new_product: "Product"
        if cls.products_dict.get(product_data["name"]):
            if product_data["price"] >= cls.products_dict[product_data["name"]].price:
                new_product = cls(
                    product_data["name"],
                    product_data["description"],
                    product_data["price"],
                    product_data["quantity"] + cls.products_dict[product_data["name"]].quantity,
                )
            else:
                new_product = cls(
                    product_data["name"],
                    product_data["description"],
                    cls.products_dict[product_data["name"]].price,
                    product_data["quantity"] + cls.products_dict[product_data["name"]].quantity,
                )
        else:
            new_product = cls(
                product_data["name"], product_data["description"], product_data["price"], product_data["quantity"]
            )

        if isinstance(new_product, Product):
            return new_product
        raise TypeError("Не удалось создать продукт")

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self._price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для цены с проверками"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        else:
            if self._price >= new_price:
                answer: str = input(
                    "Цена понижается, если уверены нажмите y(yes), а любой другой ответ отменяет действие"
                )
                if answer == "y" or answer == "yes":
                    self._price = new_price
                    print(f"Цена изменена, новая цена: {self._price}.")
                else:
                    print("Изменения отменены")
            else:
                self._price = new_price
                print(f"Цена изменена, новая цена: {self._price}.")

    def __str__(self) -> str:
        """Выводит в принт строку 'Название продукта, 80 руб. Остаток: 15 шт.'"""
        return f"{self.name}, {self.price:.1f} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Складывает продукты, в итоге получается общая стоимость всех товаров на складе."""
        if type(self) is not type(other):
            print("Возможно складывать товары только из одинаковых классов продуктов.")
            raise TypeError
        result = (self.quantity * self.price) + (other.quantity * other.price)
        return result

    def __repr__(self):
        """Представление объекта для отладки"""
        return (f"{self.__class__.__name__}("
                f"'{self.name}', "
                f"'{self.description}', "
                f"{self.price}, "
                f"{self.quantity})")
