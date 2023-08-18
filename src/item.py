
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
        Item.all.append(self)


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
    def instantiate_from_csv(cls, file = 'items.csv'):
        ROOT = Path(__file__).parent
        DATA_PATH = Path.joinpath(ROOT, file)
        path = DATA_PATH
        Item.all.clear()

        #try:
        with open(path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if reader.fieldnames[0] == 'name' and reader.fieldnames[1] =='price' and reader.fieldnames[2] == 'quantity':


                for reader_ in reader:
                    if reader_['quantity'] == None or reader_['name'] == None or reader_['price'] == None:
                        raise InstantiateCSVError('Файл item.csv поврежден')
                    else:
                        cls(name=reader_['name'], price=reader_['price'], quantity=reader_['quantity'])
            else:
                raise InstantiateCSVError('Файл item.csv поврежден')

        #except FileNotFoundError:
         #   print("FileNotFoundError: отсутствует файл items.csv")
        #except InstantiateCSVError as e:
         #   print(e)
        #return

    @staticmethod
    def string_to_number(number: str) -> int:
        return int(float(number))


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.number_of_sim})"


    def __str__(self):
        return (self.__name)


class InstantiateCSVError(Exception):

    def __init__(self, message):
        super().__init__(message)
        self.message = message


    def __str__(self):
        return self.message





