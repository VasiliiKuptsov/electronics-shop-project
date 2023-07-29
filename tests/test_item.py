"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item():
    item_ = Item('pen', 300, 30)

    assert item_.name == 'pen'
    assert item_.price == 300
    assert item_.quantity == 30
    assert repr(item_) == "Item('pen', 300, 30)"
    assert str(item_) == 'pen'