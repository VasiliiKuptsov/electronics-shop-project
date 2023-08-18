
from src.item import Item
import pytest

def test_instantiate_from_csv():
    Item.instantiate_from_csv(file='../src/items.csv')
    assert  len(Item.all) == 5
    assert isinstance(Item.all[0], Item)

def test_instantiate_from_csv_error():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('does_not_exists.csv')


def test_instantiate_from_csv_error():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('corrupted.csv')














