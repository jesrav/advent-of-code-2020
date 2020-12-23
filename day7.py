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


def count_bags(bag_dict, start_bags, start_count):
    if all([bool(bag_dict[start_bag]) is False for start_bag in start_bags]):
        return start_count
    else:
        next_level_bags = [
            int(count)*[bag] for start_bag in start_bags for bag, count in bag_dict[start_bag].items()
        ]
        next_level_bags_flat = [item for sublist in next_level_bags for item in sublist]
        count = sum([int(val) for start_bag in start_bags for val in bag_dict[start_bag].values()]) + start_count
        return count_bags(bag_dict, next_level_bags_flat, start_count=count)


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
    answer_part_2 = count_bags(bag_dict, ["shiny gold bag"], 0)
    print(f"Answer part 1: {answer_part_1}")
    print(f"Answer part 2: {answer_part_2}")


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
assert count_bags(test_bag_dict, ["shiny gold bag"], 0) == 32

if __name__ == "__main__":
    main()
