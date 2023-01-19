def process_input(file: str):
    with open(file) as f:
        input_data = f.read().splitlines()

    tree_grid = []

    for row in input_data:
        tree_grid.append([int(i) for i in row])

    return tree_grid


def part_one(filename: str):
    tree_grid = process_input(filename)
    visible_trees = (len(tree_grid[0]) * 2) + (len(tree_grid) - 2) * 2  # Counts all the 'edge' trees

    for i, row in enumerate(tree_grid[1:-1]):
        for j, tree in enumerate(row[1:-1]):
            # print(tree, i + 1, j + 1)
            adj_check = (
                    max([row[j + 1] for row in tree_grid][:i + 1]) < tree_grid[i + 1][j + 1],  # North
                    max([row[j + 1] for row in tree_grid][i + 2:]) < tree_grid[i + 1][j + 1],  # South
                    max(row[j + 2:]) < tree_grid[i + 1][j + 1],  # East
                    max(row[:j + 1]) < tree_grid[i + 1][j + 1],  # West
            )
            if any(adj_check):
                visible_trees += 1

    return visible_trees


def part_two(filename: str):
    pass


if __name__ == "__main__":
    input_file = "./input.txt"
    print(part_one(input_file))
    print(part_two(input_file))