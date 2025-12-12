import numpy as np

from src.settings import PUZZLE_INPUT_PATH


def propagate_tachyon_beams(beam_splits: int, grid: np.ndarray, incoming_tachyon_beams: set[int]) -> int:
    for row_num, row in enumerate(grid[1:]):
        current_row_tachyon_beams: set[int] = set()
        for col_num, position in enumerate(row):
            if col_num in incoming_tachyon_beams:
                if position == "^":
                    current_row_tachyon_beams.add(col_num - 1)
                    current_row_tachyon_beams.add(col_num + 1)
                    beam_splits += 1
                else:
                    current_row_tachyon_beams.add(col_num)
        incoming_tachyon_beams = current_row_tachyon_beams
    return beam_splits


def compute_star_1(puzzle_input: str) -> int:
    grid = np.asarray([[position for position in row.strip()] for row in puzzle_input.strip().split()])
    incoming_tachyon_beams: set[int] = set()
    beam_splits = 0
    for col_num, position in enumerate(grid[0]):
        if position == "S":
            incoming_tachyon_beams.add(col_num)
            break
    beam_splits = propagate_tachyon_beams(beam_splits, grid, incoming_tachyon_beams)
    return beam_splits


def propagate_timelines(grid: np.ndarray) -> int:
    for row_num in range(1, grid.shape[0]):
        for col_num in range(grid.shape[1]):
            if grid[row_num, col_num] == -1:
                if grid[row_num - 1, col_num] > 0:
                    # There are no consecutive splitters (or any adjacent at all), so this is blind-safe
                    grid[row_num, col_num - 1] += grid[row_num - 1, col_num]
                    grid[row_num, col_num + 1] += grid[row_num - 1, col_num]
            else:
                if grid[row_num - 1, col_num] > 0:
                    grid[row_num, col_num] += grid[row_num - 1, col_num]
    timelines_count = sum(grid[-1])
    return timelines_count


def compute_star_2(puzzle_input: str) -> int:
    grid = np.asarray(
        [
            [0 if position == "." else 1 if position == "S" else -1 for position in row.strip()]
            for row in puzzle_input.strip().split()
        ]
    )
    timelines_count = propagate_timelines(grid)
    return timelines_count


if __name__ == "__main__":
    print("day 7, star 1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day7.txt").read()))
    print("day 7, star 2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day7.txt").read()))
