from utils.parser import get_input_as_list_of_strings


def passport_string_to_dict(passport_as_string: str) -> dict:
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

    passports_as_strings = get_input_as_list_of_strings(
        filename, separated_by_blank_lines=True)
    passports = map(passport_string_to_dict, passports_as_strings)
    number_of_valid_passports = count_number_of_valid_passports(
        passports, important_fields)
    print(f'The number of valid passports is: {number_of_valid_passports}.')
