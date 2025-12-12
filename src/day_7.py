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


def compute_star_2(puzzle_input: str) -> int:
    pass


if __name__ == "__main__":
    print("day 7, star 1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day7.txt").read()))
    print("day 7, star 2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day7.txt").read()))
