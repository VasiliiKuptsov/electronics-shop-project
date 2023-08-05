
from src.item import Item
from src.phone import Phone

def test_item():
    phone = Phone("iPhone", 120, 50, 2)
    assert str(phone) == 'iPhone'
    assert repr(phone) == "Phone('iPhone', 120, 50, 2)"
    item = Item("Смартик", 100, 2)
    assert str(item) == 'Смартик'
    assert item.price == 100
    assert item.quantity == 2
    assert phone + item == 52






