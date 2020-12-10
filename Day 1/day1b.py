from typing import Iterable, Tuple

from utils.parser import get_input_as_iter_of_ints


# O(n^2) time | O(n) space
# Can be made into O(1) space if numbers list is allowed to be mutated.
def three_number_sum(
        numbers: Iterable[int], target: int) -> Tuple[int, int, int]:
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    for i in range(n - 2):
        num1 = sorted_numbers[i]
        left = i + 1
        right = n - 1
        current_target = target - num1
        while left < right:
            num2, num3 = sorted_numbers[left], sorted_numbers[right]
            left_right_sum = num2 + num3
            if left_right_sum == current_target:
                return num1, num2, num3
            elif left_right_sum < current_target:
                left += 1
            else:
                right -= 1
    return None


if __name__ == '__main__':
    # parameters
    numbers = get_input_as_iter_of_ints('input.txt')
    target = 2020

    triplet = three_number_sum(numbers, 2020)
    if triplet:
        x, y, z = triplet
        answer = x * y * z
        print(f'The answer is {answer}')
    else:
        print(f'No triplet adding up to {target} found.')
