

from src.phone import Phone
from src.item import Item
def test_phone():
    phone = Phone("iPhone", 120, 50, 2)
    assert str(phone) == 'iPhone'
    assert repr(phone) == "Phone('iPhone', 120, 50, 2)"
    assert phone.number_of_sim == 2

    item = Item("Смартик", 100, 2)
    assert phone + item == 52
    assert phone + phone == 100

    assert phone.number_of_sim == 2