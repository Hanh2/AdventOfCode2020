def parse_input(filename):
    with open(filename) as f:
        full_input = f.read()
        passports = full_input.split('\n\n')
        list_of_passport_fields = map(_get_fields, passports)
    return list_of_passport_fields


def _get_fields(passport):
    field_strings = passport.split()
    fields_components = [field_string.split(':') for
                         field_string in field_strings]
    fields = {key: value for key, value in fields_components}
    return fields


def count_number_of_valid_passports(
        list_of_passport_fields: list, important_fields: list) -> int:
    valid_passport_count = 0
    for passport_fields in list_of_passport_fields:
        if is_valid_passport(passport_fields, important_fields):
            valid_passport_count += 1
    return valid_passport_count


def is_valid_passport(passport_fields, important_fields):
    for important_field in important_fields:
        if important_field not in passport_fields:
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