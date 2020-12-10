from typing import List

from utils.parser import get_input_as_iter_of_ints


def main() -> None:
    filename = 'input.txt'
    first_invalid_nbr = 15690279

    list_of_nbrs = list(get_input_as_iter_of_ints(filename))
    encryption_weakness = find_encryption_weakness(
        list_of_nbrs, first_invalid_nbr)

    print(f'The encryption weakness in the XMAS-encrypted list of numbers: '
          f'{encryption_weakness}')


def find_encryption_weakness(
        list_of_nbrs: List[int], first_invalid_nbr: int) -> int:
    contiguous_set = ContiguousSet(list_of_nbrs)
    while contiguous_set.total != first_invalid_nbr:
        if contiguous_set.total < first_invalid_nbr:
            contiguous_set.increment_end_idx()
        else:
            contiguous_set.increment_start_idx()
    return contiguous_set.sum_of_smallest_and_largest_values()


class ContiguousSet:
    def __init__(self, list_of_nbrs: List[int]) -> None:
        if len(list_of_nbrs) == 0:
            raise Exception('Empty list.')
        self.list_of_nbrs = list_of_nbrs
        self.max_idx = len(list_of_nbrs) - 1
        self._start_idx = 0
        self._end_idx = 0
        self.total = list_of_nbrs[0]

    def increment_start_idx(self) -> None:
        if self._start_idx >= self._end_idx:
            raise Exception('The contiguous set is of size zero.')

        self.total -= self.list_of_nbrs[self._start_idx]
        self._start_idx += 1

    def increment_end_idx(self) -> None:
        if self._end_idx >= self.max_idx:
            print(self.max_idx, self._end_idx)
            raise Exception('Reached end of list.')

        self._end_idx += 1
        self.total += self.list_of_nbrs[self._end_idx]

    def sum_of_smallest_and_largest_values(self) -> int:
        list_of_nbrs = self.list_of_nbrs
        smallest = largest = list_of_nbrs[self._end_idx]
        for i in range(self._start_idx, self._end_idx):
            current_nbr = list_of_nbrs[i]
            if current_nbr < smallest:
                smallest = current_nbr
            elif current_nbr > largest:
                largest = current_nbr
        return smallest + largest


if __name__ == '__main__':
    main()
