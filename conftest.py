import pytest

import numbers_data as nb


@pytest.fixture()
def bank_account_number():
    numbers = [nb.FOUR, nb.FIVE, nb.SEVEN, nb.FIVE, nb.ZERO, nb.EIGHT, nb.ZERO, nb.ZERO, nb.ZERO]
    bank = nb.BankAccountInput(numbers)
    return bank.create_valid_bank_account_input()


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
