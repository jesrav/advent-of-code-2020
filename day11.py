from copy import copy, deepcopy
from pathlib import Path
from typing import List, Dict

EMPTY = "L"
FLOOR = "."
OCCUPIED = "#"
State = List[List[str]]

NEIGHBORS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1), (1,0), (1,1)
]


def get_data(filename: Path) -> State:
    with open(filename, "r") as f:
        data = f.readlines()
    data = [list(s.strip()) for s in data]
    return data


def position_exists(data, row, column):
    if row < 0 or column < 0:
        return False
    elif row < len(data) and column < len(data[row]):
        return True
    else:
        return False


def is_seat_occupied(seat):
    return seat == OCCUPIED

def is_seat_empty(seat):
    return seat == EMPTY

def count_occupied_neighbors(state, row, col):
    count = 0
    for row_diff, col_diff in NEIGHBORS:
        test_row, test_col = row + row_diff, col + col_diff

        if position_exists(state, test_row, test_col) and is_seat_occupied(state[test_row][test_col]):
            count += 1
    return count


def update_cell(state, row, col):
    neighbor_count = count_occupied_neighbors(state, row, col)
    seat = state[row][col]
    if is_seat_empty(seat) and neighbor_count == 0:
        return OCCUPIED
    elif is_seat_occupied(seat) and neighbor_count >= 4:
        return EMPTY
    else:
        return seat


def update_state(state: State) -> State:
    height = len(state)
    width = len(state[0])
    new_state = deepcopy(state)
    for row in range(height):
        for col in range(width):
            new_state[row][col] = update_cell(state, row, col)
    return new_state


def check_no_changes(state, new_state):
    height = len(state)
    width = len(state[0])
    for row in range(height):
        for col in range(width):
            if new_state[row][col] != state[row][col]:
                return False
    return True


def count_occupied_seats(state):
    height = len(state)
    width = len(state[0])
    count = 0
    for row in range(height):
        for col in range(width):
            count += is_seat_occupied(state[row][col])
    return count

def update_until_no_changes(state):
    while True:
        new_state = update_state(state)
        if check_no_changes(state, new_state):
            break
        else:
            state, new_state = new_state, None
    return state

def main():
    test_data = get_data("data/day11_test.txt")
    end_data = get_data("data/day11_test_steady.txt")

    assert update_cell(test_data, 0, 3) == OCCUPIED
    assert update_state(test_data)[0][3] == OCCUPIED
    assert count_occupied_neighbors(test_data, 0, 0) == 0
    assert count_occupied_neighbors(end_data, 0, 0) == 1


    state = update_until_no_changes(test_data)

    assert check_no_changes(state, end_data)
    assert count_occupied_seats(state) == 37
    data = get_data("data/day11.txt")
    state = update_until_no_changes(data)
    print(count_occupied_seats(state))


if __name__ == "__main__":
    main()

