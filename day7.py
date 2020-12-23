from pathlib import Path
from typing import List, Dict
from functools import reduce


def get_data(filename: Path) -> List[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    return data


def stem_bag(bag_string: str) -> str:
    if bag_string.endswith("s"):
        return bag_string[:-1]
    elif bag_string.endswith("s."):
        return bag_string[:-2]
    elif bag_string.endswith("."):
        return bag_string[:-1]
    else:
        return bag_string


def parse_input_string(input: str) -> Dict:
    inner_outer_bag_split = input.strip().split(" contain ")
    outer_bag = stem_bag(inner_outer_bag_split[0])
    inner_bags_string = inner_outer_bag_split[1]
    inner_bags_string_list = inner_bags_string.split(", ")
    inner_bags_dict = {
        stem_bag(" ".join(s.split(" ")[1:])): s.split(" ")[0]
        for s in inner_bags_string_list
    }
    if inner_bags_dict == {"other bag": "no"}:
        inner_bags_dict = {}
    return {outer_bag: inner_bags_dict}


def parse_inputs(input: List[str]) -> Dict:
    return reduce(lambda x, y: {**x, **y}, [parse_input_string(s) for s in input])


def does_bags_contain_bag(bag_dict, start_bags, needed_bag):
    if all([bool(bag_dict[start_bag]) is False for start_bag in start_bags]):
        return False
    elif any([needed_bag in bag_dict[start_bag].keys() for start_bag in start_bags]):
        return True
    else:
        next_level_bags = [
            bag for start_bag in start_bags for bag in bag_dict[start_bag].keys()
        ]
        return does_bags_contain_bag(bag_dict, next_level_bags, needed_bag)


def main():
    INPUT_PATH = Path("data/day7.txt")
    input = get_data(INPUT_PATH)
    bag_dict = parse_inputs(input)
    answer_part_1 = sum(
        [
            does_bags_contain_bag(bag_dict, [start_bag], "shiny gold bag")
            for start_bag in bag_dict.keys()
        ]
    )
    print(f"Answer part 1: {answer_part_1}")


##################################################################
# Tests
##################################################################
TEST_INPUT_PATH = Path("data/day7_test_part1.txt")
test_input = get_data(TEST_INPUT_PATH)
test_bag_dict = parse_inputs(test_input)
assert (
    sum(
        [
            does_bags_contain_bag(test_bag_dict, [start_bag], "shiny gold bag")
            for start_bag in test_bag_dict.keys()
        ]
    )
    == 4
)


if __name__ == "__main__":
    main()
