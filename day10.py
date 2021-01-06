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


def find_possible_next_adapter(source: int, adapters: List[int]) -> List[int]:
    allowed_adapters = [source + i for i in range(1, 4)]
    return [a for a in allowed_adapters if a in adapters]


def generate_all_paths(adapters):
    all_next = {source: find_possible_next_adapter(source, adapters) for source in adapters}
    edge_list= []
    for source, targets in all_next.items():
        for target in targets:
            edge_list.append((source, target))
    return edge_list


def get_3_diffs(data):
    data = sorted(data)
    pair = zip(data, data[1:])
    large_diffs = [small for small, big in pair if big-small == 3]
    return large_diffs


def get_length_of_paths(edge_list, source, target, three_jolt_diffs):
    G = nx.DiGraph()
    G.add_edges_from(edge_list)
    paths = []
    eval_points = [source] + three_jolt_diffs + [target]
    for temp_source, temp_target in zip(eval_points, eval_points[1:]):
        paths.append(len(list(nx.all_simple_paths(G, temp_source, temp_target) )))
    return math.prod(paths)


def answer_part1(data):
    data = add_source_and_drain(data)
    return answer_multiplier(count_jolt_differences(data))


def answer_part2(data):
    data = add_source_and_drain(data)
    edge_list = generate_all_paths(data)
    three_jolt_diffs = get_3_diffs(data)
    return get_length_of_paths(edge_list, 0, max(data), three_jolt_diffs)


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



(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 12, 15, 16, 19, (22)
