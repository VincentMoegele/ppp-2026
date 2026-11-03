# Exercise 02: a tiny computer

|  |  |
|---|---|
| **AI level** | **0**: no AI, and inline completion stays off |
| **Part 1** | in class, Fri Oct 9 |
| **Part 2** | at home |
| **Due** | Thu Oct 15, 17:00, as a pull request |
| **Review due** | Tue Oct 20, 17:00 (author answers before the Wednesday session) |

## Getting started

```
git checkout main
git pull
git checkout -b ex02-<login>
```

Copy the folder `exercises/ex02` to `students/<login>/ex02` and work only in the copy.
Check your work with `uv run pytest students/<login>/ex02` and see your answers with
`uv run python students/<login>/ex02/ex02.py`.

## The computer

On the first day we saw that a computer's memory holds numbers, and that some of them are the
program. In this exercise you build such a computer. Its memory is a Python list of integers,
and a **position** is an index into that list.

The computer starts at position 0. The number there is an **opcode**, which says what to do:

- **1: add.** The three numbers after the opcode are positions. Read the values at the first
  two positions, add them, and write the sum to the third position.
- **2: multiply.** The same, but multiply instead of adding.
- **99: halt.** The program is finished.

After a 1 or a 2, the computer moves forward 4 positions (the opcode and its three numbers)
to the next instruction.

Note the difference between a position and the value stored there. In `[1, 5, 6, 0, ...]` the
instruction does **not** add 5 and 6; it adds the values at positions 5 and 6.

**An example, step by step.** Memory: `[1, 5, 6, 0, 99, 20, 22]`

| Position | Opcode | What happens | Memory afterwards |
|---|---|---|---|
| 0 | 1 | value at 5 (20) + value at 6 (22) = 42, written to position 0 | `[42, 5, 6, 0, 99, 20, 22]` |
| 4 | 99 | halt | |

The result of a program is the value at position 0 after it has halted: here, 42.

Instructions can write anywhere in memory, including over other instructions. The computer
doesn't care: it always reads the opcode that is there when it gets to it.

## Part 1 (in class)

1. `step(memory, position)`: execute the one instruction that starts at `position`. It changes
   `memory` and returns the position of the next instruction, or `None` if the opcode is 99.
   Trace the tests in `test_ex02.py` by hand before you start: what should memory look like
   afterwards?
2. `run(memory)`: start at position 0, call `step` until the program halts, and return the
   value at position 0. Use your `step`.

`puzzle_input.py` contains a longer program, `PROGRAM`. Answer 2 is its result.

## Part 2 (at home)

Part 2 builds on **your own** Part 1 code.

The numbers at positions 1 and 2 are the program's inputs; we call them the **noun** and the
**verb**.

1. `run_with(program, noun, verb)`: put the noun at position 1 and the verb at position 2, run
   the program, and return its result. Use your `run`.
2. `find_noun_verb(program, target)`: which noun and verb (each from 0 to 99) make the program
   produce `target`? Return them as a pair `(noun, verb)`, or `None` if there is none.
3. What does your `step` do if the opcode is not 1, 2 or 99? Decide what it *should* do,
   write that into its description (the text in triple quotes), and add a test for it.
4. **Add at least two more tests of your own** at the end of `test_ex02.py`. Write each test
   case down first: which input, which expected result, and what case it covers.

## Your pull request

- Title: `ex02 <login>`
- Paste the output of `uv run python students/<login>/ex02/ex02.py` under **Result**.
- CI must be green: all tests pass, ruff is happy.
