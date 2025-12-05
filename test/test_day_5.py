import pytest

from src import day_5

input_1_day_5 = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

input_2_day_5 = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

output_day_5_star_1 = 3
output_day_5_star_2 = 14

day_5_star_1_test_input = [(input_1_day_5, output_day_5_star_1)]
day_5_star_2_test_input = [(input_2_day_5, output_day_5_star_2)]


@pytest.mark.parametrize("puzzle_input, output", day_5_star_1_test_input)
def test_day_5_star_1(puzzle_input: str, output: int):
    assert day_5.compute_star_1(puzzle_input) == output


@pytest.mark.parametrize("puzzle_input, output", day_5_star_2_test_input)
def test_day_5_star_2(puzzle_input: str, output: int):
    assert day_5.compute_star_2(puzzle_input) == output
