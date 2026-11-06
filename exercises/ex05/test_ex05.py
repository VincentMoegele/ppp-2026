from ex05 import (
    EXAMPLE_PATH,
    EXAMPLE_TEXT,
    lowest_risk,
    lowest_risk_any_direction,
    neighbours,
    parse_grid,
    path_risk,
)

# ---------------------------------------------------------------- Part 1


def test_parse_grid():
    assert parse_grid("12\n34\n") == [[1, 2], [3, 4]]


def test_parse_grid_blank_lines_and_spaces():
    assert parse_grid("\n  12 \n34\n\n") == [[1, 2], [3, 4]]


def test_parse_grid_example():
    grid = parse_grid(EXAMPLE_TEXT)
    assert len(grid) == 5
    assert grid[1] == [1, 9, 1, 1, 1]


def test_path_risk_start_only():
    assert path_risk([[5]], [(0, 0)]) == 0


def test_path_risk_example_path():
    assert path_risk(parse_grid(EXAMPLE_TEXT), EXAMPLE_PATH) == 12


def test_lowest_risk_one_position():
    assert lowest_risk([[5]]) == 0


def test_lowest_risk_two_by_two():
    assert lowest_risk([[1, 2], [3, 4]]) == 6
    assert lowest_risk([[1, 9], [1, 1]]) == 2


def test_lowest_risk_three_by_three():
    assert lowest_risk([[1, 1, 9], [2, 9, 9], [1, 1, 1]]) == 5


def test_lowest_risk_example():
    assert lowest_risk(parse_grid(EXAMPLE_TEXT)) == 16


def test_lowest_risk_from_the_middle():
    grid = parse_grid(EXAMPLE_TEXT)
    assert lowest_risk(grid, 3, 2) == 11
    assert lowest_risk(grid, 4, 0) == 28


def test_lowest_risk_does_not_change_grid():
    grid = parse_grid(EXAMPLE_TEXT)
    before = parse_grid(EXAMPLE_TEXT)
    lowest_risk(grid)
    assert grid == before


# ---------------------------------------------------------------- Part 2
# Add at least two tests of your own below. One of them must use a grid of your own in which
# moving in any direction is cheaper than moving only right and down.


def test_neighbours_corner():
    grid = parse_grid(EXAMPLE_TEXT)
    assert sorted(neighbours(grid, 0, 0)) == [(0, 1), (1, 0)]


def test_neighbours_middle():
    grid = parse_grid(EXAMPLE_TEXT)
    assert sorted(neighbours(grid, 2, 2)) == [(1, 2), (2, 1), (2, 3), (3, 2)]


def test_lowest_risk_any_direction_example():
    assert lowest_risk_any_direction(parse_grid(EXAMPLE_TEXT)) == 12


def test_lowest_risk_any_direction_small():
    assert lowest_risk_any_direction([[5]]) == 0
    assert lowest_risk_any_direction([[1, 2], [3, 4]]) == 6
