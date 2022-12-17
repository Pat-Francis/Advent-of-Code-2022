def process_input(file: str):
    with open(file) as f:
        crates, moves = f.read().split("\n\n")
        processed_moves = []
        processed_stacks = [list() for x in crates if x.isnumeric()]

        for line in crates.splitlines()[:-1]:
            stack_count = 0

            for i in line[1::4]:
                if i.isalpha():
                    processed_stacks[stack_count].append(i)
                stack_count += 1

        for move in moves.splitlines():
            processed_moves.append([int(s) for s in move.split() if s.isdigit()])

    return processed_stacks, processed_moves


def part_one(filename: str):
    stacks, moves = process_input(filename)

    for moves, move_from, move_to in moves:
        for i in range(0, moves):
            stacks[move_to - 1].insert(0, stacks[move_from - 1][0])
            stacks[move_from - 1].pop(0)

    return ''.join(item[0] for item in stacks)


def part_two(filename: str):
    pass


if __name__ == "__main__":
    input_file = "./input.txt"
    print(part_one(input_file))
    print(part_two(input_file))

