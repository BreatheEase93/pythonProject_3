
from typing import List, Dict


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
    def new_product(cls, my_list: List) -> 'Product':
        """Класс-метод, который принимает на вход параметры товара в словаре
        и возвращает созданный объект класса Product"""
        if cls.products_dict.get(my_list[0]["name"]):
            if my_list[0]["price"] >= cls.products_dict[my_list[0]["name"]].price:
                return cls(
                    my_list[0]["name"],
                    my_list[0]["description"],
                    my_list[0]["price"],
                    my_list[0]["quantity"] + cls.products_dict[my_list[0]["name"]].quantity)
            else:
                return cls(
                    my_list[0]["name"],
                    my_list[0]["description"],
                    cls.products_dict[my_list[0]["name"]].price,
                    my_list[0]["quantity"] + cls.products_dict[my_list[0]["name"]].quantity)
        return cls(
            my_list[0]["name"],
            my_list[0]["description"],
            my_list[0]["price"],
            my_list[0]["quantity"]
        )

    @property
    def setting_price(self)-> float:
        """Геттер для цены"""
        return self.__price

    @setting_price.setter
    def setting_price(self, new_price: float):
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








