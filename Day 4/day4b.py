import re

from day4a import parse_input


def get_field_checkers():
    eye_color_set = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    number_pattern = re.compile(r'^\d+$')
    hair_color_pattern = re.compile(r'^#[0-9a-f]{6}$')
    pid_pattern = re.compile(r'^[0-9]{9}$')
    check_height = {
        'cm': lambda x: 150 <= int(x) <= 193,
        'in': lambda x: 59 <= int(x) <= 76
    }

    def height_checker(height):
        if len(height) <= 2:
            return False
        unit = height[-2:]
        height_value = height[:-2]
        return (unit in check_height and
                number_pattern.match(height_value) and
                check_height[unit](height_value))

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


def count_number_of_valid_passports(list_of_passport_fields, field_checkers):
    valid_passport_count = 0
    for passport_fields in list_of_passport_fields:
        if is_valid_passport(passport_fields, field_checker):
            valid_passport_count += 1
    return valid_passport_count


def is_valid_passport(passport_fields, field_checker):
    for field, checker in field_checker.items():
        if field not in passport_fields:
            print(f'field ({field}) not in p_fields')
            return False
        field_value = passport_fields[field]
        if not checker(field_value):
            print(
                f'field_value failed (field: {field}, field_value: {field_value})')
            return False
    return True


if __name__ == '__main__':
    # parameters
    input_filename = 'input.txt'

    list_of_passport_fields = parse_input(input_filename)
    field_checker = get_field_checkers()
    number_of_valid_passports = count_number_of_valid_passports(
        list_of_passport_fields, field_checker)
    print(f'The number of valid passports is: {number_of_valid_passports}.')
