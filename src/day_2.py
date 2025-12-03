import re

from src.settings import PUZZLE_INPUT_PATH

re_repetitions_only = re.compile(r"^(.+?)\1+$")


def is_invalid_id_star_1(i: str) -> bool:
    if len(i) % 2 == 1:
        return False
    if i[: int(len(i) / 2)] == i[int(len(i) / 2) :]:
        return True
    else:
        return False


def compute_star_1(puzzle_input: str) -> int:
    ids = [[int(i) for i in id_range.strip().split("-")] for id_range in puzzle_input.strip().split(",")]
    sum_invalid_ids = 0
    for id_range in ids:
        for i in range(id_range[0], id_range[1] + 1):
            if is_invalid_id_star_1(str(i)):
                sum_invalid_ids += i
    return sum_invalid_ids


def is_invalid_id_star_2(i: str) -> bool:
    if re_repetitions_only.match(i):
        return True
    return False


def compute_star_2(puzzle_input: str) -> int:
    ids = [[int(i) for i in id_range.strip().split("-")] for id_range in puzzle_input.strip().split(",")]
    sum_invalid_ids = 0
    for id_range in ids:
        for i in range(id_range[0], id_range[1] + 1):
            if is_invalid_id_star_2(str(i)):
                sum_invalid_ids += i
    return sum_invalid_ids


if __name__ == "__main__":
    print("day 2, star 1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day2.txt").read()))
    print("day 2, star 2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day2.txt").read()))
