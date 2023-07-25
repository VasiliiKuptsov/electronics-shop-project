import csv
from pathlib import Path
ROOT = Path(__file__).parent
DATA_PATH = Path.joinpath(ROOT, 'items.csv')
path = DATA_PATH


class Item:

    pay_rate = 1.0
    all = []
    """
         Создание экземпляра класса item.

         :param name: Название товара.
         :param price: Цена за единицу товара.
         :param quantity: Количество товара в магазине.
         """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_):
        if len(name_) > 10:
            self.__name = name_[0:10]
        else:
            self.__name = name_

    @classmethod
    def instantiate_from_csv(cls):
        with open(path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for reader_ in reader:
                all_ = [reader_['name'], reader_['price'], reader_['quantity']]
                cls.all.append(all_)
        return

    @staticmethod
    def string_to_number(number: str) -> int:
        return int(float(number))
