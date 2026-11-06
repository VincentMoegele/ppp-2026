# Exercise 01: warm-ups and Santa's elevator

|  |  |
|---|---|
| **AI level** | **0**: no AI, and inline completion stays off |
| **Part 1** | in class, Fri Oct 2 |
| **Part 2** | at home |
| **Due** | Thu Oct 8, 17:00, as a pull request |
| **Review due** | Tue Oct 13, 17:00 (author answers before the Wednesday session) |

## Getting started

```
git checkout main
git pull
git checkout -b ex01-<login>
```

Copy the folder `exercises/ex01` to `students/<login>/ex01` and work only in the copy.
It contains:

- `ex01.py`: the functions you fill in. Each already has its first line and a description.
  Replace each `pass` line with your code, ending with `return`.
- `test_ex01.py`: tests for your functions. At the start, all of them fail.
- `puzzle_input.py`: the input for the elevator puzzle.

Check your work with

```
uv run pytest students/<login>/ex01
```

and see your answers with

```
uv run python students/<login>/ex01/ex01.py
```

## Part 1 (in class)

**Warm-ups.** Fill in `quotient_and_remainder`, `celsius_to_fahrenheit`, `first_three`,
`last_four`, `backwards` and `science_to_analytics`.

**Santa's elevator.** 
Santa is in a large building, on floor 0, and follows a list of instructions,
one character each: `(` means *go up one floor*, `)` means *go down one floor*.
The building is very tall and has many basement floors, so he never reaches the top or the
bottom. Fill in `floor`: on which floor does Santa end up?

## Part 2 (at home)

Part 2 builds on **your own** Part 1 code.

1. `floor_after`: on which floor is Santa after following only the first `steps` instructions?
   Use your function `floor`.
2. `mirrored`: the instructions were written in a mirror. Every `(` should be a `)` and vice
   versa. Return the corrected instructions. *Careful: check your result with a short example
   by hand before you trust it.*
3. `common_elements` and `count_letter`: two list warm-ups, see the descriptions in `ex01.py`.
4. **Add at least two tests of your own** at the end of `test_ex01.py`. Copy an existing test
   and change it. Good tests check cases the existing tests don't: what happens with empty
   input? With a very short string?

**Bonus (optional):** at which position does Santa enter the basement (floor -1) for the
first time? You need a loop for this, which we'll learn next week. If you want to try, go
ahead; or keep the question in mind for Friday.

## Your pull request

- Title: `ex01 <login>`
- Paste the output of `uv run python students/<login>/ex01/ex01.py` under **Result**.
- CI must be green: all tests pass, ruff is happy.
