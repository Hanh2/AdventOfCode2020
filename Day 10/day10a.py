# Assumptions:
#  * All gaps should be in range 1-3?
from typing import Dict, Iterable
import warnings

from utils.parser import get_input_as_iter_of_ints


def main():
    filename = 'input.txt'

    joltage_adapters = get_input_as_iter_of_ints(filename)
    jolt_diffs = count_jolt_differences(joltage_adapters)
    one_jolt_diffs = jolt_diffs[1]
    three_jolt_diffs = jolt_diffs[3]

    print(f'Product of the number of 1-jolt differences and the number of '
          f'3-jolt differences: \n\t'
          f'{one_jolt_diffs} * {three_jolt_diffs} = '
          f'{one_jolt_diffs * three_jolt_diffs}')


def count_jolt_differences(joltage_adapters: Iterable[int]) -> Dict[int, int]:
    sorted_joltage_adapters = sorted(joltage_adapters)
    nbr_joltage_adapters = len(sorted_joltage_adapters)
    # 3 initialized at 1 because of built-in adapter
    jolt_diffs = {1: 0, 2: 0, 3: 1}
    if nbr_joltage_adapters == 0:
        return jolt_diffs

    jolt_diffs[sorted_joltage_adapters[0]] += 1  # initial difference
    for i in range(1, nbr_joltage_adapters):
        current_jolt_diff = (
                sorted_joltage_adapters[i] - sorted_joltage_adapters[i - 1])
        jolt_diffs[current_jolt_diff] += 1
    if len(jolt_diffs) > 3:
        warnings.warn('There are gaps outside of the range 1-3.')
    return jolt_diffs


if __name__ == '__main__':
    main()
