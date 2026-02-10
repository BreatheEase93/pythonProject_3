from classes.product import Product


class Category:
    """Класс для представления разработчиков"""

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

    def add_product(self, product: 'Product'):
        """Добавляет товар в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    @property
    def products(self)-> str:
        """Геттер для получения списка товаров в виде строк"""
        if not self.__products:
            return "В категории нет товаров"

        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")

        return "\n".join(result)


