""" Advent of code 2023 - Puzzle 02

    https://adventofcode.com/2024/day/2

    John Tocher     
    Solution to puzzle 02 part 2
"""

INPUT_FILE_NAME = "puzzle_02_input_01.txt"


def read_input_data():
    # Read the puzzle input from a text file
    count_lines = 0
    lines_of_numbers = list()

    for single_line in open(INPUT_FILE_NAME, "r").readlines():
        count_lines += 1
        clean_line = single_line.strip()
        list_of_numbers = [int(each_num) for each_num in clean_line.split(" ")]
        lines_of_numbers.append(list_of_numbers)

    return lines_of_numbers


def get_differences(input_list):
    # Returns a list of differences between each integer in the supplied list

    differences = list()

    for int_index in range(1, len(input_list)):
        this_diff = input_list[int_index] - input_list[int_index - 1]
        differences.append(this_diff)

    return differences


def report_is_safe(single_report):
    # Checks the puzzle rules and reports if a report is safe

    num_positive = 0
    num_negative = 0
    num_out_of_range = 0
    list_of_diffs = get_differences(single_report)
    report_is_safe = True

    # First check the numbers are in range
    for each_diff in list_of_diffs:
        if each_diff in range(1, 4):
            num_positive += 1
        elif each_diff in range(-3, 0):
            num_negative += 1
        else:
            num_out_of_range += 1
            return False

    if num_positive and num_negative:
        report_is_safe = False

    return report_is_safe


def solve_puzzle():
    # Main solving logic
    puzzle_input = read_input_data()
    safe_report_count = 0
    for each_line in puzzle_input:
        if report_is_safe(each_line):
            # Dont bother with the damener if it's already OK!
            safe_report_count += 1
        else:
            # Here we'll make a copy of the reports, and look for a solution
            # which passes when removing a single entry, a single pass is enough
            # hence the 'break'
            for score_index in range(0, len(each_line)):
                line_to_check = each_line.copy()
                line_to_check.pop(score_index)
                if report_is_safe(line_to_check):
                    safe_report_count += 1
                    break

    print(f"Result is: {safe_report_count}")


if __name__ == "__main__":
    solve_puzzle()
