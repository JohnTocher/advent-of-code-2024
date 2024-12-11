""" Advent of code 2024 - Puzzle 07

    https://adventofcode.com/2024/day/7

    John Tocher     
    Solution to puzzle 07 part 2
"""

from itertools import product

# INPUT_FILE_NAME = "puzzle_07_input_01_sample.txt"
INPUT_FILE_NAME = "puzzle_07_input_01.txt"


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


def calculate_result(number_list, operator_list):
    """Calculates the left to right answer as desfined by the puzzle"""

    operator_index = 0
    current_result = number_list[0]
    calc_string = f"Calc: {current_result}"
    for each_number in number_list[1:]:
        this_operator = operator_list[operator_index]
        if this_operator == "+":
            current_result += each_number
            calc_string = f"{calc_string}+{each_number}"
        elif this_operator == "*":
            current_result *= each_number
            calc_string = f"{calc_string}x{each_number}"
        elif this_operator == "||":
            current_result = int(f"{current_result}{each_number}")
            calc_string = f"{calc_string}||{each_number}"
        else:
            assert False, f"Unknown operator: {this_operator}"
        operator_index += 1

    calc_string = f"{calc_string}={current_result}"

    return current_result, calc_string


def calculate_result_with_max(number_list, operator_list, max_value):
    """Calculates the left to right answer as desfined by the puzzle"""

    oversize = False
    operator_index = 0
    current_result = number_list[0]
    for each_number in number_list[1:]:
        this_operator = operator_list[operator_index]
        if this_operator == "+":
            current_result += each_number
        elif this_operator == "*":
            current_result *= each_number
        elif this_operator == "||":
            current_result = int(f"{current_result}{each_number}")
        else:
            assert False, f"Unknown operator: {this_operator}"
        operator_index += 1
        if current_result > max_value:
            oversize = True
            break

    # calc_string = f"{calc_string}={current_result}"

    return oversize, current_result


def solve_puzzle():
    # Main solving logic
    test_data = read_input_data()
    print(f"Read {len(test_data)} lines from input")
    count_tests = 0
    count_valid = 0
    total_cal = 0

    operators_for_length = dict()
    for op_length in range(1, 15):
        operators_for_length[op_length] = tuple(
            product(("+", "*", "||"), repeat=op_length)
        )

    for each_test in test_data:
        numbers = each_test["numbers"]
        count_numbers = len(numbers)
        count_operators = count_numbers - 1
        test_value = each_test["value"]

        all_operators = operators_for_length[count_operators]
        for operators_to_try in all_operators:
            # test_result, calc_string = calculate_result(numbers, operators_to_try)
            not_found, test_result = calculate_result_with_max(
                numbers, operators_to_try, test_value
            )

            if test_result == test_value:
                count_valid += 1
                total_cal += test_result
                # print(f"Pass: {calc_string}")
                break  # Don't need to check any more from this test

        count_tests += 1

    print(
        f"Found {count_valid} valid tests from {count_tests} for a total of {total_cal}"
    )


if __name__ == "__main__":
    solve_puzzle()
