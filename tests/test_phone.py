import pytest

from src.phone import Phone


@pytest.fixture()
def phone():
    return Phone("iPhone", 120000, 10, 2)


def test__repr__(phone):
    assert repr(phone) == "Phone('iPhone', 120000, 10, 2)"


def test_number_of_sim(phone):
    assert phone.number_of_sim == 2




