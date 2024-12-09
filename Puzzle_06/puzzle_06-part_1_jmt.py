""" Advent of code 2024 - Puzzle 06

    https://adventofcode.com/2024/day/6

    John Tocher     
    Solution to puzzle 06 part 1
"""

# INPUT_FILE_NAME = "puzzle_06_input_01_sample.txt"
INPUT_FILE_NAME = "puzzle_06_input_01.txt"

start_x = False
start_y = False


def read_input_data():
    # Read the puzzle input from a text file
    grid_values = dict()
    pos_y = 0
    for single_line in open(INPUT_FILE_NAME, "r").readlines():
        clean_line = single_line.strip()
        pos_x = 0
        for each_char in clean_line:
            if each_char == "^":
                start_x = pos_x
                start_y = pos_y
                each_char = "."  # Easier to handle re-passing start point
            grid_values[(pos_x, pos_y)] = each_char
            pos_x += 1
        pos_y += 1

    return grid_values, start_x, start_y, pos_x, pos_y


def get_direction_data():
    """returns a dictionary of direction data"""

    d_data = dict()

    d_data["up"] = {"walk": (0, -1), "turn": (1, 0), "new_dir": "right"}
    d_data["right"] = {"walk": (1, 0), "turn": (0, 1), "new_dir": "down"}
    d_data["down"] = {"walk": (0, 1), "turn": (-1, 0), "new_dir": "left"}
    d_data["left"] = {"walk": (-1, 0), "turn": (0, -1), "new_dir": "up"}

    return d_data


def solve_puzzle():
    # Main solving logic
    map_data, current_x, current_y, size_x, size_y = read_input_data()
    dir_data = get_direction_data()

    print(f"Starting at {start_x},{start_y}")
    steps_taken = 0
    still_walking = True
    current_direction = "up"
    visited_locations = set()
    visited_locations.add((current_x, current_y))

    while still_walking:
        next_x = current_x + dir_data[current_direction]["walk"][0]
        next_y = current_y + dir_data[current_direction]["walk"][1]
        if next_x not in range(0, size_x):
            still_walking = False
            # break
        if next_y not in range(0, size_y):
            still_walking = False
            # break
        if still_walking:
            # OK ot move!
            next_pos = map_data[(next_x, next_y)]
            if next_pos != ".":  # is an object to avoid
                next_x = current_x + dir_data[current_direction]["turn"][0]
                next_y = current_y + dir_data[current_direction]["turn"][1]
                current_direction = dir_data[current_direction]["new_dir"]
                # print(f"Turning to {next_x},{next_y}")
            else:
                # print(f"Walking to {next_x},{next_y}")
                pass

            current_x = next_x
            current_y = next_y
            visited_locations.add((current_x, current_y))
            steps_taken += 1

    print(
        f"Finished at {current_x},{current_y} after {steps_taken} steps over {len(visited_locations)} locations"
    )

    # print(f"Result: {steps_taken}")


if __name__ == "__main__":
    solve_puzzle()
