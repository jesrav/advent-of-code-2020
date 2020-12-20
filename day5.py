from pathlib import Path
from typing import List

import numpy as np

def get_data(filename: Path) -> List[str]:
    with open(filename, "r") as f:
        data = f.readlines()
    data = [row.strip() for row in data]
    return data


def binary_partition(ordered_list, in_higher_partition_list):
    remaining = ordered_list
    for in_higher_partition in in_higher_partition_list:
        if in_higher_partition:
            remaining = np.array_split(remaining, 2)[1]
        else:
            remaining = np.array_split(remaining, 2)[0]
    return remaining[0]


def get_front_back_partitioning_list(s: str) -> List[bool]:
    return [c == 'B' for c in s[:7]]


def get_right_left_partitioning_list(s: str) -> List[bool]:
    return [c == 'R' for c in s[7:]]


def get_seat_id(boardingpass: str) -> int:
    row_list = list(range(128))
    col_list = list(range(8))
    front_back_partitioning_list = get_front_back_partitioning_list(boardingpass)
    right_left_partitioning_list = get_right_left_partitioning_list(boardingpass)
    row_number = binary_partition(row_list, front_back_partitioning_list)
    col_number = binary_partition(col_list, right_left_partitioning_list)
    return 8*row_number + col_number


def get_max_seat_id(boardingpasses: List[str]) -> int:
    return max([get_seat_id(b) for b in boardingpasses])


def main():
    INPUT_PATH = Path("data/day5.txt")
    input = get_data(INPUT_PATH)
    print(f"Answer part 1: {get_max_seat_id(input)}")

##################################################################
# Tests
##################################################################
assert get_seat_id("BFFFBBFRRR") == 567
assert get_seat_id("FFFBBBFRRR") == 119
assert get_seat_id("BBFFBBFRLL") == 820

if __name__ == "__main__":
    main()
