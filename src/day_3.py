from src.settings import PUZZLE_INPUT_PATH


def get_max_joltage_per_bank(bank: list[int]) -> int:
    max_battery = max(bank)
    i_max_battery = bank.index(max_battery)
    if i_max_battery >= len(bank) - 1:
        second_battery = max_battery
        max_battery = max(bank[:i_max_battery])
    else:
        second_battery = max(bank[i_max_battery + 1 :])
    max_joltage = int("".join([str(max_battery), str(second_battery)]))

    return max_joltage


def compute_star_1(puzzle_input: str) -> int:
    banks = [[int(joltage) for joltage in bank] for bank in puzzle_input.strip().split()]
    max_possible_joltage = sum(get_max_joltage_per_bank(bank) for bank in banks)
    return max_possible_joltage


def compute_star_2(puzzle_input: str) -> int:
    pass


print("day 3, star 1: ", compute_star_1(open(PUZZLE_INPUT_PATH / "day3.txt").read()))
print("day 3, star 2: ", compute_star_2(open(PUZZLE_INPUT_PATH / "day3.txt").read()))
