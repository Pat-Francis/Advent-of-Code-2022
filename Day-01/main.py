def process_input(file: str):
    with open(file) as f:
        elf_list = []
        elves = f.read().split("\n\n")

        for elf in elves:
            elf_calories = elf.split("\n")
            int_calories = list(map(int, elf_calories))
            elf_list.append(int_calories)

        return elf_list


def cals_per_elf(elf_list):
    cals_elf = []
    for elf in elf_list:
        cal_sum = sum([i for i in elf])
        cals_elf.append(cal_sum)

    return cals_elf


def part_one(filename: str):
    cals = process_input(filename)
    elves = cals_per_elf(cals)
    return max(elves)


def part_two(filename: str):
    cals = process_input(filename)
    elves = cals_per_elf(cals)

    return sum(sorted(elves)[-3:])


if __name__ == "__main__":
    input_file = "./input.txt"
    print(part_one(input_file))
    print(part_two(input_file))
