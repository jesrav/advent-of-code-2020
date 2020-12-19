from dataclasses import dataclass
from pathlib import Path
from typing import List


def get_data(filename: Path) -> List[str]:
    with open(filename, "r") as f:
        data = f.readlines()
    return [s.rstrip() for s in data]


@dataclass
class PaswordEntry:
    """Class for keeping info on password entry and password rule."""

    required_letter: str
    first_number: int
    last_number: float
    password: str

    def is_valid_part1(self):
        character_count = self.password.count(self.required_letter)
        return self.first_number <= character_count <= self.last_number

    def is_valid_part2(self):
        character_indexes_starting_at_1 = [
            pos + 1
            for pos, char in enumerate(self.password)
            if char == self.required_letter
        ]
        first_number_right = self.first_number in character_indexes_starting_at_1
        second_number_right = self.last_number in character_indexes_starting_at_1
        correct_answer = (
                (first_number_right and not second_number_right)
                or (not first_number_right and second_number_right)
        )
        return correct_answer


def string_to_password_entry(s: str) -> PaswordEntry:
    min_count, leftover = s.split("-")
    max_count, leftover, password = leftover.split(" ")
    required_letter = leftover[:-1]
    return PaswordEntry(required_letter, int(min_count), int(max_count), password)


def parse_input(input_list: List[str]) -> List[PaswordEntry]:
    return [string_to_password_entry(s) for s in input_list]


def get_number_of_valid_passwords(
    input_list: List[PaswordEntry],
    question_part,
) -> int:
    if question_part == "part1":
        return len([psw for psw in input_list if psw.is_valid_part1()])
    elif question_part == "part2":
        return len([psw for psw in input_list if psw.is_valid_part2()])
    else:
        raise ValueError("question_part must be either 'part1' or 'part2'.")


def main():
    INPUT_PATH = "data/day2.txt"
    input = get_data(INPUT_PATH)
    parsed_input = parse_input(input)
    print(f"Answer part 1: {get_number_of_valid_passwords(parsed_input, 'part1')}")
    print(f"Answer part 2: {get_number_of_valid_passwords(parsed_input, 'part2')}")


##################################################################
# Test
##################################################################
test_input = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc",
]
parsed_test_input = parse_input(test_input)
assert get_number_of_valid_passwords(parsed_test_input, "part2") == 1
assert get_number_of_valid_passwords(parsed_test_input, "part1") == 2


if __name__ == "__main__":
    main()
