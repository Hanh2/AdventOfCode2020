def get_map_as_list_of_strings(file_name):
    with open(file_name) as f:
        input_map = f.read().splitlines()
    return input_map


def calc_nbr_trees_encountered(map_of_area, tree, right, down):
    row = 0
    col = 0
    height = len(map_of_area)
    width = len(map_of_area[0])
    nbr_trees = 0
    while row < height:
        if map_of_area[row][col] == tree:
            nbr_trees += 1
        col = (col + right) % width
        row += down
    return nbr_trees


if __name__ == '__main__':
    file_name = 'input.txt'
    tree = '#'
    right, down = 3, 1

    map_of_area = get_map_as_list_of_strings(file_name)
    nbr_trees = calc_nbr_trees_encountered(map_of_area, tree, right, down)
    print(f'Number of trees encountered: {nbr_trees}')
