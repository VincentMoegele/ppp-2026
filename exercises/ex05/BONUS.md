# Exercise 05, bonus: shields

For anyone who wants more. It's **optional**: your PR counts without it. AI level 1, like the
rest of Part 2: explanations yes, code no. Do Part 2 first; the bonus builds on your
`lowest_risk_any_direction`.

## The task

You now carry a number of **shields**. Entering a position with a shield costs 0 instead of
its risk. Each shield works for one position only, and you decide where to use them. Moves
still go up, down, left or right, and the start still doesn't count.

`lowest_risk_with_shields(grid, shields)` in your `ex05.py`: the lowest risk from the start to
the goal with `shields` shields. With 0 shields, that's the same as
`lowest_risk_any_direction`. Leave your Part 1 and 2 functions as they are, so their tests
still pass.

Add two lines at the end of your `ex05.py`:

```python
    print("6:", lowest_risk_with_shields(example, 1))
    print("7:", lowest_risk_with_shields(cave, 3))
```

With the example and 1 shield, the answer is 7.

## Before you write code

Work out the example with 1 shield by hand. The best path from Part 2 has risk 12, and every
position on it has risk 1, so a shield on that path gives 11. Why is the answer 7? Which path
is it, and what does that tell you about your search from Part 2? In your PR, explain in two
or three sentences what your search has to keep track of now, and why.

## Tests

Copy `test_ex05_bonus.py` into your `students/<login>/ex05` folder (you copied the folder
before it existed). Its tests are skipped until your `ex05.py` has a `lowest_risk_with_shields`.
Add at least one test of your own: a small grid where the best path with a shield is not the
best path without one.

If you do the bonus, say so in your PR description, so your reviewer knows to look at it.
