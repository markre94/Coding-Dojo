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
    return "".join(DIGITS_DICT[key] for key in split_digits)


def main():
    for elem in DIGITS_DICT.keys():
        print(join_number_s(elem))


if __name__ == '__main__':
    main()
