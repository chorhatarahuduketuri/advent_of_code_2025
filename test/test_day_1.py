import pytest

from src import day_1

input_1_day_1 = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

input_2_day_1 = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

output_day_1_star_1 = 3
output_day_1_star_2 = 6

day_1_star_1_test_input = [(input_1_day_1, output_day_1_star_1)]
day_1_star_2_test_input = [(input_2_day_1, output_day_1_star_2)]


@pytest.mark.parametrize("puzzle_input, output", day_1_star_1_test_input)
def test_day_1_star_1(puzzle_input: str, output: int):
    assert day_1.compute_star_1(puzzle_input) == output


@pytest.mark.parametrize("puzzle_input, output", day_1_star_2_test_input)
def test_day_1_star_2(puzzle_input: str, output: int):
    assert day_1.compute_star_2(puzzle_input) == output
