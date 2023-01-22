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
    instructions = process_input(filename)
    cycle = 0
    x = 1
    pixels = []

    for line in instructions:
        if cycle % 40 in range(x - 1, x + 2):
            pixels.append('#')
        else:
            pixels.append('.')
        cycle += 1

        if isinstance(line, int):
            if cycle % 40 in range(x - 1, x + 2):
                pixels.append('#')
            else:
                pixels.append('.')
            cycle += 1
            x += line

    # Print the 'pixels' screen
    pixel_counter = 0
    for x in range(0, 7):
        print(''.join(pixels[pixel_counter: pixel_counter + 40]))
        pixel_counter += 40


if __name__ == "__main__":
    input_file = "./input.txt"
    print(part_one(input_file))
    print(part_two(input_file))