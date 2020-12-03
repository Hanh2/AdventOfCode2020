def two_sum(numbers, target):
    seen_numbers = set()
    for num in numbers:
        complement = target - num
        if complement in seen_numbers:
            return num, complement
        else:
            seen_numbers.add(num)
    return None


def get_input_from_file(file_name):
    with open(file_name, 'r') as f:
        list_of_numbers = map(int, f.readlines())
    return list_of_numbers


if __name__ == "__main__":
    # parameters
    numbers = get_input_from_file('input.txt')
    target = 2020

    pair = two_sum(numbers, 2020)
    if pair:
        x, y = pair
        answer = x * y
        print(f'The answer is {answer}')
    else:
        print(f'No pair adding up to {target} found.')
