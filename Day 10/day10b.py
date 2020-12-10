# Assumption:
#  * No duplicate values in input list
from itertools import chain
from typing import Iterable

from utils.parser import get_input_as_iter_of_ints


def main():
    filename = 'input.txt'
    max_gap = 3

    joltage_adapters = get_input_as_iter_of_ints(filename)
    nbr_distinct_arrangements = count_nbr_distinct_arrangements(
        joltage_adapters, max_gap)

    print(f'Number of distinct ways to arrange the adapters:\n\t'
          f'{nbr_distinct_arrangements}')


def count_nbr_distinct_arrangements(
        joltage_adapters: Iterable[int], max_gap: int) -> int:
    # add zero to the list to reduce number of edge cases
    sorted_joltage_adapters = sorted(chain(joltage_adapters, [0]))
    nbr_adapters = len(sorted_joltage_adapters)
    if nbr_adapters == 0 or sorted_joltage_adapters[0] > max_gap:
        return 0

    # one possible arrangement if no adapters
    nbr_arrangements = [1]
    for i in range(1, nbr_adapters):
        current_adapter = sorted_joltage_adapters[i]
        current_nbr_arrangements = 0
        k = 1
        while (i - k >= 0 and
               current_adapter - sorted_joltage_adapters[i - k] <= max_gap):
            current_nbr_arrangements += nbr_arrangements[-k]
            k += 1
        nbr_arrangements.append(current_nbr_arrangements)
    return nbr_arrangements[-1]


if __name__ == '__main__':
    main()
