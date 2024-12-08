""" Advent of code 2024 - Puzzle 03

    https://adventofcode.com/2024/day/3

    John Tocher     
    Solution to puzzle 03 part 2
"""

# INPUT_FILE_NAME = "puzzle_03_input_02_sample.txt"
INPUT_FILE_NAME = "puzzle_03_input_01.txt"


def read_input_data():
    # Read the puzzle input from a text file
    count_lines = 0
    lines_of_input = list()

    for single_line in open(INPUT_FILE_NAME, "r").readlines():
        count_lines += 1
        clean_line = single_line.strip()
        lines_of_input.append(clean_line)

    return lines_of_input


def solve_puzzle():
    # Main solving logic
    puzzle_input = read_input_data()
    product_sum = 0
    count_lines = 0
    mult_enabled = True
    for each_line in puzzle_input:
        more_to_check = True
        start_pos = 0
        count_lines += 1
        # if count_lines == 4:
        #    assert False, "Test!"
        while more_to_check:
            cmd_pos = each_line.find("mul(", start_pos)
            # Now we need to check if there are any valid dos or donts before our command
            do_pos = each_line.rfind("do()", start_pos, cmd_pos)
            dont_pos = each_line.rfind("don't()", start_pos, cmd_pos)

            if do_pos > 0 and dont_pos > 0:
                # We have both enab;ed /disable, see which one is later
                print(f"Do at: {do_pos} Dont at {dont_pos}")
                if do_pos > dont_pos:
                    mult_enabled = True
                else:
                    mult_enabled = False
            elif do_pos > 0:
                # Just the enable command
                print(f"Do at: {do_pos} ")
                mult_enabled = True
            elif dont_pos > 0:
                # Just the disable command
                print(f"Dont at: {dont_pos} ")
                mult_enabled = False

            if cmd_pos >= start_pos:
                # check if it's valid
                close_pos = each_line.find(")", cmd_pos)
                if close_pos:
                    potential_cmd = each_line[cmd_pos + 4 : close_pos]
                    debug_text = f"Line {count_lines} potential cmd at pos: {cmd_pos}:{potential_cmd}"
                    comma_pos = potential_cmd.count(",")
                    if comma_pos == 1:
                        number_parts = potential_cmd.split(",")
                        numbers_ok = True
                        for each_number in number_parts:
                            for each_char in each_number:
                                if not each_char.isdigit():
                                    numbers_ok = False
                                    break
                        if numbers_ok:
                            this_product = int(number_parts[0]) * int(number_parts[1])
                            debug_text = f"{debug_text} - Product:{this_product}"
                            if mult_enabled:
                                product_sum += this_product
                            start_pos = cmd_pos + 4
                        else:
                            debug_text = f"{debug_text} - Failed: bad characters"
                            start_pos = cmd_pos + 4

                    else:
                        debug_text = f"{debug_text} - Failed: wrong comma count"
                        start_pos = cmd_pos + 4

                    print(debug_text)

                else:
                    # No closing bracket for this cmd means no closing for any - we're done
                    more_to_check = False
            else:
                # Not found
                more_to_check = False

            if start_pos + 8 > len(each_line):
                more_to_check = False

    print(f"Result: {product_sum}")


if __name__ == "__main__":
    solve_puzzle()
