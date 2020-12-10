from typing import Iterable, List
import itertools

from utils.parser import get_input_as_iter_of_ints


def main():
    filename = 'input.txt'
    preamble_size = 25

    list_of_nbrs = list(get_input_as_iter_of_ints(filename))
    first_nbr_breaking_rule = get_first_nbr_breaking_rule(
        list_of_nbrs, preamble_size)
    print(f'The first number not satisfying the property: '
          f'{first_nbr_breaking_rule}')


def get_first_nbr_breaking_rule(
        list_of_nbrs: List[int], preamble_size: int) -> int:
    for i in range(preamble_size, len(list_of_nbrs)):
        curr_nbr = list_of_nbrs[i]
        prev_nbrs = itertools.islice(list_of_nbrs, i - preamble_size, i)
        if two_number_sum(prev_nbrs, curr_nbr) is None:
            return curr_nbr


def two_number_sum(numbers: Iterable[int], target: int):
    seen_numbers = set()
    for num in numbers:
        complement = target - num
        if complement in seen_numbers:
            return num, complement
        else:
            seen_numbers.add(num)
    return None


if __name__ == '__main__':
    main()
