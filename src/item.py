import csv


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        Item.all.append(self)
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        raise Exception

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> float:
        self.price = self.price * Item.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
        else:
            print("Exception: Длина наименования товара превышает 10 символов")
            self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls, file_path='../src/items.csv'):
        try:
            with open(file_path, encoding="cp1251") as file:
                csvfile = csv.DictReader(file)
                for row in csvfile:
                    cls(row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл items.csv')
        except KeyError as ke:
            raise InstantiateCSVError('Файл items.csv поврежден', ke)

    @staticmethod
    def string_to_number(value):
        return int(float(value))


class InstantiateCSVError(Exception):
    def __init__(self, *args):
        if len(args) < 3:
            self.message = "Файл items.csv поврежден"
