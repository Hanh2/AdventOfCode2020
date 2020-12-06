from utils.parser import get_input_as_list_of_strings


def extract_group_answer(group_answers_as_ml_string: list) -> str:
    group_answers_as_strings = group_answers_as_ml_string.split('\n')
    group_answers_as_sets = map(set, group_answers_as_strings)
    group_answers_as_set = set.intersection(*group_answers_as_sets)
    group_answers_as_string = ''.join(sorted(group_answers_as_set))
    return group_answers_as_string


if __name__ == '__main__':
    filename = 'input.txt'
    group_answers_as_ml_strings = get_input_as_list_of_strings(
        filename, separate_by_blank_lines=True)
    group_answers = map(extract_group_answer, group_answers_as_ml_strings)
    counts = map(len, group_answers)
    sum_of_counts = sum(counts)
    print(f'The sum of the counts is {sum_of_counts}.')
