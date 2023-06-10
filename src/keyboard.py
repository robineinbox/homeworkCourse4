from src.item import Item
from src.mixin import LanguageMixin


class Keyboard(LanguageMixin, Item):
    """
    Класс для представления товара "клавиатура" с возможностью изменения языка.
    """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.language = 'EN'

    def __str__(self) -> str:
        return self.name














# from src.item import Item
#
#
# class Keyboard(Item):
#     """
#     Класс для представления товара "клавиатура".
#     """
#
#     def __init__(self, name: str, price: float, quantity: int) -> None:
#         super().__init__(name, price, quantity)
#         self.language = 'EN'
#
#     def __str__(self) -> str:
#         return self.name






















    # from src.item import Item
    # def change_lang(self):
    #     pass
# from src.mixin import KeyboardMixin
#
#
# class Keyboard(Item, KeyboardMixin):
#     """
#     Класс для представления клавиатуры в магазине.
#     """
#
#     def __init__(self, name: str, price: float, quantity: int) -> None:
#         """
#         Создает экземпляр класса Keyboard.
#         :param name: Название клавиатуры.
#         :param price: Цена за единицу клавиатуры.
#         :param quantity: Количество клавиатур в магазине.
#         """
#         super().__init__(name, price, quantity)
#         self.language = 'EN'
#
#     def __str__(self) -> str:
#         """
#         Возвращает название клавиатуры.
#         :return: Название клавиатуры.
#         """
#         return self.name











# from src.item import Item
#
#
# class Keyboard(Item):
#     """
#     Класс для представления клавиатуры в магазине.
#     """
#     def __init__(self, name: str, price: float, quantity: int) -> None:
#         """
#         Создает экземпляр класса Keyboard.
#
#         :param name: Название клавиатуры.
#         :param price: Цена за единицу клавиатуры.
#         :param quantity: Количество клавиатур в магазине.
#         """
#         super().__init__(name, price, quantity)
#         self.language = 'EN'
#
#     def __str__(self) -> str:
#         """
#         Возвращает название клавиатуры.
#
#         :return: Название клавиатуры.
#         """
#         return self.name

    # def change_lang(self) -> 'Keyboard':
    #     """
    #     Меняет раскладку клавиатуры на следующую.
    #
    #     :return: Текущий экземпляр класса Keyboard.
    #     """
    #     if self.language == 'EN':
    #         self.language = 'RU'
    #     else:
    #         self.language = 'EN'
    #     return self










