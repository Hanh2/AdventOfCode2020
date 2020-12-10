from typing import Iterable, Tuple

from utils.parser import get_input_as_iter_of_ints


def two_number_sum(numbers: Iterable[int], target: int) -> Tuple[int, int]:
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
    numbers = get_input_as_iter_of_ints('input.txt')
    target = 2020

    pair = two_number_sum(numbers, 2020)
    if pair:
        x, y = pair
        answer = x * y
        print(f'The answer is {answer}')
    else:
        print(f'No pair adding up to {target} found.')
