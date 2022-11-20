from main import split_input, map_bank_digits
from numbers_data import DIGITS_DICT
import pytest


@pytest.fixture()
def data_test():
    return (f" _     _  _     _  _  _  _  _ "
            f"| |  | _| _||_||_ |_   ||_||_|"
            f"|_|  ||_  _|  | _||_|  ||_| _|"
            f"                              ")


@pytest.fixture()
def data_test_9_1():
    return (f" _     _  _     _  _  _  _  _ "
            f"| |  | _| _||_||_ |_   ||_||_|"
            f"|_|  ||_  _|  | _||_|  ||_| _|"
            f"                              ")


@pytest.fixture()
def data_test_zeros():
    return (f" _  _  _  _  _  _  _  _  _ "
            f"| || || || || || || || || |"
            f"|_||_||_||_||_||_||_||_||_|"
            f"                           ")


@pytest.fixture()
def data_test_zero():
    return (f" _ "
            f"| |"
            f"|_|"
            f"   ")


def test_multiple_digits(data_test):
    multi = split_input(data_test)
    assert DIGITS_DICT[multi[0]] == "0"


def test_ocr_nine_zeros(data_test_zeros):
    multi = split_input(data_test_zeros)
    assert map_bank_digits(multi) == "0" * 9


def test_map_bank_number(data_test):
    s_input = split_input(data_test)
    assert map_bank_digits(s_input) == "0123456789"



