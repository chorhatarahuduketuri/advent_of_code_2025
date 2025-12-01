from src.settings import PUZZLE_INPUT_PATH
import re


def compute_star_1(puzzle_input: str) -> int:
    position = 50
    count_of_zero_positions = 0
    moves = [tuple(re.findall(r"[RL]+|\d+", line.strip())) for line in puzzle_input.strip().split("\n")]
    for direction, magnitude in moves:
        if direction == 'L':
            position = (position - int(magnitude)) % 100
        else:
            position = (position + int(magnitude)) % 100
        if position == 0:
            count_of_zero_positions += 1
    return count_of_zero_positions


def compute_star_2(puzzle_input: str) -> int:
    pass

print("day 1, star 1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day1.txt").read()))
print("day 1, star 2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day1.txt").read()))
