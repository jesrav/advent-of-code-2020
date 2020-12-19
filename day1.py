from pathlib import Path
from typing import List, Tuple
import itertools
from functools import reduce


def get_data(filename: Path) -> List[int]:
    with open(filename, "r") as f:
        data = f.readlines()
    return [int(el) for el in data]


def sums_to_2020(n_let) -> bool:
    return sum(n_let) == 2020


def get_all_n_lets_generator(integer_list: List[int], n: int):
    return itertools.combinations(integer_list, n)


def get_n_let_summing_to_2020(integer_list: List[int], n) -> Tuple[int, int]:
    for nlet in get_all_n_lets_generator(integer_list, n):
        if sums_to_2020(nlet):
            return nlet


def get_answer(integer_list: List[int], n):
    n_let = get_n_let_summing_to_2020(integer_list, n)
    return reduce(lambda x, y: x*y, n_let)


def main():
    INPUT_PATH = "data/day1.txt"
    input_list = get_data(INPUT_PATH)
    print(f"Result part 1: {get_answer(input_list, 2)}")
    print(f"Result part 2: {get_answer(input_list, 3)}")


##################################################################
# Test
##################################################################
test_input = [
    1721,
    979,
    366,
    299,
    675,
    1456,
 ]
assert get_answer(test_input, 2) == 514579
assert get_answer(test_input, 3) == 241861950

if __name__ == "__main__":
    main()

