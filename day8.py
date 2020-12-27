from pathlib import Path
from typing import List, Dict
import copy


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
        self.last_row = max([k for k in actions_dict])

    def take_action(self, action_type: str, action_input: int) -> int:
        if action_type == 'acc':
            self.accumulator += action_input
            self.row = self.row + 1

        elif action_type == 'nop':
            self.row = self.row + 1

        else:
            self.row = self.row + action_input

    def run_until_repeat_or_finished(self):
        while True:
            if self.row in self.rows_visited:
                return False
            elif self.row == self.last_row + 1:
                return True
            else:
                self.rows_visited.append(self.row)
                self.take_action(self.actions_dict[self.row]['action'], self.actions_dict[self.row]['count'])


def switch_jmp_nop(actions_dict, line):
    if actions_dict[line]['action'] == 'jmp':
        actions_dict_modified = copy.deepcopy(actions_dict)
        actions_dict_modified[line]['action'] = 'nop'
        return actions_dict_modified
    elif actions_dict[line]['action'] == 'nop':
        actions_dict_modified = copy.deepcopy(actions_dict)
        actions_dict_modified[line]['action'] = 'jmp'
        return actions_dict_modified
    else:
        return actions_dict


def fix_boot_code(actions_dict):
    possible_bug_lines = [
        k for k, v in actions_dict.items() if v['action'] in ['nop', 'jmp']
    ]
    for line in possible_bug_lines:
        actions_dict_modified = switch_jmp_nop(actions_dict, line)
        bc = BootCode(actions_dict_modified)
        code_finished = bc.run_until_repeat_or_finished()
        if code_finished:
            return bc


def get_actions_dict(input):
    parsed_input = [s.strip() for s in input]
    actions_dict = {}
    for i, row_input in enumerate(parsed_input):
        actions_dict[i + 1] = {"action": row_input.split(" ")[0], "count": int(row_input.split(" ")[1])}
    return actions_dict


def main():
    INPUT_PATH = Path("data/day8.txt")
    input = get_data(INPUT_PATH)
    actions_dict = get_actions_dict(input)

    # Part 1
    bc = BootCode(actions_dict)
    bc.run_until_repeat_or_finished()
    print(f"Answer part 1: {bc.accumulator}")

    # Part 2
    fixed_bc = fix_boot_code(actions_dict)
    print(f"Answer part 2: {fixed_bc.accumulator}")


##################################################################
# Tests
##################################################################
# Part 1
TEST_INPUT_PATH = Path("data/day8_test_part1.txt")
test_input = get_data(TEST_INPUT_PATH)
test_actions_dict = get_actions_dict(test_input)
bc_test = BootCode(test_actions_dict)
bc_test.run_until_repeat_or_finished()
assert bc_test.accumulator == 5

# Part 2
fixed_bc_test = fix_boot_code(test_actions_dict)
assert fixed_bc_test.accumulator == 8


if __name__ == "__main__":
    main()
