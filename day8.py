from pathlib import Path
from typing import List, Dict

accumulator = 0


def get_data(filename: Path) -> List[str]:
    with open(filename, "r") as f:
        data = f.readlines()

    return data


class BootCode:

    def __init__(self, actions_dict: Dict):
        self.actions_dict = actions_dict
        self.accumulator = 0
        self.row = 1
        self.rows_visited = []

    def take_action(self, action_type: str, action_input: int) -> int:
        if action_type == 'acc':
            self.accumulator += action_input
            self.row = self.row + 1

        elif action_type == 'nop':
            self.row = self.row + 1

        else:
            self.row = self.row + action_input

    def run_until_repeat(self):
        while True:
            if self.row in self.rows_visited:
                break
            else:
                self.rows_visited.append(self.row)
                self.take_action(self.actions_dict[self.row]['action'], self.actions_dict[self.row]['count'])


def get_actions_dict(input):
    parsed_input = [s.strip() for s in input]
    actions_dict = {}
    for i, row_input in enumerate(parsed_input):
        actions_dict[i] = {"action": row_input.split(" ")[0], "count": int(row_input.split(" ")[1])}
    return actions_dict


def main():
    INPUT_PATH = Path("data/day8.txt")
    input = get_data(INPUT_PATH)
    actions_dict = get_actions_dict(input)
    bc = BootCode(actions_dict)
    bc.run_until_repeat()
    print(f"Answer part 1: {bc.accumulator}")


##################################################################
# Tests
##################################################################
TEST_INPUT_PATH = Path("data/day8_test_part1.txt")
test_input = get_data(TEST_INPUT_PATH)
test_actions_dict = get_actions_dict(test_input)
bc_test = BootCode(test_actions_dict)
bc_test.run_until_repeat()
assert bc_test.accumulator == 5

if __name__ == "__main__":
    main()
