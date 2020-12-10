from typing import Dict, Iterable, List

from utils.parser import get_input_as_list_of_strings


def main() -> None:
    # parameters
    filename = 'input.txt'
    my_bag_color = 'shiny gold'

    bags_as_strings = get_input_as_list_of_strings(filename)
    contains_bag = get_contains_bag_table(bags_as_strings)
    nbr_valid_outer_bags = get_nbr_valid_outer_bags_containing_bag(
        my_bag_color, contains_bag)

    print(f'Number of bag colors that can contain at least one {my_bag_color}'
          f' bag: {nbr_valid_outer_bags}')


def get_contains_bag_table(bags_as_strings: List[str]) -> Dict[str, List[str]]:
    separator = ' bags contain '
    contains_bag = {}
    for string in bags_as_strings:
        outer_bag_color, inner_bags_full_string = string.split(separator)
        inner_bag_colors = extract_inner_bag_colors(inner_bags_full_string)
        for inner_bag_color in inner_bag_colors:
            if inner_bag_color in contains_bag:
                contains_bag[inner_bag_color].append(outer_bag_color)
            else:
                contains_bag[inner_bag_color] = [outer_bag_color]
    return contains_bag


def extract_inner_bag_colors(inner_bags_full_string: str) -> Iterable[str]:
    inner_bag_strings = inner_bags_full_string.split(', ')
    return map(extract_inner_bag_color, inner_bag_strings)


def extract_inner_bag_color(inner_bag_string: str) -> str:
    if inner_bag_string == 'no other bags.':
        return 'None'
    # remove first (number) and last (the word 'bag(s)') components
    return ' '.join(inner_bag_string.split()[1:-1])


def get_nbr_valid_outer_bags_containing_bag(
        bag: str, contains_bag: Dict[str, List[str]]) -> int:
    valid_outer_bags = set()
    stack = [bag]
    while stack:
        current_bag_color = stack.pop()
        if current_bag_color in contains_bag:
            contains_current_bag = contains_bag[current_bag_color]
            for bag_color in contains_current_bag:
                if bag_color not in valid_outer_bags:
                    valid_outer_bags.add(bag_color)
                    stack.append(bag_color)
    return len(valid_outer_bags)


if __name__ == '__main__':
    main()
