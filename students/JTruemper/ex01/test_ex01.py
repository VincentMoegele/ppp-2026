import pytest
from ex01 import (
    backwards,
    celsius_to_fahrenheit,
    common_elements,
    count_letter,
    first_three,
    floor,
    floor_after,
    last_four,
    mirrored,
    quotient_and_remainder,
    science_to_analytics,
)

# ---------------------------------------------------------------- Part 1


def test_quotient_and_remainder():
    assert quotient_and_remainder(17, 5) == (3, 2)
    with pytest.raises(ZeroDivisionError):
        quotient_and_remainder(2, 0)


def test_quotient_and_remainder_no_remainder():
    assert quotient_and_remainder(10, 5) == (2, 0)


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(0) == 32


def test_celsius_to_fahrenheit_same_value():
    # -40 °C is -40 °F
    assert celsius_to_fahrenheit(-40) == -40


def test_first_three():
    assert first_three("Python") == "Pyt"


def test_last_four():
    assert last_four("Python") == "thon"


def test_backwards():
    assert backwards("Python") == "nohtyP"


def test_science_to_analytics():
    assert science_to_analytics("DataScience") == "DataAnalytics"


def test_floor():
    assert floor("(((") == 3
    assert floor("(()") == 1


def test_floor_below_zero():
    assert floor("())))") == -3


def test_floor_up_and_down():
    assert floor("()()") == 0


# ---------------------------------------------------------------- Part 2
# Add at least two tests of your own below, for the Part 2 functions.


def test_floor_after():
    assert floor_after("((())", 3) == 3


def test_mirrored():
    assert mirrored("(()") == "))("
    assert mirrored(")))))(((((") == "((((()))))"


def test_common_elements():
    assert common_elements(["a", "b", "c"], ["b", "c", "d"]) == {"b", "c"}


def test_count_letter():
    assert count_letter(["banana", "apple"], "a") == 4
