from utils.parser import get_input_as_list_of_strings


def seat_string_to_id(seat_string: str) -> int:
    binary_string = seat_string_to_binary_string(seat_string)
    seat_id = int(binary_string, base=2)
    return seat_id


def seat_string_to_binary_string(seat_string: str) -> str:
    binary_string = ''.join(
        ['1' if (ch == 'B' or ch == 'R') else '0' for ch in seat_string]
    )
    return binary_string


if __name__ == '__main__':
    filename = 'input.txt'
    boarding_passes = get_input_as_list_of_strings(filename)
    seat_ids = map(seat_string_to_id, boarding_passes)
    print(f'The highest seat ID is {max(seat_ids)}.')
