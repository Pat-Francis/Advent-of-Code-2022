def process_input(file: str):
    with open(file) as f:
        id_numbers = f.read().splitlines()
        split_ranges = [line.split(",") for line in id_numbers]
        processed_input = []

        for line in split_ranges:
            range1 = [int(x) for x in line[0].split("-")]
            range2 = [int(x) for x in line[1].split("-")]
            processed_input.append([range1, range2])

        return processed_input


def enveloped_range(range1, range2):
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
        if enveloped_range(ranges[0], ranges[1]):
            count += 1

    return count


def part_two(filename: str):
    ranges_list = process_input(filename)
    count = 0

    for ranges in ranges_list:
        if range_overlap(ranges[0], ranges[1]):
            count += 1

    return count


if __name__ == "__main__":
    input_file = "./input.txt"
    print(part_one(input_file))
    print(part_two(input_file))
