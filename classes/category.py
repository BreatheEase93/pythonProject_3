from classes.basemodel import BaseModel
from classes.product import Product


class Category(BaseModel):
    """Класс для категории продуктов"""

    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    products: list

    def __init__(self, name: str, description: str, products: list) -> None:
        """Инициирование объекта class Category"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: 'Product') -> None:
        """Добавляет товар в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    @property
    def products(self) -> str:
        """Геттер для получения списка товаров в виде строк"""
        if not self.__products:
            return "В категории нет товаров"

        result = []
        for product in self.__products:
            result.append(str(product))

        return "\n".join(result)

    def __str__(self):
        """Вывод на str"""
        new_quantity = 0
        for product in self.__products:
            new_quantity += product.quantity

        return f"{self.name}, количество продуктов: {new_quantity} шт."

    def get_products_list(self) -> list:
        """Возвращает список товаров (список объектов Product)"""
        return self.__products[:]

    def __repr__(self) -> str:
        """Представление категории для отладки"""
        return (
            f"Category("
            f"name='{self.name}', "
            f"description='{self.description}', "
            f"products_count={len(self.__products)})"
        )

    def middle_price(self) -> float:
        """Геттер для получения средней цены"""
        try:
            quantity: int = 0
            result_add: float = 0
            products = self.get_products_list()

            if not products:
                return 0.0

            for product in products:
                quantity += product.quantity
                result_add += (product.quantity * product.price)

            result = result_add / quantity
            return result
        except ZeroDivisionError:
            return 0.0
