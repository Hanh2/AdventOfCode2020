def check_password(rule, password):
    positions_string, target_char = rule.split()
    pos_1, pos_2 = positions_as_ints(positions_string)
    first_char = password[pos_1 - 1]
    second_char = password[pos_2 - 1]
    if first_char == target_char:
        return second_char != target_char
    else:
        return second_char == target_char


def positions_as_ints(bounds_string):
    bounds = bounds_string.split('-')
    return tuple(map(int, bounds))


if __name__ == '__main__':
    nbr_valid_passwords = 0
    with open('input.txt') as f:
        while line := f.readline():
            rule, password = line.split(': ')
            if check_password(rule, password):
                nbr_valid_passwords += 1
    print(nbr_valid_passwords)
