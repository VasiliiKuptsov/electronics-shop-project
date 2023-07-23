from src.item import Item


def test_item():
    item_ = Item('pen', 300, 30)
    assert item_.price == 300
    assert item_.quantity == 30
    assert item_.calculate_total_price() == 9000
    assert item_.apply_discount() == 300
    Item.pay_rate = 0.8
    assert item_.apply_discount() == 240
