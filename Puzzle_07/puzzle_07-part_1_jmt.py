""" Advent of code 2024 - Puzzle 07

    https://adventofcode.com/2024/day/7

    John Tocher     
    Solution to puzzle 07 part 1
"""

INPUT_FILE_NAME = "puzzle_07_input_01_sample.txt"
# INPUT_FILE_NAME = "puzzle_07_input_01.txt"


def read_input_data():
    # Read the puzzfle input from a text file
    test_details = list()
    pos_y = 0
    for single_line in open(INPUT_FILE_NAME, "r").readlines():
        clean_line = single_line.strip()
        test_val, test_parms = clean_line.split(":")
        this_test = dict()
        this_test["value"] = int(test_val)
        this_test["numbers"] = [
            int(each_part) for each_part in test_parms.strip().split(" ")
        ]
        test_details.append(this_test)

    return test_details


def get_operators(operator_number, operator_bits):
    """Returns a list of operators, calculated with a binary
    representation of the input number with the 1 or 0 being
    mapped to addition or multiplication"""

    operator_list = list()
    bin_text = f"{operator_number:x}".zfill(operator_bits)
    for each_char in bin_text:
        if each_char == "0":
            operator_list.append("+")
        else:
            operator_list.append("*")

    return operator_list


def solve_puzzle():
    # Main solving logic
    test_data = read_input_data()
    count_tests = 0
    count_valid = 0
    for each_test in test_data:
        count_numbers = len(each_test["numbers"])
        operator_count = 2 ** (count_numbers - 1)
        for ooperator_group in range(0, operator_count):
            operators = get_operators(ooperator_group, count_numbers)
            print(f"{count_tests} Operators: {operators}")
        count_tests += 1

    print(f"Found {count_valid} solutions which cause a loop")


if __name__ == "__main__":
    solve_puzzle()
