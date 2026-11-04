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
    abs_path = "/"
    file_tuples = []
    for line in lines:
        if line.startswith("$ cd "):
            if line == "$ cd /":
                abs_path = "/"
            elif line == "$ cd ..":
                abs_path = abs_path[0 : abs_path[0:-1].rfind("/") + 1]
            else:
                # cd into any directory
                abs_path = abs_path + line[5:] + "/"
        elif not (line.startswith("dir") or line.startswith("$ ls")):  # must be file
            full_file_path = (
                f"{abs_path}{line.split(' ')[1]}"  # 'dir' is always followed by the filename
            )
            file_tuples.append((full_file_path, int(line.split(" ")[0])))
    return file_tuples


def directory_sizes(entries):
    """Return a dict mapping every directory path to the total size of all files under it.

    entries is a list of (path, size) pairs, e.g. ("/a/b/c.txt", 100). A directory's total
    size includes every file anywhere below it, however deep. The root directory is "/".
    """
    folder_size_dict = {}
    for file, size in entries:
        current_path = file[0 : file.rfind("/") + 1]
        if current_path != "/":
            current_path = current_path[:-1]

        folder_size_dict[current_path] = folder_size_dict.get(current_path, 0) + size

        while current_path != "/":
            current_path = current_path[0 : current_path[0:-1].rfind("/") + 1]
            if current_path != "/":
                current_path = current_path[:-1]
            folder_size_dict[current_path] = folder_size_dict.get(current_path, 0) + size

    return folder_size_dict


def small_directories_total(sizes, limit=100000):
    """Return the sum of the sizes of all directories whose total size is at most `limit`."""
    return sum(v for k, v in sizes.items() if v <= limit)


# ---------------------------------------------------------------- Part 2 (at home)


def directory_to_delete(sizes, disk_size=50000000, needed_free=20000000):
    """Return the size of the smallest directory whose deletion frees enough space.

    The disk holds `disk_size` in total; at least `needed_free` must stay unused.
    `sizes["/"]` is the space currently used. Return None if enough space is free already.
    """
    required_space = needed_free - (disk_size - sizes["/"])
    if required_space < 0:
        return None

    smallest_key = "/"
    for k, v in sizes.items():
        if v >= required_space and sizes[k] < sizes[smallest_key]:
            smallest_key = k
    return sizes[smallest_key]


def delete_directory(sizes, path):
    """Return a new dict of directory sizes, as if the directory `path` had been deleted.

    The result is what directory_sizes would return for the files that remain.
    `sizes` itself must not change.

    If `path` is not a directory in sizes, returns a copy of `sizes` unchanged.
    """

    prefix = path if path.endswith("/") else path + "/"

    sizes_copy = {
        current_path: size
        for current_path, size in sizes.items()
        if current_path != path and not current_path.startswith(prefix)
    }

    if sizes_copy == sizes:
        return sizes_copy

    target = path
    target_size = sizes[target]

    while target != "/":
        target = target[0 : target[0:-1].rfind("/") + 1]
        if target != "/":
            sizes_copy[target[0:-1]] = sizes_copy[target[0:-1]] - target_size
        else:
            sizes_copy[target] = sizes_copy[target] - target_size

    return sizes_copy


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
