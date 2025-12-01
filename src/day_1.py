from src.settings import PUZZLE_INPUT_PATH
import re


def compute_star_1(puzzle_input: str) -> int:
    position = 50
    count_of_zero_positions = 0
    moves = [tuple(re.findall(r"[RL]+|\d+", line.strip())) for line in puzzle_input.strip().split("\n")]
    for direction, magnitude in moves:
        if direction == "L":
            position = (position - int(magnitude)) % 100
        else:
            position = (position + int(magnitude)) % 100
        if position == 0:
            count_of_zero_positions += 1
    return count_of_zero_positions


def compute_star_2(puzzle_input: str) -> int:
    position = 50
    count_of_zero_crossings = 0
    moves = [tuple(re.findall(r"[RL]+|\d+", line.strip())) for line in puzzle_input.strip().split("\n")]
    for direction, magnitude in moves:
        if direction == "L":
            zero_crossings = abs((position - int(magnitude)) // 100)
            if position == 0:
                count_of_zero_crossings += zero_crossings
                if int(magnitude) > position and zero_crossings > 0:
                    count_of_zero_crossings -= 1  # uncount moving from zero to 99
                position = (position - int(magnitude)) % 100
            else:
                count_of_zero_crossings += zero_crossings
                position = (position - int(magnitude)) % 100
                if position == 0:
                    count_of_zero_crossings += 1  # count landing onto zero
        else:  # direction == 'R'
            count_of_zero_crossings += abs((position + int(magnitude)) // 100)
            position = (position + int(magnitude)) % 100
    return count_of_zero_crossings


print("day 1, star 1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day1.txt").read()))
print("day 1, star 2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day1.txt").read()))
