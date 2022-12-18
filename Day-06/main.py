def process_input(file: str):
    with open(file) as f:
        return f.read()


def find_marker(input_stream: str, packet_size: int):
    for count, _ in enumerate(input_stream):
        if len(set(input_stream[count:count + packet_size])) == packet_size:
            return count + packet_size


def part_one(filename: str):
    input_stream = process_input(filename)
    packet_size = 4

    return find_marker(input_stream, packet_size)


def part_two(filename: str):
    input_stream = process_input(filename)
    packet_size = 14

    return find_marker(input_stream, packet_size)


if __name__ == "__main__":
    input_file = "./input.txt"
    print(part_one(input_file))
    print(part_two(input_file))
