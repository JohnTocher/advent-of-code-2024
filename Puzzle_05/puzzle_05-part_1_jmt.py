""" Advent of code 2024 - Puzzle 05

    https://adventofcode.com/2024/day/5

    John Tocher     
    Solution to puzzle 05 part 1
"""

# INPUT_FILE_NAME = "puzzle_05_input_01_sample.txt"
INPUT_FILE_NAME = "puzzle_05_input_01.txt"


def read_input_data():
    # Read the puzzle input from a text file
    pages_before = dict()
    updates = list()

    for single_line in open(INPUT_FILE_NAME, "r").readlines():
        clean_line = single_line.strip()
        if "|" in clean_line:
            page_text = clean_line.split("|")
            page_left = int(page_text[0])
            page_after = int(page_text[1])
            new_list = pages_before.get(page_after, list())
            new_list.append(page_left)
            pages_before[page_after] = new_list
        else:
            if len(clean_line) > 1:
                update_pages = [int(page_text) for page_text in clean_line.split(",")]
                updates.append(update_pages)

    return pages_before, updates


def solve_puzzle():
    # Main solving logic
    pages_before, updates = read_input_data()
    # print(f"{pages_before[13]}")
    # print(f"{updates[3]}")

    middle_sum = 0

    for each_update in updates:
        order_ok = True
        for page_index in range(0, len(each_update) - 1):
            # Make sure note of the pages which MUST come before exist after the page
            for check_index in range(page_index + 1, len(each_update)):
                if each_update[page_index] in pages_before:
                    if (
                        each_update[check_index]
                        in pages_before[each_update[page_index]]
                    ):
                        order_ok = False
                        break
        if order_ok:
            middle_index = int(len(each_update) / 2)
            middle_sum += each_update[middle_index]
            print(f"Order ok for {each_update} - middle is {each_update[middle_index]}")

    print(f"Result: {middle_sum}")


if __name__ == "__main__":
    solve_puzzle()
