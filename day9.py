from pathlib import Path
from typing import List
from itertools import combinations


def get_data(filename: Path) -> List[str]:
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


def get_answer_part1(data: List[int], n: int):
    number_has_sum_in_previous_n = [
        has_sum_in_previous_n(index, data, n) for index, number in enumerate(data)
    ]
    number_has_sum_in_previous_n = number_has_sum_in_previous_n[n:]
    return data[n + number_has_sum_in_previous_n.index(False)]


def main():
    INPUT_PATH = Path("data/day9.txt")
    data = get_data(INPUT_PATH)
    print(f"Answer part 1: {get_answer_part1(data, 25)}")


##################################################################
# Tests
##################################################################
# Part 1
TEST_INPUT_PATH = Path("data/day9_test_part1.txt")
test_input = get_data(TEST_INPUT_PATH)
assert get_answer_part1(test_input, 5) == 127


if __name__ == "__main__":
    main()
