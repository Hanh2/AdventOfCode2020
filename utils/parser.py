from typing import Iterator, List


def get_input_as_iter_of_ints(filename: str) -> Iterator[int]:
    with open(filename, 'r') as f:
        while nbr := f.readline():
            yield int(nbr)


def get_input_as_list_of_strings(
        filename: str, separate_by_blank_lines: bool = False) -> List[str]:
    separator = '\n' if not separate_by_blank_lines else '\n\n'
    with open(filename, 'r') as f:
        # f.readlines() includes an unwanted '\n' at the end of each line
        list_of_strings = f.read().split(separator)
    return list_of_strings


def get_full_input_as_string(filename: str) -> str:
    with open(filename, 'r') as f:
        full_input = f.read()
    return full_input
