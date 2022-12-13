def process_input(file: str):
    with open(file) as f:
        rucksacks = f.read().split("\n")
        split_sacks = [[i[:len(i)//2], i[len(i)//2:]] for i in rucksacks]

        return split_sacks


def part_one(filename: str):
    priority_sum = 0
    rucks = process_input(filename)

    for ruck in rucks:
        common_item = list(set(ruck[0]) & set(ruck[1]))

        if common_item[0].isupper():
            priority_sum += ord(common_item[0]) - ord('A') + 27
        else:
            priority_sum += ord(common_item[0]) - ord('a') + 1

    return priority_sum


def part_two(filename: str):
    pass


if __name__ == "__main__":
    input_file = "./input.txt"
    print(part_one(input_file))
    print(part_two(input_file))
