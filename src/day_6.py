import math
import re

import numpy as np

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


def solve_and_append_problem(numbers: list[int], operator: str | None, problems: list[int]) -> tuple[list[int], str]:
    if operator == "+":
        problem = sum(numbers)
        problems.append(problem)
        numbers = []
        operator = None  # Not strictly necessary
    else:
        problem = math.prod(numbers)
        problems.append(problem)
        numbers = []
        operator = None  # Not strictly necessary
    return numbers, operator


def compute_star_2(puzzle_input: str) -> int:
    grid = np.asarray([[char for char in line] for line in puzzle_input.strip("\n").split("\n")])

    problems = []
    numbers = []
    operator = None
    for i in range(len(grid[0])):
        potential_number = "".join([x for x in grid[:-1, i] if x.strip()])
        if potential_number:
            numbers.append(int(potential_number))
            potential_operator = grid[-1, i]
            operator = potential_operator if potential_operator.strip() else operator
        else:
            numbers, operator = solve_and_append_problem(numbers, operator, problems)
    # solve final problem
    numbers, operator = solve_and_append_problem(numbers, operator, problems)

    return sum(problems)


if __name__ == "__main__":
    print("day 6, star 1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day6.txt").read()))
    print("day 6, star 2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day6.txt").read()))
