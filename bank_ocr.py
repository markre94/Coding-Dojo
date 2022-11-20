from numbers_data import DIGITS_DICT


def split_input(input_string):
    rows = 4
    cols = len(input_string) // rows
    digits = cols // 3
    single_row_char_no = 3

    numbers = [[] for _ in range(digits)]
    str_idx = 0
    for row_no in range(rows):
        for digit_no in range(digits):
            cut_part = input_string[str_idx:single_row_char_no]
            numbers[digit_no].append(tuple(ch for ch in cut_part))
            str_idx, single_row_char_no = single_row_char_no, single_row_char_no + 3

    return [tuple(y) for y in numbers]


def map_bank_digits(split_digits):
    return "".join(DIGITS_DICT.get(key, '?') for key in split_digits)


def calculate_checksum(account_number: str):
    value = 0
    for i, n in enumerate(reversed(account_number), start=1):
        value += (i * int(n))

    return value % 11


def is_bank_account_number_valid(account_number: str):
    if len(account_number) != 9:
        return False
    return is_bank_account_checksum_correct(account_number)


def is_bank_account_checksum_correct(account_number: str):
    return calculate_checksum(account_number) == 0


def validate_read_number(number: str):
    if '?' in number:
        return number + " ILL"
    if not is_bank_account_number_valid(number):
        return number + " ERR"
    return number


def read_input_data(ocr_input: str) -> str:
    split_data = split_input(ocr_input)
    read_numbers = map_bank_digits(split_data)
    return validate_read_number(read_numbers)
