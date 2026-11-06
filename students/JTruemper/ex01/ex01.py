# Exercise 01. See README.md for the full task.
# Each function below has its first line written for you. The text in triple quotes says
# what the function should do. Replace the `pass` line with your code, ending with `return`.

from puzzle_input import INSTRUCTIONS

# ---------------------------------------------------------------- Part 1 (in class)


def quotient_and_remainder(a, b):
    """Return the quotient and remainder of the integer division a // b, e.g. (3, 2) for 17, 5."""
    if b == 0:
        raise ZeroDivisionError("Division by 0 is not allowed!")
    return (a // b, a % b)


def celsius_to_fahrenheit(celsius):
    """Return the temperature celsius (in °C) converted to °F."""
    return (celsius * 1.8) + 32


def first_three(text):
    """Return the first three characters of text."""
    return text[:3]


def last_four(text):
    """Return the last four characters of text."""
    return text[-4:]


def backwards(text):
    """Return text backwards."""
    return text[::-1]


def science_to_analytics(text):
    """Return text with every "Science" replaced by "Analytics"."""
    return text.replace("Science", "Analytics")


def floor(instructions):
    """Return the floor Santa ends up on, starting on floor 0: "(" is one up, ")" one down."""
    return instructions.count("(") - instructions.count(")")


# ---------------------------------------------------------------- Part 2 (at home) (Did not get to do Part 1 in class anyways)


def floor_after(instructions, steps):
    """Return the floor Santa is on after following only the first `steps` instructions.

    Use your function `floor` from Part 1.
    """
    return floor(instructions[:steps])


def mirrored(instructions):
    """Return the instructions as seen in a mirror: every "(" becomes ")" and vice versa."""
    return instructions.replace("(", "x").replace(")", "y").replace("x", ")").replace("y", "(")


def common_elements(first, second):
    """Return the set of elements that occur in both lists."""
    return set(first) & set(second)


def count_letter(words, letter):
    """Return how often letter occurs in all the strings of the list words together."""
    return ("".join(words)).count(letter)  # replace this line with your code


# ---------------------------------------------------------------- Answers

# The lines below run when you run this file (`uv run python ex01.py`), but not when the
# tests import it. Leave the `if` line as it is; we'll see what it means later.
if __name__ == "__main__":
    first_list = ["drs", "clt", "iny", "alv", "nvy", "bpt", "gkw", "fkm", "jrz", "hov", "bqu",
                  "bov", "eju", "eiz", "fjm", "bek", "abj", "hov", "coq", "iox", "efs", "krw",
                  "evy", "elw", "gil", "ajq", "cek", "fkm", "mnu", "adf"]  # fmt: skip
    second_list = ["dlz", "akw", "bry", "eyz", "bny", "kst", "elw", "ekl", "djm", "aft", "gkw",
                   "krw", "coq", "evy", "bov", "bkl", "bov", "afs", "hov", "fjq", "cqu", "ahq",
                   "beh", "ijz", "ksy", "ilx", "htu", "epz", "ekl", "ajq"]  # fmt: skip

    print("Part 1")
    print("1:", quotient_and_remainder(2711274328912, 23369245575))
    print("2:", celsius_to_fahrenheit(233))
    print("3:", first_three("DataScience"), last_four("DataScience"))
    print("4:", backwards("DataScience"), science_to_analytics("DataScience"))
    print("5:", floor(INSTRUCTIONS))
    print("Part 2")
    print("6:", floor_after(INSTRUCTIONS, 1000))
    print("7:", floor(mirrored(INSTRUCTIONS)))
    print("8:", len(first_list), len(second_list))
    print("9:", common_elements(first_list, second_list))
    print("10:", count_letter(first_list, "a"), count_letter(second_list, "a"))
