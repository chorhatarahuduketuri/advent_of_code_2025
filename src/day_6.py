import math
import re

from src.settings import PUZZLE_INPUT_PATH


def math_operation(nums: list[str], operation: str) -> int:
    if operation == "+":
        return sum(int(num) for num in nums)
    elif operation == "*":
        return math.prod(int(num) for num in nums)
    else:
        raise ValueError(f"Operation {operation} not supported")


def compute_star_1(puzzle_input: str) -> int:
    parsed_input = [re.split(pattern=r"\s+", string=line.strip()) for line in puzzle_input.strip().split("\n")]
    problems = [element for element in zip(*parsed_input)]
    answers = [math_operation(problem[0:-1], problem[-1]) for problem in problems]
    return sum(answers)


def compute_star_2(puzzle_input: str) -> int:
    pass


if __name__ == "__main__":
    print("day 6, star 1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day6.txt").read()))
    print("day 6, star 2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day6.txt").read()))
