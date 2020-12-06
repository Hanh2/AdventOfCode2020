def get_input_as_list_of_ints(filename: str) -> list:
    with open(filename, 'r') as f:
        list_of_ints = map(int, f.readlines())
    return list_of_ints


def get_input_as_list_of_strings(filename: str) -> list:
    with open(filename, 'r') as f:
        # f.readlines() includes an unwanted '\n' at the end of each line
        list_of_strings = f.read().split('\n')
    return list_of_strings


def get_full_input_as_string(filename: str) -> str:
    with open(filename, 'r') as f:
        full_input = f.read()
    return full_input
