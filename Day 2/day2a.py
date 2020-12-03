def check_password(rule, password):
    bounds_string, char = rule.split()
    bounds = bounds_as_ints(bounds_string)
    nbr_occurrences = password.count(char)
    return bounds[0] <= nbr_occurrences <= bounds[1]


def bounds_as_ints(bounds_string):
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
