from ex03 import (
    EXAMPLE,
    delete_directory,
    directory_sizes,
    directory_to_delete,
    parse_transcript,
    small_directories_total,
)

EXAMPLE_ENTRIES = [
    ("/notes.txt", 100),
    ("/photos/trip.jpg", 4000),
    ("/photos/summer/beach.jpg", 2500),
    ("/photos/summer/sunset.jpg", 1500),
    ("/music/song.mp3", 3000),
]

# ---------------------------------------------------------------- Part 1


def test_parse_transcript_example():
    assert parse_transcript(EXAMPLE) == EXAMPLE_ENTRIES


def test_parse_transcript_cd_root():
    lines = ["$ cd /", "$ cd a", "$ cd b", "$ cd /", "$ cd c", "$ ls", "5 x.txt"]
    assert parse_transcript(lines) == [("/c/x.txt", 5)]


def test_directory_sizes_root():
    sizes = directory_sizes(EXAMPLE_ENTRIES)
    assert sizes["/"] == 11100


def test_directory_sizes_nested():
    sizes = directory_sizes(EXAMPLE_ENTRIES)
    assert sizes["/photos"] == 8000
    assert sizes["/photos/summer"] == 4000


def test_small_directories_total():
    sizes = directory_sizes(EXAMPLE_ENTRIES)
    assert small_directories_total(sizes, limit=5000) == 7000


# ---------------------------------------------------------------- Part 2
# Add at least two tests of your own below, for the Part 2 functions.
# One of them must check that delete_directory does not change `sizes`.


def test_directory_to_delete():
    sizes = directory_sizes(EXAMPLE_ENTRIES)
    assert directory_to_delete(sizes, disk_size=13000, needed_free=5400) == 4000


def test_delete_directory():
    sizes = directory_sizes(EXAMPLE_ENTRIES)
    assert delete_directory(sizes, "/photos/summer") == {
        "/": 7100,
        "/photos": 4000,
        "/music": 3000,
    }


def test_delete_directory_false_path():
    sizes = directory_sizes(EXAMPLE_ENTRIES)
    assert delete_directory(sizes, "/photos/swummer") == {
        "/": 11100,
        "/music": 3000,
        "/photos": 8000,
        "/photos/summer": 4000,
    }


def test_delete_parent_directory():
    sizes = directory_sizes(EXAMPLE_ENTRIES)
    assert delete_directory(sizes, "/photos") == {
        "/": 3100,
        "/music": 3000,
    }

def test_parse_transcript_empty_list():
    assert parse_transcript([]) == []

def test_directory_to_delete_enough_space():
    sizes = directory_sizes(EXAMPLE_ENTRIES)
    assert directory_to_delete(sizes, 500000000,10) == None