""" Advent of code 2024 - Puzzle 01

    https://adventofcode.com/2024/day/1

    John Tocher     
    Solution to puzzle 01 part 1
"""

INPUT_FILE_NAME = "puzzle_01_input_01.txt"


def read_input_data():
    # Read the puzzle input from a text file
    count_lines = 0
    lines_of_numbers = list()
    list_a = list()
    list_b = list()
    for single_line in open(INPUT_FILE_NAME, "r").readlines():
        count_lines += 1
        clean_line = single_line.strip()
        list_of_numbers = [int(each_num) for each_num in clean_line.split("   ")]
        list_a.append(list_of_numbers[0])
        list_b.append(list_of_numbers[1])

    list_a.sort()
    list_b.sort()

    return list_a, list_b


def solve_puzzle():
    # Main solving logic
    puzzle_input = read_input_data()
    assert len(puzzle_input[0]) == len(puzzle_input[1]), "Bad input!"
    diff_total = 0
    for line_index in range(0, len(puzzle_input[0])):
        this_diff = abs(puzzle_input[0][line_index] - puzzle_input[1][line_index])
        diff_total += this_diff

    print(f"Result is: {diff_total}")


if __name__ == "__main__":
    solve_puzzle()
