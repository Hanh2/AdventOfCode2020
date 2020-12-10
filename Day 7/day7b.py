from typing import Dict, Iterable, List, Tuple

from utils.parser import get_input_as_list_of_strings

# type used for content
content_type = List[Tuple[int, str]]


def main() -> None:
    # parameters
    filename = 'input.txt'
    my_bag_color = 'shiny gold'

    bags_as_strings = get_input_as_list_of_strings(filename)
    content_of_bag = get_content_table(bags_as_strings)
    nbr_required_bags = get_nbr_required_bags_inside(
        my_bag_color, content_of_bag)

    print(f'Number of bags required inside a {my_bag_color} bag: '
          f'{nbr_required_bags}')


def get_content_table(bags_as_strings: List[str]) -> Dict[str, content_type]:
    separator = ' bags contain '
    content_of_bag = {}
    for string in bags_as_strings:
        outer_bag_color, inner_bags_full_string = string.split(separator)
        inner_bag_colors = list(
            extract_inner_bags_info(inner_bags_full_string))
        content_of_bag[outer_bag_color] = inner_bag_colors
    return content_of_bag


def extract_inner_bags_info(inner_bags_full_string: str) \
        -> Iterable[Tuple[str]]:
    if inner_bags_full_string == 'no other bags.':
        return []
    inner_bag_strings = inner_bags_full_string.split(', ')
    return map(extract_inner_bag_info, inner_bag_strings)


def extract_inner_bag_info(inner_bag_string: str) -> Tuple[str]:
    inner_bag_string_elements = inner_bag_string.split()
    inner_bag_multiplicity = int(inner_bag_string_elements[0])
    inner_bag_color = ' '.join(inner_bag_string_elements[1:-1])
    return inner_bag_multiplicity, inner_bag_color


def get_nbr_required_bags_inside(
        bag: str, content_of: Dict[str, content_type]) -> int:
    cache = {}
    return _nbr_bags_inside_recurse(bag, content_of, cache)


def _nbr_bags_inside_recurse(
        bag: str, content_of: Dict[str, content_type], cache: Dict[str, int]) \
        -> int:
    if bag not in cache:
        nbr_bags_inside = 0
        for inner_bag in content_of[bag]:
            multiplicity, inner_bag_color = inner_bag
            bags_inside_inner_bag = _nbr_bags_inside_recurse(
                inner_bag_color, content_of, cache)
            nbr_bags_inside += multiplicity * (1 + bags_inside_inner_bag)
        cache[bag] = nbr_bags_inside
    return cache[bag]


if __name__ == '__main__':
    main()
