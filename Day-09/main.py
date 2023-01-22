def process_input(file: str):
    with open(file) as f:
        input_data = f.read().splitlines()

    head_moves = []

    for line in input_data:
        direction, move = line.split(" ")
        head_moves.append([direction, int(move)])

    return head_moves


def part_one(filename: str):
    moves = process_input(filename)
    head_loc = [0, 0]
    tail_loc = [0, 0]
    tail_trail = []
    head_deltas = {'R': [0, 1],
                   'L': [0, -1],
                   'U': [1, 0],
                   'D': [-1, 0]
                   }

    for move in moves:
        direction = move[0]
        steps = move[1]

        for step in range(0, steps):
            prev_head = head_loc
            head_loc = [sum(i) for i in zip(head_loc, head_deltas.get(direction))]
            head_tail_delta = [x - y for (x, y) in zip(head_loc, tail_loc)]

            if any(i > 1 for i in head_tail_delta) or any(i < -1 for i in head_tail_delta):
                tail_loc = prev_head

            if tail_loc not in tail_trail:
                tail_trail.append(tail_loc)

    return len(tail_trail)


def part_two(filename: str):
    moves = process_input(filename)
    knots_length = 10
    knots = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    knots_indices = [[i, i + 1] for i in range(0, knots_length - 1)]
    tail_trail = []
    head_deltas = {'R': [1, 0],
                   'L': [-1, 0],
                   'U': [0, 1],
                   'D': [0, -1]
                   }

    for move in moves:
        direction = move[0]
        steps = move[1]

        for step in range(0, steps):
            for head, tail in knots_indices:
                if head == 0:
                    knots[head] = [sum(i) for i in zip(knots[head], head_deltas.get(direction))]

                head_tail_delta = [x - y for (x, y) in zip(knots[head], knots[tail])]

                tail_update = []
                if sum(abs(i) for i in head_tail_delta) > 2:
                    for coord in head_tail_delta:
                        tail_update.append(coord // abs(coord))
                else:
                    for coord in head_tail_delta:
                        if coord > 1:
                            tail_update.append(1)
                        elif coord < -1:
                            tail_update.append(-1)
                        else:
                            tail_update.append(0)

                knots[tail] = [sum(i) for i in zip(knots[tail], tail_update)]

                if tail == 9 and knots[tail] not in tail_trail:
                    tail_trail.append(knots[tail])

    return len(tail_trail)


if __name__ == "__main__":
    input_file = "./input.txt"
    print(part_one(input_file))
    print(part_two(input_file))
