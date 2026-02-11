from classes.category import Category


class CategoryProductIterator:
    """Итератор, позволяющий перебирать товары одной категории"""

    def __init__(self, category: Category):
        """Инициализирует итератор."""
        if not isinstance(category, Category):
            raise TypeError('Аргумент должен быть объектом класса Category.')
        self.products = list(category.get_products_list())
        self.index = 0

    def __iter__(self):
        """Возвращает итератора."""
        return self

    def __next__(self):
        """Получает следующий продукт из списка."""
        if self.index < len(self.products):
            current_product = self.products[self.index]
            self.index += 1
            return current_product
        else:
            raise StopIteration()