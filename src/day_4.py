import numpy as np

from src.settings import PUZZLE_INPUT_PATH


def _count_accessible_directions(grid: np.ndarray, i: int, j: int) -> int:
    counter = 0
    surrounding_directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for d_i, d_j in surrounding_directions:
        s_i = d_i + i
        s_j = d_j + j
        if s_i < 0 or s_i >= len(grid) or s_j < 0 or s_j >= len(grid):  # if off the side of the grid
            counter += 1
        elif grid[s_i, s_j] == ".":  # else if on the grid
            counter += 1
    return counter


def is_accessible(grid: np.ndarray, position: str, i: int, j: int) -> int:
    """Important assumption: grid is definitely square, so len(grid) == len(grid[0])"""
    if position == ".":
        return 0  # False: No paper to be accessed, regardless of surrounding positions
    counter = _count_accessible_directions(grid, i, j)
    if counter > 4:
        return 1  # True
    return 0  # False


def get_accessibility(grid: np.ndarray) -> np.ndarray:
    return np.asarray(
        [[is_accessible(grid, position, i, j) for j, position in enumerate(row)] for i, row in enumerate(grid)]
    )


def compute_star_1(puzzle_input: str) -> int:
    grid = np.asarray([[position for position in row.strip()] for row in puzzle_input.strip().split()], str)
    accessibility = get_accessibility(grid)
    return accessibility.sum()


def remove_rolls_from_grid(grid: np.ndarray, accessibility: np.ndarray):
    return np.asarray(
        [
            [position if accessibility[i, j] == 0 else "." for j, position in enumerate(row)]
            for i, row in enumerate(grid)
        ]
    )


def compute_star_2(puzzle_input: str) -> int:
    grid = np.asarray([[position for position in row.strip()] for row in puzzle_input.strip().split()], str)
    removed_rolls = 0
    accessibility = get_accessibility(grid)
    while accessibility.sum() > 0:
        removed_rolls += accessibility.sum()
        grid = remove_rolls_from_grid(grid, accessibility)
        accessibility = get_accessibility(grid)
    return removed_rolls


if __name__ == "__main__":
    print("day 4, star 1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day4.txt").read()))
    print("day 4, star 2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day4.txt").read()))
