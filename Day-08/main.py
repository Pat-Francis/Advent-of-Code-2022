def process_input(file: str):
    with open(file) as f:
        input_data = f.read().splitlines()

    tree_grid = []

    for row in input_data:
        tree_grid.append([int(i) for i in row])

    return tree_grid


def scenic_score(views: list[list], tree_height: int):
    view_score = 1

    for direction in views:
        dir_score = 0

        for tree in direction:
            if tree < tree_height:
                dir_score += 1
            else:
                dir_score += 1
                break

        view_score *= dir_score

    return view_score


def part_one(filename: str):
    tree_grid = process_input(filename)
    visible_trees = (len(tree_grid[0]) * 2) + (len(tree_grid) - 2) * 2  # Counts all the 'edge' trees

    # First and last rows/columns omitted, already added to visible_trees
    for i, row in enumerate(tree_grid[1:-1]):
        for j, tree in enumerate(row[1:-1]):
            adj_check = (
                max([row[j + 1] for row in tree_grid][:i + 1]) < tree,  # North
                max([row[j + 1] for row in tree_grid][i + 2:]) < tree,  # South
                max(row[j + 2:]) < tree,  # East
                max(row[:j + 1]) < tree,  # West
            )
            if any(adj_check):
                visible_trees += 1

    return visible_trees


def part_two(filename: str):
    tree_grid = process_input(filename)
    view_scores = []

    for i, row in enumerate(tree_grid[1:-1]):
        for j, tree in enumerate(row[1:-1]):
            views = [[row[j + 1] for row in tree_grid][i::-1],  # North
                     [row[j + 1] for row in tree_grid][i + 2:],  # South
                     row[j + 2:],  # East
                     row[j::-1]]  # West
            view_scores.append(scenic_score(views, tree))

    return max(view_scores)


if __name__ == "__main__":
    input_file = "./input.txt"
    print(part_one(input_file))
    print(part_two(input_file))
