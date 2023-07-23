

"""
    Класс для представления товара в магазине.
    """
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
        self.all.append(self) #добавил , результата нет

    def calculate_total_price(self) -> float:
        return self.price * self.quantity


    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate
        return #self.price


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
    def instantiate_from_csv(cls, reader):
        name, price, quantity = reader.split(',')
        return cls(name, price, quantity)




