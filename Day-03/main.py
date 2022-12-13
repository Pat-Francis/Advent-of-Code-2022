def process_input(file: str):
    with open(file) as f:
        rucksacks = f.read().split("\n")

        return rucksacks


def split_sacks(rucksacks):
    return [[i[:len(i)//2], i[len(i)//2:]] for i in rucksacks]


def grouped_elves(rucksacks):
    return [rucksacks[x:x + 3] for x in range(0, len(rucksacks), 3)]


def priority_sum(common_items):
    pri_sum = 0

    for item in common_items:
        if item[0].isupper():
            pri_sum += ord(item[0]) - ord('A') + 27
        else:
            pri_sum += ord(item[0]) - ord('a') + 1

    return pri_sum


def part_one(filename: str):
    common_items = []
    rucksacks = process_input(filename)
    rucks = split_sacks(rucksacks)

    for ruck in rucks:
        common_items.append(list(set(ruck[0]) & set(ruck[1])))

    return priority_sum(common_items)


def part_two(filename: str):
    badges = []
    rucksacks = process_input(filename)
    groups = grouped_elves(rucksacks)

    for group in groups:
        badges.append(list(set(group[0]) & set(group[1]) & set(group[2])))

    return priority_sum(badges)


if __name__ == "__main__":
    input_file = "./input.txt"
    print(part_one(input_file))
    print(part_two(input_file))
