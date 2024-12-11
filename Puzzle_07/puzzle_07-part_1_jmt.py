""" Advent of code 2024 - Puzzle 07

    https://adventofcode.com/2024/day/7

    John Tocher     
    Solution to puzzle 07 part 1
"""

# INPUT_FILE_NAME = "puzzle_07_input_02_sample.txt"
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


def get_operators(operator_number, operator_count):
    """Returns a list of operators, calculated with a binary
    representation of the input number with the 1 or 0 being
    mapped to addition or multiplication"""

    operator_list = list()
    bin_text = f"{operator_number:b}".zfill(operator_count)
    # print(f"Num: {operator_number:02} from {operator_count} operators. Map: {bin_text}")
    for each_char in bin_text:
        if each_char == "0":
            operator_list.append("+")
        else:
            operator_list.append("*")

    return operator_list


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
        else:
            assert False, f"Unknown operator: {this_operator}"
        operator_index += 1

    calc_string = f"{calc_string}={current_result}"

    return current_result, calc_string


def solve_puzzle():
    # Main solving logic
    test_data = read_input_data()
    print(f"Read {len(test_data)} lines from input")
    count_tests = 0
    count_valid = 0
    total_cal = 0

    for each_test in test_data:
        # For 2 numbers, 1 operator 0b to 1b (0 to 1)
        # For 3 numbers, 2 operators from 00b to 11b (0 to 3)
        # For 4 numbers, 3 operators from 000b to 111b (0 to 7)
        # For 5 numbers, 4 operators from 0000b to 1111b (0 to 15)
        numbers = each_test["numbers"]
        count_numbers = len(numbers)
        count_operators = count_numbers - 1
        operator_combos = 2 ** (count_operators)
        # print(f"Have {count_operators} operators, Testing from 0 to {operator_combos}")
        for combo_count in range(0, operator_combos):
            operators = get_operators(combo_count, count_operators)
            test_result, calc_string = calculate_result(numbers, operators)

            if test_result == each_test["value"]:
                count_valid += 1
                total_cal += test_result
                break  # Don't need to check any more from this test
            else:
                # print(f"Fail: {calc_string}")
                pass

        count_tests += 1

    print(
        f"Found {count_valid} valid tests from {count_tests} for a total of {total_cal}"
    )


if __name__ == "__main__":
    solve_puzzle()
