class ProductQuantityError(Exception):
    """Ошибка, возникающая при попытке добавить товар с нулевым количеством"""

    def __init__(self, message="Количество товара должно быть больше 0"):
        self.message = message
        super().__init__(self.message)
