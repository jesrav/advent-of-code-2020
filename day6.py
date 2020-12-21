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
        list(group) for k, group in groupby(parsed_input, lambda x: x == "") if not k
    ]
    return parsed_input


def get_yes_count_for_group_part_1(group_input: List[str]) -> int:
    character_list = [c for s in group_input for c in s]
    return len(set(character_list))


def get_yes_count_for_group(group_input: List[str], version: str) -> int:
    individual_character_sets = [set(s) for s in group_input]
    if version == "part1":
        set_of_yes_anwers = set.union(*individual_character_sets)
    elif version == "part2":
        set_of_yes_anwers = set.intersection(*individual_character_sets)
    else:
        raise ValueError("version must be 'part1' or 'part2")
    return len(set_of_yes_anwers)


def main():
    INPUT_PATH = Path("data/day6.txt")
    input = get_data(INPUT_PATH)
    parsed_input = parse_input(input)
    answer_part_1 = sum([get_yes_count_for_group(g, "part1") for g in parsed_input])
    answer_part_2 = sum([get_yes_count_for_group(g, "part2") for g in parsed_input])
    print(f"Answer part 1: {answer_part_1}")
    print(f"Answer part 2: {answer_part_2}")


##################################################################
# Tests
##################################################################
TEST_INPUT_PATH = Path("data/day6_test_part1.txt")
test_input = get_data(TEST_INPUT_PATH)
test_parsed_input = parse_input(test_input)
test_answer_part_1 = sum(
    [get_yes_count_for_group(g, "part1") for g in test_parsed_input]
)
assert test_answer_part_1 == 11
test_answer_part_2 = sum(
    [get_yes_count_for_group(g, "part2") for g in test_parsed_input]
)
assert test_answer_part_2 == 6


if __name__ == "__main__":
    main()
