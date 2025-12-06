import pytest

from src import day_6

input_1_day_6 = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

input_2_day_6 = """"""

output_day_6_star_1 = 4277556
output_day_6_star_2 = ...

day_6_star_1_test_input = [(input_1_day_6, output_day_6_star_1)]
day_6_star_2_test_input = [(input_2_day_6, output_day_6_star_2)]


@pytest.mark.parametrize("puzzle_input, output", day_6_star_1_test_input)
def test_day_6_star_1(puzzle_input: str, output: int):
    assert day_6.compute_star_1(puzzle_input) == output


@pytest.mark.parametrize("puzzle_input, output", day_6_star_2_test_input)
def test_day_6_star_2(puzzle_input: str, output: int):
    assert day_6.compute_star_2(puzzle_input) == output
