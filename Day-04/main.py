def process_input(file: str):
    with open(file) as f:
        id_numbers = f.read().splitlines()

        return [line.split(",") for line in id_numbers]


def enveloped_range(range1: list, range2: list):
    if (range1[0] <= range2[0] and range1[1] >= range2[1]) or \
       (range2[0] <= range1[0] and range2[1] >= range1[1]):
        return True
    else:
        return False


def range_overlap(range1: list, range2: list):
    return max(range1[0], range2[0]) <= min(range1[1], range2[1])


def part_one(filename: str):
    ranges_list = process_input(filename)
    count = 0

    for ranges in ranges_list:
        range1 = [int(x) for x in ranges[0].split("-")]
        range2 = [int(x) for x in ranges[1].split("-")]
        print(ranges, range1, range2)
        if enveloped_range(range1, range2):
            count += 1

    return count


def part_two(filename: str):
    ranges_list = process_input(filename)
    count = 0

    for ranges in ranges_list:
        range1 = [int(x) for x in ranges[0].split("-")]
        range2 = [int(x) for x in ranges[1].split("-")]

        if range_overlap(range1, range2):
            count += 1

    return count


if __name__ == "__main__":
    input_file = "./input.txt"
    print(part_one(input_file))
    print(part_two(input_file))
