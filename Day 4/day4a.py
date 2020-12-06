def parse_input(filename: str) -> list:
    with open(filename) as f:
        full_input = f.read()
        passports_as_strings = full_input.split('\n\n')
        passports = map(_get_fields, passports_as_strings)
    return passports


def _get_fields(passport_as_string: str) -> dict:
    field_strings = passport_as_string.split()
    fields_components = [field_string.split(':') for
                         field_string in field_strings]
    fields = {key: value for key, value in fields_components}
    return fields


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
    input_filename = 'input.txt'

    list_of_passport_fields = parse_input(input_filename)
    number_of_valid_passports = count_number_of_valid_passports(
        list_of_passport_fields, important_fields)
    print(f'The number of valid passports is: {number_of_valid_passports}.')
