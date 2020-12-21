from pathlib import Path
from typing import List
from functools import reduce

import numpy as np


def get_data(filename: Path) -> List[str]:
    with open(filename, "r") as f:
        data = f.readlines()
    return [s.rstrip() for s in data]


def coordinate_string_to_is_tree_list(s: str) -> List[int]:
    return [True if el == "#" else False for el in s]


def parse_input(input_list: List[str]) -> List[List[int]]:
    return [coordinate_string_to_is_tree_list(s) for s in input_list]


def position_is_tree(row_list, position) -> bool:
    row_multiplier = int(np.ceil(position / (len(row_list) - 1)))
    if row_multiplier > 0:
        row_list = row_multiplier * row_list
    return row_list[position]


def get_positions(
    start_position: np.array, step_vector: np.array, n_rows: int
) -> List[np.array]:
    position = start_position
    positions = [start_position]
    while position[0] + step_vector[0] < n_rows:
        position = position + step_vector
        positions.append(position)

    return positions


def get_tree_sum(positions, parsed_input):
    tree_sum = 0
    for position in positions:
        tree_sum += 1 * position_is_tree(parsed_input[position[0]], position[1])
    return tree_sum


def get_answer_part_1(parsed_input, step_vector):
    positions = get_positions(
        start_position=np.array([0, 0]),
        step_vector=step_vector,
        n_rows=len(parsed_input),
    )
    return get_tree_sum(positions, parsed_input)


def get_answer_part_2(parsed_input, step_vectors):
    tree_counts = [
        get_answer_part_1(parsed_input, step_vector) for step_vector in step_vectors
    ]
    return reduce(lambda x, y: x * y, tree_counts)


def main():
    INPUT_PATH = Path("data/day3.txt")
    input = get_data(INPUT_PATH)
    step_vector_part_1 = np.array([1, 3])
    step_vectors_part_2 = [
        [1, 1],
        [1, 3],
        [1, 5],
        [1, 7],
        [2, 1],
    ]

    parsed_input = parse_input(input)
    print(f"Answer 1: {get_answer_part_1(parsed_input, step_vector_part_1)}")
    print(f"Answer 1: {get_answer_part_2(parsed_input, step_vectors_part_2)}")


##################################################################
# Test
##################################################################
test_input = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]
step_vector_part_1 = np.array([1, 3])
step_vectors_part_2 = [
    [1, 1],
    [1, 3],
    [1, 5],
    [1, 7],
    [2, 1],
]
parsed_test_input = parse_input(test_input)

assert get_answer_part_1(parsed_test_input, step_vector_part_1) == 7
assert get_answer_part_2(parsed_test_input, step_vectors_part_2) == 336


if __name__ == "__main__":
    main()
