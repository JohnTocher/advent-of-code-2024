""" Advent of code 2024 - Puzzle 08

    https://adventofcode.com/2024/day/8

    John Tocher     
    Solution to puzzle 08 part 1
"""

from itertools import permutations
from math import lcm

INPUT_FILE_NAME = "puzzle_08_input_02_sample.txt"
# INPUT_FILE_NAME = "puzzle_08_input_01.txt"


def read_input_data():
    # Read the puzzfle input from a text file

    antenna_data = dict()
    pos_y = 0
    for single_line in open(INPUT_FILE_NAME, "r").readlines():
        clean_line = single_line.strip()
        pos_x = 0
        for each_char in clean_line:
            if each_char != ".":
                this_pos = (pos_x, pos_y)
                pos_list = antenna_data.get(each_char, list())
                pos_list.append(this_pos)
                antenna_data[each_char] = pos_list
            pos_x += 1
        pos_y += 1

    return antenna_data, pos_x, pos_y


def sort_two_coords(list_of_coords):
    """Takes a list of coordinates and sorts them consistently"""

    index_0 = 0
    index_1 = 1

    if list_of_coords[0][0] < list_of_coords[1][0]:  # X value increasing
        index_0 = 0
        index_1 = 1
    elif list_of_coords[0][0] > list_of_coords[1][0]:  # X value decreasing
        index_0 = 1
        index_1 = 0
    elif list_of_coords[0][1] < list_of_coords[1][1]:  # Y value increasing
        index_0 = 0
        index_1 = 1
    elif list_of_coords[0][1] < list_of_coords[1][1]:  # Y value decreasing
        index_0 = 1
        index_1 = 0
    else:
        assert False, "Overlapping points"

    return (tuple(list_of_coords[index_0]), tuple(list_of_coords[index_1]))


def all_points_on_line(pair_of_points, size_x, size_y):
    """Calculates all of the points along the given lines"""
    dx = pair_of_points[0][0] - pair_of_points[1][0]
    dy = pair_of_points[0][1] - pair_of_points[1][1]

    divisor = lcm(abs(dx), abs(dy))
    print(f"lcm: {divisor}")

    points_on_line = set()
    this_x = pair_of_points[0][0]
    this_y = pair_of_points[0][1]
    while this_x in range(0, size_x) and this_y in range(0, size_y):
        points_on_line.add((this_x, this_y))
        this_x += dx
        this_y += dy

    this_x = pair_of_points[0][0]
    this_y = pair_of_points[0][1]
    while this_x in range(0, size_x) and this_y in range(0, size_y):
        points_on_line.add((this_x, this_y))
        this_x -= dx
        this_y -= dy

    return points_on_line


def draw_grid(grid_elements, size_x, size_y):
    for ty in range(0, size_y):
        this_line = ""
        for tx in range(0, size_x):
            if (tx, ty) in grid_elements:
                this_line = f"{this_line}X"
            else:
                this_line = f"{this_line}."
        print(this_line)


def solve_puzzle():
    # Main solving logic
    ant_data, size_x, size_y = read_input_data()
    loc_count = 0

    # print(f"Sample: {ant_data['A']}")

    for label, locations in ant_data.items():
        all_pairs = permutations(locations, 2)
        unique_pairs = set()
        for each_pair in all_pairs:
            sorted_pair = sort_two_coords(each_pair)
            unique_pairs.add(sorted_pair)

        print(f"{label} combo {unique_pairs} ")
        for each_pair in unique_pairs:
            all_points = all_points_on_line(each_pair, size_x, size_y)
            print(f"All points {all_points}")

        draw_grid(all_points, size_x, size_y)

    print(f"Locations {loc_count}")


if __name__ == "__main__":
    solve_puzzle()
