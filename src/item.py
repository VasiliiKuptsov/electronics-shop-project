
import csv
from pathlib import Path
ROOT = Path(__file__).parent
DATA_PATH = Path.joinpath(ROOT, 'items.csv')
path = DATA_PATH


class Item:

    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self) -> float:
        return self.price * self.quantity


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
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
        #raise FileNotFoundError('отсутствует файл items.csv')
        try:

            with open(path, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
        except FileNotFoundError:
            print("FileNotFoundError: отсутствует файл items.csv")

            for reader_ in reader:
                print(reader_)
                if reader_['quantity'] == None:
                    raise InstantiateCSVError
                all_ = [reader_['name'], reader_['price'], reader_['quantity']]

                cls.all.append(all_)
        return

    @staticmethod
    def string_to_number(number: str) -> int:
        return int(float(number))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):

        return (self.__name)


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'InstantiateCSVError: Файл item.csv поврежден'

    def __str__(self):
        return self.message
    #@staticmethod

    #def instantiate_from_csv():

        """try:
            with open(path, "rb") as file:

                file_csv = file.read()
                print(file_csv)
        except FileNotFoundError:
            print("FileNotFoundError: отсутствует файл items.csv")
            return None
        else:
            print('Продолжение работы программы...')"""




