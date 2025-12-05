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


def compute_star_2(puzzle_input: str) -> int:
    pass


if __name__ == "__main__":
    print("day 5, star 1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day5.txt").read()))
    print("day 5, star 2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day5.txt").read()))
