import re
from typing import Callable, Dict, List

from utils.parser import get_input_as_list_of_strings
from day4a import passport_string_to_dict


def get_field_checkers() -> Dict[str, Callable]:
    # regex patterns
    byr_pattern = re.compile(r'^(19[2-9][0-9]|200[0-2])$')
    iyr_pattern = re.compile(r'^(20(1[0-9]|20))$')
    eyr_pattern = re.compile(r'^(20(2[0-9]|30))$')
    cm_pattern = '1([5-8][0-9]|9[0-3])cm'
    in_pattern = '(59|6[0-9]|7[0-6])in'
    hgt_pattern = re.compile(f'^({cm_pattern}|{in_pattern})$')
    hcl_pattern = re.compile(r'^#[0-9a-f]{6}$')
    ecl_pattern = re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$')
    pid_pattern = re.compile(r'^[0-9]{9}$')

    field_checkers = {
        'byr': lambda x: byr_pattern.match(x),
        'iyr': lambda x: iyr_pattern.match(x),
        'eyr': lambda x: eyr_pattern.match(x),
        'hgt': lambda x: hgt_pattern.match(x),
        'hcl': lambda x: hcl_pattern.match(x),
        'ecl': lambda x: ecl_pattern.match(x),
        'pid': lambda x: pid_pattern.match(x)
    }
    return field_checkers


def count_number_of_valid_passports(
        passports: List[Dict[str, str]],
        field_checkers: Dict[str, Callable]) -> int:
    valid_passport_count = 0
    for passport in passports:
        if is_valid_passport(passport, field_checker):
            valid_passport_count += 1
    return valid_passport_count


def is_valid_passport(
        passport: Dict[str, str], field_checker: Dict[str, Callable]) -> bool:
    for field, checker in field_checker.items():
        if field not in passport:
            return False
        field_value = passport[field]
        if not checker(field_value):
            return False
    return True


if __name__ == '__main__':
    # parameters
    filename = 'input.txt'

    passports_as_strings = get_input_as_list_of_strings(
        filename, separate_by_blank_lines=True)
    passports = map(passport_string_to_dict, passports_as_strings)
    field_checker = get_field_checkers()
    number_of_valid_passports = count_number_of_valid_passports(
        passports, field_checker)
    print(f'The number of valid passports is: {number_of_valid_passports}.')
