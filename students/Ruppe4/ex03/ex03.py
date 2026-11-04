# Exercise 03. See README.md for the full task.
# Replace each `pass` line with your code, ending with `return`.

from puzzle_input import TRANSCRIPT

EXAMPLE = [
    "$ cd /",
    "$ ls",
    "dir photos",
    "100 notes.txt",
    "dir music",
    "$ cd photos",
    "$ ls",
    "4000 trip.jpg",
    "dir summer",
    "$ cd summer",
    "$ ls",
    "2500 beach.jpg",
    "1500 sunset.jpg",
    "$ cd ..",
    "$ cd ..",
    "$ cd music",
    "$ ls",
    "3000 song.mp3",
]

# ---------------------------------------------------------------- Part 1 (in class)


def parse_transcript(lines):
    """Return a list of (path, size) pairs, one per file listed in the transcript.

    lines is a list of strings like EXAMPLE. Paths are full paths, e.g. "/photos/trip.jpg",
    in the order the files appear in the transcript.
    """
    cwd = []
    files = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if parts[0] == "$":
            if parts[1] == "cd":
                target = parts[2]
                if target == "/":
                    cwd = []
                elif target == "..":
                    if cwd:
                        cwd.pop()
                else:
                    cwd.append(target)

        elif parts[0] == "dir":
            continue
        else:
            size, name = int(parts[0]), parts[1]
            files.append(("/" + "/".join(cwd + [name]), size))
    return files


def _ancestors(file_path):
    """'/a/b/f.txt' -> ['/', '/a', '/a/b']"""
    parts = file_path.split("/")[1:-1]
    result = ["/"]
    for i in range(1, len(parts) + 1):
        result.append("/" + "/".join(parts[:i]))
    return result


def directory_sizes(entries):
    """Return a dict mapping every directory path to the total size of all files under it.

    entries is a list of (path, size) pairs, e.g. ("/a/b/c.txt", 100). A directory's total
    size includes every file anywhere below it, however deep. The root directory is "/".
    """
    sizes = {"/": 0}
    for path, size in entries:
        for d in _ancestors(path):
            sizes[d] = sizes.get(d, 0) + size
    return sizes


def small_directories_total(sizes, limit=100000):
    """Return the sum of the sizes of all directories whose total size is at most `limit`."""
    return sum(s for s in sizes.values() if s <= limit)


# ---------------------------------------------------------------- Part 2 (at home)


def directory_to_delete(sizes, disk_size=50000000, needed_free=20000000):
    """Return the size of the smallest directory whose deletion frees enough space.

    The disk holds `disk_size` in total; at least `needed_free` must stay unused.
    `sizes["/"]` is the space currently used. Return None if enough space is free already.
    """
    free = disk_size - sizes["/"]
    if free >= needed_free:
        return None
    missing = needed_free - free
    candidates = [s for s in sizes.values() if s >= missing]
    if not candidates:
        raise ValueError(f"no directory is large enough to free {missing} bytes")
    return min(candidates)


def delete_directory(sizes, path):
    """Return a new dict of directory sizes, as if the directory `path` had been deleted.

    The result is what directory_sizes would return for the files that remain.
    `sizes` itself must not change.
    """
    if path not in sizes:
        raise KeyError(f"unknown directory: {path}")
    removed = sizes[path]
    result = {}
    for d, s in sizes.items():
        if path == "/":
            result = {"/": 0}
            break
        if d == path or d.startswith(path + "/"):
            continue
        if path.startswith(d + "/") or d == "/":
            s -= removed

            if s == 0 and d != "/":
                continue

        result[d] = s
    return result


# ---------------------------------------------------------------- Answers

if __name__ == "__main__":
    print("Part 1")
    example_sizes = directory_sizes(parse_transcript(EXAMPLE))
    print("1:", small_directories_total(example_sizes, limit=5000))
    sizes = directory_sizes(parse_transcript(TRANSCRIPT))
    print("2:", small_directories_total(sizes))

    print("Part 2")
    print("3:", directory_to_delete(sizes))
    print("4:", small_directories_total(delete_directory(sizes, "/home/backup")))
    print("2 again:", small_directories_total(sizes))
