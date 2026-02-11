
from typing import Dict, Union


class Product:
    """Класс для представления товаров"""
    products_dict: Dict[str, 'Product'] = {}

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициирование объекта class Product"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.products_dict[name] = self

    @classmethod
    def new_product(cls, product_data: Dict[str, Union[str, float, int]]) -> 'Product':
        """Класс-метод, который принимает на вход параметры товара в словаре
        и возвращает созданный объект класса Product"""
        if cls.products_dict.get(product_data["name"]):
            if product_data["price"] >= cls.products_dict[product_data["name"]].price:
                return cls(
                    product_data["name"],
                    product_data["description"],
                    product_data["price"],
                    product_data["quantity"] + cls.products_dict[product_data["name"]].quantity)
            else:
                return cls(
                    product_data["name"],
                    product_data["description"],
                    cls.products_dict[product_data["name"]].price,
                    product_data["quantity"] + cls.products_dict[product_data["name"]].quantity)
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"]
        )

    @property
    def price(self)-> float:
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для цены с проверками"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        else:
            if self.__price >= new_price:
                answer: str = input("Цена понижается, если уверены нажмите y(yes), а любой другой ответ отменяет действие")
                if answer == "y" or answer == "yes":
                    self.__price = new_price
                    print(f"Цена изменена, новая цена: {self.__price}.")
                else:
                    print(f"Изменения отменены")
            else:
                self.__price = new_price
                print(f"Цена изменена, новая цена: {self.__price}.")

    def __str__(self):
        """Выводит в принт строку 'Название продукта, 80 руб. Остаток: 15 шт.'"""
        return f"{self.name},{self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Складывает продукты, в итоге у вас получалась полная стоимость всех товаров на складе."""
        result = (self.quantity * self.price) + (other.quantity * other.price)
        return result









