from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Dict


@dataclass
class PassportEntry:
    byr: Optional[str] = None
    iyr: Optional[str] = None
    eyr: Optional[str] = None
    hgt: Optional[str] = None
    hcl: Optional[str] = None
    ecl: Optional[str] = None
    pid: Optional[str] = None
    cid: Optional[str] = None

    def is_valid(self):
        if None in [
            self.byr,
            self.iyr,
            self.eyr,
            self.hgt,
            self.hcl,
            self.ecl,
            self.pid,
        ]:
            return False
        else:
            return True


def get_data(filename: Path) -> List[str]:
    with open(filename, "r") as f:
        data = f.read()
    return data


def parse_input(input_string: str) -> List[PassportEntry]:

    # Split on blank line.
    passport_entry_list = input_string.split("\n\n")

    # Replace newline with space.
    passport_entry_list = [pe.replace("\n", " ") for pe in passport_entry_list]

    # Split on space
    passport_entry_list = [pe.split(" ") for pe in passport_entry_list]

    # Convert each list with a Passport entry to a dictionary
    passport_entries_parsed = []
    for passport_entry in passport_entry_list:
        passport_dict = {}
        for item in passport_entry:
            passport_dict.update({item.split(":")[0]: item.split(":")[1]})
        passport_entries_parsed.append(passport_dict)

    # Convert list of dictionaries to list of PassportEntry's
    return [
        PassportEntry(**passport_dict)
        for passport_dict in passport_entries_parsed
    ]


def main():
    INPUT_PATH = Path("data/day4.txt")
    input = get_data(INPUT_PATH)
    parsed_input = parse_input(input)
    print(f"Asnwer part 1: {sum([pe.is_valid() for pe in parsed_input])}")


##################################################################
# Test
##################################################################
INPUT_TEST_PATH = Path("data/day4_test.txt")
input_test = get_data(INPUT_TEST_PATH)
parsed_input_test = parse_input(input_test)
assert sum([pe.is_valid() for pe in parsed_input_test]) == 2


if __name__ == "__main__":
    main()
