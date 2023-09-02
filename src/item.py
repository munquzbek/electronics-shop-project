import csv
import pandas as pd


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        self.__name = name
        self.price = price
        self.quantity = quantity

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
    def instantiate_from_csv(cls):
        with open('../src/items.csv', encoding="cp1251") as file:
            csvfile = csv.DictReader(file)
            for row in csvfile:
                Item.all.append(Item(row['name'], row['price'], int(row["quantity"])))
            return Item.all

    @staticmethod
    def string_to_number(value):
        floated = float(value)
        rounded = int(round(floated, 0))
        print(rounded)
        return rounded
