from utils.parser import get_input_as_list_of_ints


def two_sum(numbers, target):
    seen_numbers = set()
    for num in numbers:
        complement = target - num
        if complement in seen_numbers:
            return num, complement
        else:
            seen_numbers.add(num)
    return None


if __name__ == "__main__":
    # parameters
    numbers = get_input_as_list_of_ints('input.txt')
    target = 2020

    pair = two_sum(numbers, 2020)
    if pair:
        x, y = pair
        answer = x * y
        print(f'The answer is {answer}')
    else:
        print(f'No pair adding up to {target} found.')
