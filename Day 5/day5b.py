from utils.parser import get_input_as_list_of_strings
from day5a import seat_string_to_id


def get_missing_seat_id(seat_ids):
    set_of_seat_ids = set(seat_ids)
    min_id = min(set_of_seat_ids)
    max_id = max(set_of_seat_ids)
    for i in range(min_id + 1, max_id):  # the missing ID is not on the edge
        if i not in set_of_seat_ids:
            return i
    return -1  # if no seats are missing


if __name__ == '__main__':
    filename = 'input.txt'
    boarding_passes = get_input_as_list_of_strings(filename)
    seat_ids = map(seat_string_to_id, boarding_passes)
    missing_seat_id = get_missing_seat_id(seat_ids)
    print(f'The missing seat ID is {missing_seat_id}.')
