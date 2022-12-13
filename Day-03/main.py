def process_input(file: str):
    with open(file) as f:
        rucksacks = f.read().split("\n")

        return rucksacks


def split_sacks(rucksacks):
    return [[i[:len(i)//2], i[len(i)//2:]] for i in rucksacks]


def grouped_elves(rucksacks):
    return [rucksacks[x:x + 3] for x in range(0, len(rucksacks), 3)]


def part_one(filename: str):
    priority_sum = 0
    rucksacks = process_input(filename)
    rucks = split_sacks(rucksacks)

    for ruck in rucks:
        common_item = list(set(ruck[0]) & set(ruck[1]))

        if common_item[0].isupper():
            priority_sum += ord(common_item[0]) - ord('A') + 27
        else:
            priority_sum += ord(common_item[0]) - ord('a') + 1

    return priority_sum


def part_two(filename: str):
    rucksacks = process_input(filename)
    groups = grouped_elves(rucksacks)
    priority_sum = 0

    for group in groups:
        badge = list(set(group[0]) & set(group[1]) & set(group[2]))

        if badge[0].isupper():
            priority_sum += ord(badge[0]) - ord('A') + 27
        else:
            priority_sum += ord(badge[0]) - ord('a') + 1

    return priority_sum


if __name__ == "__main__":
    input_file = "./input.txt"
    print(part_one(input_file))
    print(part_two(input_file))

# TODO: Refactor priority_sum into separate function
