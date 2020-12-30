from pathlib import Path
from typing import List
from itertools import combinations


def get_data(filename: Path) -> List[int]:
    with open(filename, "r") as f:
        data = f.readlines()
    data = [int(s.strip()) for s in data]
    return data


def has_sum_in_previous_n(index: int, data: List[int], n: int) -> bool:
    number = data[index]
    previous_n = data[index-n:index]
    relevant_previous_n = [el for el in previous_n if el < number]
    sums = [sum(combi) for combi in combinations(relevant_previous_n, 2)]
    return number in sums


def get_part1_index(data: List[int], n: int) -> int:
    number_has_sum_in_previous_n = [
        has_sum_in_previous_n(index, data, n) for index, number in enumerate(data)
    ]
    number_has_sum_in_previous_n = number_has_sum_in_previous_n[n:]
    return n + number_has_sum_in_previous_n.index(False)


def get_bordering_combis(data: List[int], n: int) -> List[List[int]]:
    possible_combinations = [
        data[i:i+n] for i in range(len(data) - n + 1)
    ]
    return possible_combinations


def get_part2_combination(data: List[int], value) -> int:

    for n in range(2,len(data)):
        combis = get_bordering_combis(data, n)
        match_combis = [c for c in combis if value == sum(c)]
        if len(match_combis) == 1:
            return match_combis[0]
        elif len(match_combis) > 1:
            raise ValueError("There should only be one match, something is wrong")
        else:
            continue


def main():
    INPUT_PATH = Path("data/day9.txt")
    data = get_data(INPUT_PATH)
    answer_part1 = data[get_part1_index(data, 25)]
    print(f"Answer part 1: {answer_part1}")
    part_2_combination = get_part2_combination(
        data, answer_part1,
    )
    answer_part2 = min(part_2_combination) + max(part_2_combination)
    print(f"Answer part 2: {answer_part2}")


##################################################################
# Tests
##################################################################
# Part 1
TEST_INPUT_PATH = Path("data/day9_test_part1.txt")
test_input = get_data(TEST_INPUT_PATH)
assert test_input[get_part1_index(test_input, 5)] == 127
assert get_part2_combination(test_input, 127) == [15, 25, 47, 40]


if __name__ == "__main__":
    main()
