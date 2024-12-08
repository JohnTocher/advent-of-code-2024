""" Advent of code 2024 - Puzzle 04

    https://adventofcode.com/2024/day/4

    John Tocher     
    Solution to puzzle 04 part 2
"""

# INPUT_FILE_NAME = "puzzle_04_input_01_sample.txt"
INPUT_FILE_NAME = "puzzle_04_input_01.txt"


def read_input_data():
    # Read the puzzle input from a text file
    grid_values = dict()
    pos_y = 0
    for single_line in open(INPUT_FILE_NAME, "r").readlines():
        clean_line = single_line.strip()
        pos_x = 0
        for each_char in clean_line:
            grid_values[(pos_x, pos_y)] = each_char
            pos_x += 1
        pos_y += 1

    return grid_values, pos_x, pos_y


def word_geometry_for_xmas():
    # Returns a list of geometries as x,y offsets for allowed layouts

    all_geos = list()
    all_geos.append([[1, 0], [2, 0], [3, 0]])  # Right
    all_geos.append([[-1, 0], [-2, 0], [-3, 0]])  # Right
    all_geos.append([[0, 1], [0, 2], [0, 3]])  # Up
    all_geos.append([[0, -1], [0, -2], [0, -3]])  # Down

    all_geos.append([[1, 1], [2, 2], [3, 3]])  # Up right
    all_geos.append([[-1, 1], [-2, 2], [-3, 3]])  # Up left
    all_geos.append([[1, -1], [2, -2], [3, -3]])  # Down right
    all_geos.append([[-1, -1], [-2, -2], [-3, -3]])  # Up right

    return all_geos


def word_geometry_for_x_mas():
    # Returns a list of geometries as x,y offsets for allowed layouts

    all_geos = list()
    all_geos.append([[-1, -1], [1, 1], [-1, 1], [1, -1]])  # left to right both
    all_geos.append([[-1, -1], [1, 1], [1, -1], [-1, 1]])  # one of each  A
    all_geos.append([[1, -1], [-1, 1], [1, 1], [-1, -1]])  # right to left both
    all_geos.append([[1, 1], [-1, -1], [-1, 1], [1, -1]])  # one of each B

    return all_geos


def words_from_point(grid_data, start_point, geo_list, max_x, max_y):
    """Produce a list of all words of allowed geometries starting at the supplied point"""

    word_list = list()
    for each_geo in geo_list:
        this_word = "X"
        for letter_pos in each_geo:
            new_x = letter_pos[0] + start_point[0]
            new_y = letter_pos[1] + start_point[1]
            if new_x in range(0, max_x) and new_y in range(0, max_y):
                this_letter = grid_data[(new_x, new_y)]
            else:
                this_letter = "-"
            this_word = f"{this_word}{this_letter}"
        if this_word == "XMAS":
            word_list.append(this_word)

    return word_list


def x_mas_from_point(grid_data, start_point, geo_list, max_x, max_y):
    """Produce a list of all words of allowed geometries starting at the supplied point"""

    word_list = list()
    for each_geo in geo_list:
        this_word = ""
        for letter_pos in each_geo:
            new_x = letter_pos[0] + start_point[0]
            new_y = letter_pos[1] + start_point[1]
            if new_x in range(0, max_x) and new_y in range(0, max_y):
                this_letter = grid_data[(new_x, new_y)]
            else:
                this_letter = "-"
            this_word = f"{this_word}{this_letter}"
        if this_word == "MSMS":  # We're not putting the A in the middle for simplicity
            word_list.append(this_word)

    return word_list


def solve_puzzle():
    # Main solving logic
    puzzle_grid, size_x, size_y = read_input_data()
    print(f"Data has {size_x} x {size_y} elements")
    word_count = 0

    geo_lists = word_geometry_for_x_mas()

    for pos_y in range(0, size_y):
        for pos_x in range(0, size_x):
            if puzzle_grid[(pos_x, pos_y)] == "A":
                # Might be an x-mas centred here
                words_from_here = x_mas_from_point(
                    puzzle_grid, (pos_x, pos_y), geo_lists, size_x, size_y
                )
                # if (pos_x == 1) and (pos_y == 7):
                #    print(f"A at {pos_x},{pos_y}")
                # print(f"{pos_x},{pos_y}: {words_from_here}")
                word_count += len(words_from_here)

    print(f"Result: {word_count}")


if __name__ == "__main__":
    solve_puzzle()
