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


# Hilfsfunktionen
def change_directory(current_dir, target):
    """Change directory path to target"""
    if target == "/":
        return "/"  # root direcotry
    if target == "..":
        parent = current_dir[: current_dir.rfind("/")]
        return parent or "/"  # parent directory or root directory
    if current_dir == "/":
        return "/" + target  # go down one directory from root
    return current_dir + "/" + target  # go down one directory


def build_path(current_dir, filename):
    """Build filepath e.g. /photos/selfie.jpg"""
    if current_dir == "/":
        return "/" + filename  # file in / directory
    return current_dir + "/" + filename  # file in subdirectory


def parent_directories(path):
    """All directories which contain given file"""
    parts = path.strip("/").split("/")  # "/a/b/c.txt" -> ["a", "b", "c.txt"]
    dirs = ["/"]  # dirs starts with root directory
    current = ""
    for directory in parts[:-1]:
        current += "/" + directory  # current = "/a"
        dirs.append(current)  # ["/", "/a"]...
    return dirs


def is_inside(directory, path):
    """Return True if directory is path itself or lies inside path."""
    prefix = path.rstrip("/") + "/"  # "/a/b/c.txt"  -> "/a/b/"
    return directory == path or directory.startswith(prefix)


def is_parent(directory, path):
    """Return True if directory is a parent directory of path."""
    return directory == "/" or path.startswith(directory + "/")


def parse_transcript_old(lines):
    """Return a list of (path, size) pairs, one per file listed in the transcript.

    lines is a list of strings like EXAMPLE. Paths are full paths, e.g. "/photos/trip.jpg",
    in the order the files appear in the transcript.
    """
    files = []
    current_dir = "/"
    for line in lines:  # for every command
        if line.startswith("$ cd "):
            current_dir = change_directory(current_dir, line[5:])
        elif line[0].isdigit():  # ls command shows files starting with size
            size, filename = line.split(" ")
            files.append((build_path(current_dir, filename), int(size)))
    return files


def parse_transcript(lines):
    """Return a list of (path, size) pairs, one per file listed in the transcript.

    lines is a list of strings like EXAMPLE. Paths are full paths, e.g. "/photos/trip.jpg",
    in the order the files appear in the transcript.
    """
    files = []
    current_dir = "/"
    for line in lines:  # for every command
        if line == "":
            continue
        elif line.startswith("$ cd "):
            current_dir = change_directory(current_dir, line[5:])
        elif line[0].isdigit():  # ls command shows files starting with size
            size, filename = line.split(" ", 1)
            files.append((build_path(current_dir, filename), int(size)))
        else:
            continue
    return files


def directory_sizes(entries):
    """Return a dict mapping every directory path to the total size of all files under it.

    entries is a list of (path, size) pairs, e.g. ("/a/b/c.txt", 100). A directory's total
    size includes every file anywhere below it, however deep. The root directory is "/".
    """
    sizes = {}
    for path, size in entries:  # go through every file
        for directory in parent_directories(
            path
        ):  # sum up size for every directory (including parent directories)
            sizes[directory] = (
                sizes.get(directory, 0) + size
            )  # add 0 if directory doesn´t exist yet
    return sizes


def small_directories_total(sizes, limit=100000):
    """Return the sum of the sizes of all directories whose total size is at most `limit`."""
    return sum(size for size in sizes.values() if size <= limit)


# ---------------------------------------------------------------- Part 2 (at home)


def directory_to_delete(sizes, disk_size=50000000, needed_free=20000000):
    """Return the size of the smallest directory whose deletion frees enough space.

    The disk holds `disk_size` in total; at least `needed_free` must stay unused.
    `sizes["/"]` is the space currently used. Return None if enough space is free already.
    """
    free_space = disk_size - sizes["/"]
    space_to_free = needed_free - free_space
    if space_to_free <= 0:
        return None
    return min(size for size in sizes.values() if size >= space_to_free)


def delete_directory(sizes, path):
    """Return a new dict of directory sizes, as if the directory `path` had been deleted.

    The result is what directory_sizes would return for the files that remain.
    `sizes` itself must not change. If path isn´t included in sizes, the function returns a copy of the original sizes.
    """
    if path not in sizes:
        return sizes.copy()  # if directory to delete doesn´t exist return a copy of the original
    deleted_size = sizes[path]
    new_sizes = {}
    for directory, size in sizes.items():
        if is_inside(directory, path):
            continue
        elif is_parent(directory, path):
            new_sizes[directory] = size - deleted_size
        else:
            new_sizes[directory] = size
    return new_sizes


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
    print(parse_transcript(EXAMPLE))
    print(parse_transcript(["$ cd /", "", "$ ls", "dir photos", "100 notes.txt"]))
