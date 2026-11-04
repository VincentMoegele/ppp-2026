# Exercise 03: how big is this folder?

|  |  |
|---|---|
| **AI level** | **0**: no AI, and inline completion stays off |
| **Part 1** | in class, Fri Oct 16 |
| **Part 2** | at home |
| **Due** | Thu Oct 22, 17:00, as a pull request |
| **Review due** | Tue Oct 27, 17:00 (author answers before the Wednesday session on Nov 4) |

## Getting started

```
git checkout main
git pull
git checkout -b ex03-<login>
```

Copy the folder `exercises/ex03` to `students/<login>/ex03` and work only in the copy.
Check your work with `uv run pytest students/<login>/ex03` and see your answers with
`uv run python students/<login>/ex03/ex03.py`.

## The input

Someone explored a hard drive in a terminal and saved what they typed and what came back.
Lines starting with `$` are commands:

- `$ cd /` goes to the **root** directory, `/`.
- `$ cd photos` goes into the directory `photos` inside the current one.
- `$ cd ..` goes back up one level, to the directory that contains the current one.
- `$ ls` lists the current directory. The lines after it, up to the next `$`, are its
  contents: `dir summer` is a directory, `4000 trip.jpg` is a file of 4000 bytes.

A directory's **total size** is the size of every file anywhere underneath it, however deep.
Every file is at least 1 byte.

**Example** (`EXAMPLE` in `ex03.py`):

```
$ cd /
$ ls
dir photos
100 notes.txt
dir music
$ cd photos
$ ls
4000 trip.jpg
dir summer
$ cd summer
$ ls
2500 beach.jpg
1500 sunset.jpg
$ cd ..
$ cd ..
$ cd music
$ ls
3000 song.mp3
```

The files, with their full paths:

```python
[
    ("/notes.txt", 100),
    ("/photos/trip.jpg", 4000),
    ("/photos/summer/beach.jpg", 2500),
    ("/photos/summer/sunset.jpg", 1500),
    ("/music/song.mp3", 3000),
]
```

| Directory | Total size | Why |
|---|---|---|
| `/` | 11100 | every file |
| `/photos` | 8000 | `trip.jpg` + `beach.jpg` + `sunset.jpg` |
| `/photos/summer` | 4000 | `beach.jpg` + `sunset.jpg` |
| `/music` | 3000 | `song.mp3` |

`puzzle_input.py` contains a much longer transcript, `TRANSCRIPT`, generated for this course.

## Part 1 (in class)

1. `parse_transcript(lines)`: return the list of `(path, size)` pairs for all files in the
   transcript, in the order they appear, like the list above.

2. `directory_sizes(entries)`: return a dict mapping every directory path to its total size.

3. `small_directories_total(sizes, limit=100000)`: given the dict from `directory_sizes`,
   return the sum of the sizes of all directories whose total size is **at most** `limit`.
   With the example and `limit=5000`, that's `/photos/summer` (4000) and `/music` (3000):
   `7000`.

Answer 1 uses the example (with `limit=5000`); answer 2 uses `TRANSCRIPT`, with the default
`limit`.

## Part 2 (at home)

Part 2 builds on **your own** Part 1 code.

1. `directory_to_delete(sizes, disk_size=50000000, needed_free=20000000)`: the disk holds
   `disk_size` in total, and at least `needed_free` must stay unused. `sizes["/"]` is the
   space currently used. Find the **smallest** directory whose deletion frees enough space,
   and return its size, or `None` if enough space is free already.

2. `delete_directory(sizes, path)`: return a **new** dict of directory sizes, as if the
   directory `path` and everything in it had been deleted. The result must be exactly what
   `directory_sizes` would return for the files that remain. With the example, deleting
   `/photos/summer` gives `{"/": 7100, "/photos": 4000, "/music": 3000}`.

   **`sizes` itself must not change.**

3. What does your `delete_directory` do if `path` is not in `sizes`? Decide what it
   *should* do, write that into its description (the text in triple quotes), and add a test
   for it.

4. **Add at least two more tests of your own** at the end of `test_ex03.py`, one of them
   checking that `sizes` doesn't change. Write each test case down first: which input, which
   expected result, and which case it covers.

## Your pull request

- Title: `ex03 <login>`
- Paste the output of `uv run python students/<login>/ex03/ex03.py` under **Result**.
- CI must be green: all tests pass, ruff is happy.
