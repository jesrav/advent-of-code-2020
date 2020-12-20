from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Dict
import re

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

    def all_fields_present(self):
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

    def byr_valid(self):
        if 1920 <= int(self.byr) <= 2002:
            return True
        else:
            return False

    def iyr_valid(self):
        if 2010 <= int(self.iyr) <= 2020:
            return True
        else:
            return False

    def eyr_valid(self):
        if 2020 <= int(self.eyr) <= 2030:
            return True
        else:
            return False

    def hgt_valid(self):

        char_is_digit_list = [c.isdigit() for c in self.hgt]
        if sum(char_is_digit_list) == 0:
            return False
        fist_digit_index = char_is_digit_list.index(True)
        if fist_digit_index != 0:
            return False
        last_digit_index = len(char_is_digit_list) -1 - char_is_digit_list[::-1].index(True)
        if not all(char_is_digit_list[fist_digit_index:last_digit_index]):
            return False

        digits = self.hgt[:last_digit_index + 1]
        measure = self.hgt[last_digit_index + 1:]
        if measure not in ["cm", 'in']:
            return False
        if measure == 'cm':
            if not 150 <= int(digits) <= 193:
                return False
            else:
                return True
        if measure == 'in':
            if not 59 <= int(digits) <= 76:
                return False
            else:
                return True

    def hcl_is_valid(self):
        if self.hcl[0] != "#":
            return False
        if len(self.hcl) != 7:
            return False
        pattern = re.compile("[a-z0-9]+")
        if pattern.fullmatch(self.hcl[1:]) is None:
            return False
        return True

    def ecl_valid(self):
        return self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def pid_id_valid(self):
        only_digits = all([c.isdigit() for c in self.pid])
        has_nine_digits = len(self.pid) == 9
        return (only_digits and has_nine_digits)

    def is_valid(self):
        return (
            self.byr_valid()
            and self.hcl_is_valid()
            and self.iyr_valid()
            and self.eyr_valid()
            and self.hgt_valid()
            and self.pid_id_valid()
            and self.ecl_valid()
        )


def get_data(filename: Path) -> List[str]:
    with open(filename, "r") as f:
        data = f.read()
    return data


def parse_input(input_string: str) -> List[PassportEntry]:

    # Remove last newline, if present
    if input_string.endswith("\n"):
        input_string = input_string[:-1]

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
    part1_sum = sum([pe.all_fields_present() for pe in parsed_input])
    print(f"Asnwer part 1: {part1_sum}")
    part2_sum = sum([pe.all_fields_present() and pe.is_valid() for pe in parsed_input])
    print(f"Asnwer part 1: {part2_sum}")

##################################################################
# Tests
##################################################################

# Part 1
INPUT_TEST_PART1_PATH = Path("data/day4_test.txt")
input_test_part_1 = get_data(INPUT_TEST_PART1_PATH)
parsed_input_test_part_1 = parse_input(input_test_part_1)
assert sum([pe.all_fields_present() for pe in parsed_input_test_part_1]) == 2

# Part 2
valid_byr = PassportEntry(byr="2002")
invalid_byr = PassportEntry(byr="2003")
assert valid_byr.byr_valid() == True
assert invalid_byr.byr_valid() == False

valid_hgt = PassportEntry(hgt="60in")
invalid_hgt = PassportEntry(hgt="140cm")
assert valid_hgt.hgt_valid() == True
assert invalid_hgt.hgt_valid() == False

valid_hcl = PassportEntry(hcl="#123abc")
invalid_hcl = PassportEntry(hcl="123abc")
assert valid_hcl.hcl_is_valid() == True
assert invalid_hcl.hcl_is_valid() == False

INPUT_TEST_PART2_PATH = Path("data/day4_test_part2.txt")
input_test_part_2 = get_data(INPUT_TEST_PART2_PATH)
parsed_input_test_part_2 = parse_input(input_test_part_2)
assert sum([pe.all_fields_present() and pe.is_valid() for pe in parsed_input_test_part_2]) == 4


if __name__ == "__main__":
    main()
