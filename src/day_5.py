from src.settings import PUZZLE_INPUT_PATH


def is_id_in_range(ingredient_id: int, range_pair: list[int]) -> bool:
    return range_pair[0] <= ingredient_id <= range_pair[1]


def compute_star_1(puzzle_input: str) -> int:
    ranges_ingredients = [segment for segment in puzzle_input.strip().split("\n\n")]

    ranges = [[int(r) for r in rangez.split("-")] for rangez in ranges_ingredients[0].split()]
    ingredients = [int(ingredient) for ingredient in ranges_ingredients[1].split()]

    fresh_ingredient_count = 0
    for ingredient in ingredients:
        for r in ranges:
            if is_id_in_range(ingredient, r):
                fresh_ingredient_count += 1
                break

    return fresh_ingredient_count


def merge_two_ranges(range_1: list[int], range_2: list[int]) -> list[int]:
    return [min(range_1[0], range_2[0]), max(range_1[1], range_2[1])]


def merge_all_ranges(ranges_sorted: list[list[int]]) -> list[list[int]]:
    all_merged_ranges = [ranges_sorted[0]]
    for r in ranges_sorted[1:]:
        if all_merged_ranges[-1][1] < r[0]:
            all_merged_ranges.append(r)
        else:
            all_merged_ranges[-1] = merge_two_ranges(all_merged_ranges[-1], r)
    return all_merged_ranges


def count_fresh_ranges(ranges_merged: list[list[int]]) -> int:
    count = 0
    for merged_range in ranges_merged:
        count += merged_range[1] + 1 - merged_range[0]
    return count


def compute_star_2(puzzle_input: str) -> int:
    ranges = [segment for segment in puzzle_input.strip().split("\n\n")][0]

    ranges_sorted = sorted(
        [[int(r) for r in rangez.split("-")] for rangez in ranges.split()], key=lambda x: (x[0], x[1])
    )

    ranges_merged = merge_all_ranges(ranges_sorted)

    count = count_fresh_ranges(ranges_merged)

    return count


if __name__ == "__main__":
    print("day 5, star 1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day5.txt").read()))
    print("day 5, star 2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day5.txt").read()))
