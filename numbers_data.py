import random

ONE = ((" ", " ", " "),
       (" ", " ", "|"),
       (" ", " ", "|"),
       (" ", " ", " "))

ZERO = ((" ", "_", " "),
        ("|", " ", "|"),
        ("|", "_", "|"),
        (" ", " ", " "))

TWO = ((" ", "_", " "),
       (" ", "_", "|"),
       ("|", "_", " "),
       (" ", " ", " "))

THREE = ((" ", "_", " "),
         (" ", "_", "|"),
         (" ", "_", "|"),
         (" ", " ", " "))

FOUR = ((" ", " ", " "),
        ("|", "_", "|"),
        (" ", " ", "|"),
        (" ", " ", " "))

FIVE = ((" ", "_", " "),
        ("|", "_", " "),
        (" ", "_", "|"),
        (" ", " ", " "))

SIX = ((" ", "_", " "),
       ("|", "_", " "),
       ("|", "_", "|"),
       (" ", " ", " "))

SEVEN = ((" ", "_", " "),
         (" ", " ", "|"),
         (" ", " ", "|"),
         (" ", " ", " "))

EIGHT = ((" ", "_", " "),
         ("|", "_", "|"),
         ("|", "_", "|"),
         (" ", " ", " "))

NINE = ((" ", "_", " "),
        ("|", "_", "|"),
        (" ", "_", "|"),
        (" ", " ", " "))


AVAILABLE_NUMS = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]

DIGITS_DICT = {ZERO: "0", ONE: "1", TWO: "2", THREE: "3", FOUR: "4", FIVE: "5", SIX: "6", SEVEN: "7", EIGHT: "8",
               NINE: "9"}


def join_number_s(number) -> str:
    result = []
    for row in number:
        result.append("".join(row))

    return "\n".join(result)


def get_random_number_list(k: int):
    return random.choices(AVAILABLE_NUMS, k=k)


class BankAccountInput:
    def __init__(self, numbers: list):
        self.numbers = numbers

    def __str__(self):
        return "\n".join(self._get_bank_account_result_rows())

    def _get_bank_account_result_rows(self):
        result = []
        rows = len(self.numbers[0])
        for i in range(rows):
            row = ""
            for num in self.numbers:
                row += "".join(num[i])
            result.append(row)
        return result

    def create_valid_bank_account_input(self) -> str:
        result = self._get_bank_account_result_rows()
        return "".join(result)
