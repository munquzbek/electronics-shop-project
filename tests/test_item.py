import pytest

from src.item import Item


@pytest.fixture
def item():
    return Item("Смартфон", 1000, 2)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 2000


def test_apply_discount(item):
    Item.pay_rate = 0.8
    assert item.apply_discount() == 800.0


def test_string_to_number(item):
    assert item.string_to_number('7.5') == 8
    assert item.string_to_number('8.5') == 8


