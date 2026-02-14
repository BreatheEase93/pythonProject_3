
class ProductReprMixin:
    """Миксин для печати информации о создании объекта"""

    verbose_creation = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.__class__.verbose_creation:
            print(f"Создан объект: {self.__repr__()}")
