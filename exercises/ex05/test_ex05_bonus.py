# Tests for the bonus (see BONUS.md). If you copied the ex05 folder before this file
# existed, copy just this file into your students/<login>/ex05 folder.
#
# They are skipped until your ex05.py has a function `lowest_risk_with_shields`, so they
# don't turn CI red if you don't do the bonus.

import pytest

import ex05

pytestmark = pytest.mark.skipif(
    not hasattr(ex05, "lowest_risk_with_shields"),
    reason="bonus not attempted: ex05.py has no lowest_risk_with_shields",
)


def test_no_shields_is_part_2():
    assert ex05.lowest_risk_with_shields([[1, 2], [3, 4]], 0) == 6
    assert ex05.lowest_risk_with_shields(ex05.parse_grid(ex05.EXAMPLE_TEXT), 0) == 12


def test_one_position():
    assert ex05.lowest_risk_with_shields([[5]], 0) == 0
    assert ex05.lowest_risk_with_shields([[5]], 2) == 0


def test_shield_on_the_nine():
    assert ex05.lowest_risk_with_shields([[1, 9], [9, 1]], 1) == 1


def test_more_shields_than_steps():
    assert ex05.lowest_risk_with_shields([[1, 2], [3, 4]], 2) == 0
    assert ex05.lowest_risk_with_shields([[1, 2], [3, 4]], 5) == 0


def test_shields_on_the_example():
    grid = ex05.parse_grid(ex05.EXAMPLE_TEXT)
    assert ex05.lowest_risk_with_shields(grid, 1) == 7
    assert ex05.lowest_risk_with_shields(grid, 3) == 5


def test_does_not_change_grid():
    grid = ex05.parse_grid(ex05.EXAMPLE_TEXT)
    before = ex05.parse_grid(ex05.EXAMPLE_TEXT)
    ex05.lowest_risk_with_shields(grid, 2)
    assert grid == before
