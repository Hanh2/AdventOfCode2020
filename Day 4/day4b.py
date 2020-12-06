import re

from day4a import parse_input


def get_field_checkers() -> dict:
    # regex patterns
    number_pattern = re.compile(r'^\d+$')
    height_pattern = re.compile(r'^\d+(cm|in)$')
    hair_color_pattern = re.compile(r'^#[0-9a-f]{6}$')
    pid_pattern = re.compile(r'^[0-9]{9}$')

    eye_color_set = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    check_height = {
        'cm': lambda x: 150 <= int(x) <= 193,
        'in': lambda x: 59 <= int(x) <= 76
    }

    def height_checker(height):
        if not height_pattern.match(height):
            return False
        unit = height[-2:]
        height_value = height[:-2]
        return check_height[unit](height_value)

    field_checkers = {
        'byr': lambda x: number_pattern.match(x) and 1920 <= int(x) <= 2002,
        'iyr': lambda x: number_pattern.match(x) and 2010 <= int(x) <= 2020,
        'eyr': lambda x: number_pattern.match(x) and 2020 <= int(x) <= 2030,
        'hgt': height_checker,
        'hcl': lambda x: hair_color_pattern.match(x),
        'ecl': lambda x: x in eye_color_set,
        'pid': lambda x: pid_pattern.match(x)
    }
    return field_checkers


def count_number_of_valid_passports(
        passports: dict, field_checkers: dict) -> int:
    valid_passport_count = 0
    for passport in passports:
        if is_valid_passport(passport, field_checker):
            valid_passport_count += 1
    return valid_passport_count


def is_valid_passport(passport: dict, field_checker: dict) -> bool:
    for field, checker in field_checker.items():
        if field not in passport:
            return False
        field_value = passport[field]
        if not checker(field_value):
            return False
    return True


if __name__ == '__main__':
    # parameters
    input_filename = 'input.txt'

    passports = parse_input(input_filename)
    field_checker = get_field_checkers()
    number_of_valid_passports = count_number_of_valid_passports(
        passports, field_checker)
    print(f'The number of valid passports is: {number_of_valid_passports}.')
