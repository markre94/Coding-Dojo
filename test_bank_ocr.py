from bank_ocr import split_input, map_bank_digits, is_bank_account_number_valid, calculate_checksum, validate_read_number, \
    read_input_data
from numbers_data import DIGITS_DICT, ONE, TWO
import pytest


def test_multiple_digits(data_test):
    multi = split_input(data_test)
    assert DIGITS_DICT[multi[0]] == "0"


def test_ocr_nine_zeros(data_test_zeros):
    multi = split_input(data_test_zeros)
    assert map_bank_digits(multi) == "0" * 9


def test_map_bank_number(data_test):
    s_input = split_input(data_test)
    assert map_bank_digits(s_input) == "0123456789"


@pytest.mark.parametrize("test_input, expected", [('457508000', 0), ('6' * 9, 6)])
def test_calculate_checksum(test_input, expected):
    assert calculate_checksum(test_input) == expected


@pytest.mark.parametrize("no_input, result", [('457508000', True), ('664371495', False), ('', False),
                                              ('9' * 10, False)])
def test_bank_account_valid(no_input, result):
    assert is_bank_account_number_valid(no_input) is result


@pytest.mark.parametrize("no_input, result", [('457508000', '457508000'), ('664371495', '664371495 ERR'),
                                              ('664?7?495', '664?7?495 ILL')])
def test_validate_read_number(no_input, result):
    assert validate_read_number(no_input) == result


def test_map_bank_digits():
    INVALID = ((" ", "_", " "),
               (" ", "_", "|"),
               (" ", " ", "|"),
               (" ", " ", " "))

    nums = [ONE, TWO, INVALID]
    assert map_bank_digits(nums) == "12?"


def test_read_input_data(bank_account_number):
    result = read_input_data(bank_account_number)
    assert result == '457508000'
