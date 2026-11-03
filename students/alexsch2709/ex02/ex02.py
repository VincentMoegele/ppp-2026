# # Exercise 02. See README.md for the full task.
# Replace each `pass` line with your code, ending with `return`.

from puzzle_input import PROGRAM, TARGET

# ---------------------------------------------------------------- Part 1 (in class)


def step(memory, position):
    """Execute the instruction that starts at `position` in memory.

    Opcode 1 adds, opcode 2 multiplies, opcode 99 halts (see README.md).
    Return the position of the next instruction, or None if the opcode is 99.
    All other opcodes will be ignored as well as the 3 following operators to ensure that the program can run smoothly.
    """

    instruction = memory[position]

    if instruction == 1:
        # add
        pos1 = memory[position + 1]
        pos2 = memory[position + 2]
        val1 = memory[pos1]
        val2 = memory[pos2]

        memory[memory[position + 3]] = val1 + val2

        return position + 4

    elif instruction == 2:
        # multiply
        pos1 = memory[position + 1]
        pos2 = memory[position + 2]
        val1 = memory[pos1]
        val2 = memory[pos2]

        memory[memory[position + 3]] = val1 * val2

        return position + 4

    elif instruction == 99:
        return None
    else:
        return position + 4


def run(memory):
    """Execute instructions, starting at position 0, until the program halts.

    Return the value at position 0 after the program has halted.
    """
    pos = 0
    while True:
        zwischen = step(memory, pos)
        if zwischen is not None:
            pos = zwischen
        if zwischen is None or zwischen >= len(memory):
            return memory[0]


# ---------------------------------------------------------------- Part 2 (at home)


def run_with(program, noun, verb):
    """Return the result of program with noun at position 1 and verb at position 2."""

    copy = program.copy()

    copy[1] = noun
    copy[2] = verb
    return run(copy)


def find_noun_verb(program, target):
    """Return (noun, verb), each from 0 to 99, for which run_with gives target.

    Return None if there is no such pair.
    """

    for i in range(0, 100):
        for j in range(0, 100):
            if run_with(program, i, j) == target:
                return (i, j)

    return None


# ---------------------------------------------------------------- Answers

if __name__ == "__main__":
    print("Part 1")
    print("1:", run([2, 9, 10, 9, 1, 9, 11, 0, 99, 6, 7, 3]))
    print("2:", run(list(PROGRAM)))

    print("Part 2")
    print("3:", run_with(list(PROGRAM), 0, 0))
    print("4:", find_noun_verb(list(PROGRAM), TARGET))
