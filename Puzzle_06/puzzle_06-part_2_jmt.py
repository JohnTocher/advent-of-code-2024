""" Advent of code 2024 - Puzzle 06

    https://adventofcode.com/2024/day/6

    John Tocher     
    Solution to puzzle 06 part 2
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


def test_map_for_loop(
    map_data, current_x, current_y, size_x, size_y, dir_data, return_locations=False
):
    """Runs the original algoritm returning whether or not the guard will loop"""

    # print(f"Starting at {start_x},{start_y}")
    steps_taken = 0
    still_walking = True
    will_loop = False
    current_direction = "up"
    visited_locations = set()
    visited_locations.add((current_x, current_y))
    visited_details = set()

    while still_walking:
        next_x = current_x + dir_data[current_direction]["walk"][0]
        next_y = current_y + dir_data[current_direction]["walk"][1]
        if next_x not in range(0, size_x):
            still_walking = False
        if next_y not in range(0, size_y):
            still_walking = False
        if still_walking:
            # OK to move!
            next_pos = map_data[(next_x, next_y)]
            while next_pos != ".":  # is an object to avoid
                next_x = current_x + dir_data[current_direction]["turn"][0]
                next_y = current_y + dir_data[current_direction]["turn"][1]
                current_direction = dir_data[current_direction]["new_dir"]
                next_pos = map_data[(next_x, next_y)]
                # print(f"Turning to {next_x},{next_y}")
            else:
                # print(f"Walking to {next_x},{next_y}")
                pass

            current_x = next_x
            current_y = next_y
            visited_locations.add((current_x, current_y))
            location_detail = (current_x, current_y, current_direction)
            if location_detail in visited_details:
                # In a loop!
                still_walking = False
                will_loop = True
            else:
                visited_details.add(location_detail)

            steps_taken += 1

    if return_locations:
        return visited_locations
    else:
        return will_loop


def solve_puzzle():
    # Main solving logic
    map_data, start_x, start_y, size_x, size_y = read_input_data()
    dir_data = get_direction_data()

    count_tests = 0
    count_loops = 0

    modified_map_data = map_data.copy()
    patrol_locations = test_map_for_loop(
        modified_map_data,
        start_x,
        start_y,
        size_x,
        size_y,
        dir_data,
        return_locations=True,
    )
    print(f"First test visits {len(patrol_locations)} locations")
    print(f"Start locations are {start_x},{start_y}")

    for each_location in patrol_locations:
        test_x = each_location[0]
        test_y = each_location[1]

        if map_data[(test_x, test_y)] == ".":
            count_tests += 1
            print(f"Testing obstacle location number: {count_tests}")
            modified_map_data = map_data.copy()
            modified_map_data[(test_x, test_y)] = "O"
            will_loop = test_map_for_loop(
                modified_map_data, start_x, start_y, size_x, size_y, dir_data
            )
            if will_loop:
                count_loops += 1

    print(f"Found {count_loops} solutions which cause a loop")


if __name__ == "__main__":
    solve_puzzle()
