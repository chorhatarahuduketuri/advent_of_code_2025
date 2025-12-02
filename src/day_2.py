from src.settings import PUZZLE_INPUT_PATH


def is_invalid_id(i: str) -> bool:
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
            if is_invalid_id(str(i)):
                sum_invalid_ids += i
    return sum_invalid_ids


def compute_star_2(puzzle_input: str) -> int:
    pass


print("day 2, star 1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day2.txt").read()))
print("day 2, star 2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day2.txt").read()))
