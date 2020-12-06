from utils.parser import get_input_as_list_of_strings
from day3a import calc_nbr_trees_encountered


if __name__ == '__main__':
    # parameters
    file_name = 'input.txt'
    tree = '#'
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]]

    map_of_area = get_input_as_list_of_strings(file_name)
    product = 1
    for (right, down) in slopes:
        nbr_trees = calc_nbr_trees_encountered(map_of_area, tree, right, down)
        product *= nbr_trees
    print(f'Product of the number of trees encountered'
          f' on each of the listed slopes: {product}')
