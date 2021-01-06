from pathlib import Path
from typing import List, Dict
from collections import Counter


def get_data(filename: Path) -> List[int]:
    with open(filename, "r") as f:
        data = f.readlines()
    data = [int(s.strip()) for s in data]
    return data


def add_source_and_drain(data: List[int]) -> List[int]:
    return data + [0, max(data) + 3]


def count_jolt_differences(data: List[int]) -> Counter:
    data = sorted(data)
    pair = zip(data, data[1:])
    diffs = [big-small for small, big in pair]
    counter = Counter(diffs)
    return counter


def answer_multiplier(diff_counts):
    return diff_counts[1] * diff_counts[3]


def main():
    input_path = Path("data/day10.txt")
    data = get_data(input_path)
    answer_part1 = answer_multiplier(count_jolt_differences(add_source_and_drain(data)))
    print(f"Answer part 1: {answer_part1}")
    answer_part2 = None
    print(f"Answer part 2: {answer_part2}")


##################################################################
# Tests
##################################################################
# Part 1
TEST_INPUT_PATH = Path("data/day10_test.txt")
test_input = get_data(TEST_INPUT_PATH)
assert answer_multiplier(count_jolt_differences(add_source_and_drain(test_input))) == 5*7

TEST_INPUT_PATH = Path("data/day10_test2.txt")
test_input = get_data(TEST_INPUT_PATH)
assert answer_multiplier(count_jolt_differences(add_source_and_drain(test_input))) == 22*10

if __name__ == "__main__":
    main()
