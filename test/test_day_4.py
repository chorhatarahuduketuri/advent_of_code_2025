import pytest

from src import day_4

input_1_day_4 = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

input_2_day_4 = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

output_day_4_star_1 = 13
output_day_4_star_2 = 43

day_4_star_1_test_input = [(input_1_day_4, output_day_4_star_1)]
day_4_star_2_test_input = [(input_2_day_4, output_day_4_star_2)]


@pytest.mark.parametrize("puzzle_input, output", day_4_star_1_test_input)
def test_day_4_star_1(puzzle_input: str, output: int):
    assert day_4.compute_star_1(puzzle_input) == output


@pytest.mark.parametrize("puzzle_input, output", day_4_star_2_test_input)
def test_day_4_star_2(puzzle_input: str, output: int):
    assert day_4.compute_star_2(puzzle_input) == output
