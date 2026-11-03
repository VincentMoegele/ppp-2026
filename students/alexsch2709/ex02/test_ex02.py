from ex02 import find_noun_verb, run, run_with, step

# ---------------------------------------------------------------- Part 1


def test_step_add():
    memory = [1, 0, 0, 0, 99]
    assert step(memory, 0) == 4
    assert memory == [2, 0, 0, 0, 99]


def test_step_multiply():
    memory = [2, 3, 0, 3, 99]
    assert step(memory, 0) == 4
    assert memory == [2, 3, 0, 6, 99]


def test_step_at_a_later_position():
    memory = [1, 0, 0, 0, 2, 4, 4, 0, 99]
    assert step(memory, 4) == 8
    assert memory == [4, 0, 0, 0, 2, 4, 4, 0, 99]


def test_step_halt():
    assert step([99], 0) is None


def test_run():
    assert run([1, 5, 6, 0, 99, 20, 22]) == 42


def test_run_reads_what_it_wrote():
    assert run([2, 9, 10, 9, 1, 9, 11, 0, 99, 6, 7, 3]) == 45


def test_run_changes_its_own_program():
    # the first instruction writes 99 to position 4
    assert run([1, 9, 10, 4, 1, 0, 0, 0, 99, 50, 49]) == 1


# ---------------------------------------------------------------- Part 2
# Add at least two tests of your own below, for the Part 2 functions.

# computes 100 * noun + verb
HUNDRED_NOUN_PLUS_VERB = [1, 0, 0, 3, 2, 1, 13, 13, 1, 13, 2, 0, 99, 100] + [0] * 86


def test_run_with():
    assert run_with(HUNDRED_NOUN_PLUS_VERB, 12, 34) == 1234


def test_find_noun_verb():
    assert find_noun_verb(HUNDRED_NOUN_PLUS_VERB, 1234) == (12, 34)


def test_step_self():
    memory = [1, 2, 1, 0, 99]
    assert step(memory, 0) == 4
    assert memory == [3, 2, 1, 0, 99]


def test_run_with_self():
    assert run_with(HUNDRED_NOUN_PLUS_VERB, 22, 33) == 2233


def test_noun_verb_self():
    assert find_noun_verb(HUNDRED_NOUN_PLUS_VERB, 9999) == (99, 99)
