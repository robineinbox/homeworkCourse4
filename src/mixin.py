﻿# Класс-миксин для хранения и изменения раскладки клавиатуры
class LanguageMixin:
    def __init__(self):
        self.language = 'EN'

    def change_lang(self):
        """
        Меняет раскладку клавиатуры на следующую.

        :return: Текущий экземпляр класса Keyboard.
        """
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'
        return self

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        """
        Устанавливает язык раскладки.

        :param value: Значение языка раскладки.
        :return: None
        """
        if value not in ('EN', 'RU'):
            raise ValueError(f"Неподдерживаемый язык: {value}")
        self._language = value











# class LanguageMixin:
#     languages = {'EN': 'English', 'RU': 'Russian'}
#     default_lang = 'EN'
#
#     def __init__(self, language=default_lang):
#         self.language = language
#
#     def change_lang(self):
#         curr_lang = list(self.languages.keys()).index(self.language)
#         next_lang = (curr_lang + 1) % len(self.languages)
#         self.language = list(self.languages.keys())[next_lang]
#         return self



# class LanguageMixin:
#     def __init__(self, language='EN'):
#         self.language = language
#
#     def change_lang(self):
#         if self.language == "EN":
#             self.language = "RU"
#         else:
#             self.language = "EN"
#         return self
#
#     def set_language(self, language):
#         if language not in ('EN', 'RU'):
#             raise ValueError(f"Неподдерживаемый язык: {language}")
#         self.language = language