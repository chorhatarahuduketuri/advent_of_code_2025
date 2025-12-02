import pytest

from src import day_2

input_1_day_2 = (
    "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,"
    "38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
)

input_2_day_2 = """"""

output_day_2_star_1 = 1227775554
output_day_2_star_2 = ...

day_2_star_1_test_input = [(input_1_day_2, output_day_2_star_1)]
day_2_star_2_test_input = [(input_2_day_2, output_day_2_star_2)]


@pytest.mark.parametrize("puzzle_input, output", day_2_star_1_test_input)
def test_day_2_star_1(puzzle_input: str, output: int):
    assert day_2.compute_star_1(puzzle_input) == output


@pytest.mark.parametrize("puzzle_input, output", day_2_star_2_test_input)
def test_day_2_star_2(puzzle_input: str, output: int):
    assert day_2.compute_star_2(puzzle_input) == output
