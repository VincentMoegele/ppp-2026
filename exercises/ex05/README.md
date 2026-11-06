# Exercise 05: through the cave

|  |  |
|---|---|
| **AI level** | **1**: AI may **explain**, it may not write code for you (see below). Inline completion stays off. |
| **Part 1** | in class, Fri Nov 6, **no AI**. Anything you finish at home falls under level 1. |
| **Part 2** | at home, AI level 1 |
| **Due** | Thu Nov 12, 17:00, as a pull request |
| **Review due** | Tue Nov 17, 17:00 (author answers before the Wednesday session on Nov 18) |

## Getting started

```
git checkout main
git pull
git checkout -b ex05-<login>
```

Copy the folder `exercises/ex05` to `students/<login>/ex05` and work only in the copy.
Check your work with `uv run pytest students/<login>/ex05` and see your answers with
`uv run python students/<login>/ex05/ex05.py`.

## AI level 1: explanations, not code

From this exercise on, you may use an AI assistant at home, within limits that change from
week to week. This week:

- **Allowed:** asking it to explain a concept, an error message, or why something is slow;
  asking how problems *like this one* are usually solved; asking it to explain an example
  from the lecture.
- **Not allowed:** asking it for code for this exercise, pasting your code in for it to fix,
  or pasting the task in. Everything in your PR is code you wrote and can explain.
- **In your PR**, under **AI use**: the questions you asked (copy them, not the whole
  conversation), and in two or three sentences, in your own words, the idea you took from the
  answers. If you didn't use AI, write "none".

In class on Friday, someone may be asked to explain their PR, including the idea behind
Part 2.

## The cave

The cave is a grid of digits. Each digit is the **risk** of entering that position, from 1 to
9. You start in the **top-left** corner and want to reach the **bottom-right** one. Each move
goes one step to a neighbouring position. The risk of a path is the sum of the risks of all
the positions you **enter**; the start doesn't count, because you never enter it.

Positions are written `(row, col)`, counting from 0. `(0, 0)` is the start; in a 5 × 5 grid,
`(4, 4)` is the goal, and `grid[row][col]` is the risk at `(row, col)`.

**Example** (`EXAMPLE_TEXT` in `ex05.py`):

```
19999
19111
19191
11191
99991
```

`EXAMPLE_PATH` goes down from the start to `(3, 0)`, right to `(3, 2)`, up to `(1, 2)`, right
to `(1, 4)` and down to the goal. It enters 12 positions with risk 1 each, so its risk is 12.

`puzzle_input.py` contains `CAVE`, a 100 × 100 grid generated for this course.

## Part 1 (in class, no AI)

1. `parse_grid(text)`: turn the text of a grid into a list of rows, each a list of ints.
2. `path_risk(grid, path)`: the risk of a path given as a list of positions. Answer 2 is the
   risk of `EXAMPLE_PATH`.
3. `lowest_risk(grid, row=0, col=0)`: the lowest risk of any path from `(row, col)` to the
   goal, **moving only right or down**. Write it as a **recursive** function. If you're
   stuck: at the goal, the lowest risk is 0. Anywhere else, suppose you already knew the
   lowest risk from the position to the right and from the position below. What would the
   lowest risk from here be?

   With the example, `lowest_risk` gives 16: right and down only, there is no way round the
   9s. That's answer 1.

Answer 3 is `lowest_risk` for the whole cave. Try it. If it hasn't finished after a few
seconds, stop it with Ctrl+C: that's what Part 2 is about.

## Part 2 (at home, AI level 1)

Part 2 builds on **your own** Part 1 code.

1. **Make `lowest_risk` fast enough for the cave**: answer 3 should take well under a second.
   It must still give the same results, and the Part 1 tests must still pass.
   - First find out *how* slow it is: how often is `lowest_risk` called for a 2 × 2 grid, a
     3 × 3 grid, a 10 × 10 grid? Count it.
   - Then find out why, and how problems like this are usually made fast. This is the place
     to ask an AI to **explain**. Write the code yourself.
2. `neighbours(grid, row, col)`: the positions directly above, below, left and right of
   `(row, col)` that are inside the grid.
3. `lowest_risk_any_direction(grid)`: the lowest risk from the start to the goal, now moving
   **up, down, left or right**. With the example, that's 12, `EXAMPLE_PATH`'s risk (answer 4);
   answer 5 is the cave.
   - Why doesn't the recursive idea from Part 1 work any more, once you can move up and left?
     Try it on a 2 × 2 grid and see what happens.
   - Again, you may ask an AI to explain how this kind of search is usually done, and write
     the code yourself.
4. **Add at least two more tests of your own** at the end of `test_ex05.py`. One of them uses
   a small grid you make up, in which moving in any direction is cheaper than moving only
   right and down. Write each test case down first: which input, which expected result, and
   which case it covers.

## Your pull request

- Title: `ex05 <login>`
- Paste the output of `uv run python students/<login>/ex05/ex05.py` under **Result**.
- Under **AI use**: your questions and the idea you took from the answers (see above).
- CI must be green: all tests pass, ruff is happy.
