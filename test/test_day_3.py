import pytest

from src import day_3

input_1_day_3 = """987654321111111
811111111111119
234234234234278
818181911112111"""

input_2_day_3 = """"""

output_day_3_star_1 = 357
output_day_3_star_2 = ...

day_3_star_1_test_input = [(input_1_day_3, output_day_3_star_1)]
day_3_star_2_test_input = [(input_2_day_3, output_day_3_star_2)]


@pytest.mark.parametrize("puzzle_input, output", day_3_star_1_test_input)
def test_day_3_star_1(puzzle_input: str, output: int):
    assert day_3.compute_star_1(puzzle_input) == output


@pytest.mark.parametrize("puzzle_input, output", day_3_star_2_test_input)
def test_day_3_star_2(puzzle_input: str, output: int):
    assert day_3.compute_star_2(puzzle_input) == output
