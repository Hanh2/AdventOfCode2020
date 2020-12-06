from utils.parser import get_full_input_as_string


def extract_passports_as_dicts(full_input: str) -> list:
    passports_as_strings = full_input.split('\n\n')
    passports_as_dicts = map(_passport_string_to_dict, passports_as_strings)
    return passports_as_dicts


def _passport_string_to_dict(passport_as_string: str) -> dict:
    field_strings = passport_as_string.split()
    field_key_value_pairs = [
        field_string.split(':') for field_string in field_strings]
    passport_as_dict = {key: value for key, value in field_key_value_pairs}
    return passport_as_dict


def count_number_of_valid_passports(
        passports: list, important_fields: list) -> int:
    valid_passport_count = 0
    for passport in passports:
        if is_valid_passport(passport, important_fields):
            valid_passport_count += 1
    return valid_passport_count


def is_valid_passport(passport: dict, important_fields: list) -> bool:
    for important_field in important_fields:
        if important_field not in passport:
            return False
    return True


if __name__ == '__main__':
    # parameters
    important_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    filename = 'input.txt'

    full_input = get_full_input_as_string(filename)
    passports = extract_passports_as_dicts(full_input)
    number_of_valid_passports = count_number_of_valid_passports(
        passports, important_fields)
    print(f'The number of valid passports is: {number_of_valid_passports}.')
