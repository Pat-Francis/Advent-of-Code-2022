def process_input(file: str):
    processed_data = []
    with open(file) as f:
        input_data = f.read().splitlines()

        for line in input_data:
            if len(line.split(" ")) == 2:
                _, value = line.split(" ")
                processed_data.append(int(value))
            else:
                processed_data.append(line)

    return processed_data


def part_one(filename: str):
    instructions = process_input(filename)
    cycle = 0
    x = 1
    interesting = [20, 60, 100, 140, 180, 220]
    signal_strengths = []

    for line in instructions:
        cycle += 1

        if cycle in interesting:
            signal_strengths.append(cycle * x)

        if isinstance(line, int):
            cycle += 1
            if cycle in interesting:
                signal_strengths.append(cycle * x)
            x += line

    return sum(signal_strengths)


def part_two(filename: str):
    pass


if __name__ == "__main__":
    input_file = "./input.txt"
    print(part_one(input_file))
    print(part_two(input_file))