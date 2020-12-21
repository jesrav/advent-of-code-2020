from pathlib import Path
from typing import List
from itertools import groupby


def get_data(filename: Path) -> List[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    return data


def parse_input(input: str) -> List[List[str]]:
    parsed_input = [s.strip("\n") for s in input]
    parsed_input = [
        list(group) for k, group in groupby(parsed_input, lambda x: x == "")
        if not k
    ]
    return parsed_input


def get_yes_count_for_group(group_input: List[str]) -> int:
    character_list = [c for s in group_input for c in s]
    return len(set(character_list))


def get_answer_part_1(input_parsed):
    return sum([get_yes_count_for_group(g) for g in input_parsed])


def main():
    INPUT_PATH = Path("data/day6.txt")
    input = get_data(INPUT_PATH)
    parsed_input = parse_input(input)
    print(f"Answer part 1: {get_answer_part_1(parsed_input)}")


##################################################################
# Tests
##################################################################
TEST_INPUT_PATH = Path("data/day6_test_part1.txt")
test_input = get_data(TEST_INPUT_PATH)
test_parsed_input = parse_input(test_input)
assert get_answer_part_1(test_parsed_input) == 11


if __name__ == "__main__":
    main()
