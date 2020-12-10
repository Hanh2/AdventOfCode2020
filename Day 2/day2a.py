from utils.parser import get_input_as_list_of_strings


def check_password(rule: str, password: str):
    bounds_string, char = rule.split()
    bounds = bounds_as_ints(bounds_string)
    nbr_occurrences = password.count(char)
    return bounds[0] <= nbr_occurrences <= bounds[1]


def bounds_as_ints(bounds_string: str):
    bounds = bounds_string.split('-')
    return tuple(map(int, bounds))


if __name__ == '__main__':
    filename = 'input.txt'
    nbr_valid_passwords = 0
    lines = get_input_as_list_of_strings(filename)
    for line in lines:
        rule, password = line.split(': ')
        if check_password(rule, password):
            nbr_valid_passwords += 1
    print(nbr_valid_passwords)
