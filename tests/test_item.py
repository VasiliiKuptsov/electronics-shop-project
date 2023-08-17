
from src.item import Item
from src.phone import Phone

def test_instantiate_from_csv():
    Item.instantiate_from_csv(file='../src/items.csv')
    assert  len(Item.all) == 5
    assert isinstance(Item.all[0], Item)









