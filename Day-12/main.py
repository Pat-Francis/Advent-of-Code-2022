from collections import defaultdict
from heapq import heappop, heappush


def process_input(file: str):
    with open(file) as f:
        input_data = f.read().splitlines()

    processed_input = []
    starting_loc = ()
    end_loc = ()

    for line in input_data:
        processed_input.append([i for i in line])

    for i, row in enumerate(processed_input):
        for j, loc in enumerate(row):
            if loc == "S":
                starting_loc = (i, j)

            if loc == "E":
                end_loc = (i, j)

    return processed_input, starting_loc, end_loc


def next_letter(a):
    return chr(ord(a) + 1)


def get_adjacent(height_map):
    adjacent = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    locations = []
    neighbours = defaultdict(dict)

    for i, _ in enumerate(height_map):
        for j, _ in enumerate(height_map[0]):
            locations.append((i, j))

    for x, y in locations:
        for dx, dy in adjacent:
            if 0 <= x + dx < len(height_map) and 0 <= y + dy < len(height_map[0]):
                neighbours[x, y].update({(x + dx, y + dy): height_map[x + dx][y + dy]})

    return locations, neighbours


def dijkstra(locations, edges, start, end):
    visited = []
    queue = [(0, start)]
    letter = "a"

    while queue:
        path_len, location = heappop(queue)

        if location == end:
            return path_len

        for neighbour, neigh_letter in edges[location].items():
            if neighbour not in visited:
                if neigh_letter == next_letter(letter) or neigh_letter == letter:
                    visited.append(neighbour)
                    if neigh_letter == next_letter(letter):
                        letter = next_letter(letter)

                    heappush(queue, (path_len + 1, neighbour))

                if letter == "z" and neigh_letter == "E":
                    heappush(queue, (path_len + 1, neighbour))

    return queue[0]


def part_one(filename: str):
    height_map, start, end = process_input(filename)
    locations, edges = get_adjacent(height_map)

    return dijkstra(locations, edges, start, end)


def part_two(filename: str):
    pass


if __name__ == "__main__":
    input_file = "./test_input.txt"
    print(part_one(input_file))
    print(part_two(input_file))