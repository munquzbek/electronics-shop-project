from src.item import Item


class Language:

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    def change_lang(self):
        """
        Change language
        """
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'

    @property
    def language(self):
        return self.__language


class Keyboard(Language, Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

