def process_input(file: str):
    with open(file) as f:
        return f.read().splitlines()


def part_one(filename: str):
    input_data = process_input(filename)
    current_dir = ""
    dir_structure = {"/": {"child_dir": [], "files": {}}}

    for line in input_data:
        parts = line.split(" ")
        if parts[0] == "$":
            if parts[1] == "ls":
                pass
            else:
                if parts[2] == "..":
                    current_dir = current_dir[:-1]
                else:
                    current_dir += parts[2]
                    if current_dir not in dir_structure:
                        dir_structure.update({current_dir: {"child_dir": [], "files": {}}})
        elif parts[0] == "dir":
            dir_structure[current_dir]["child_dir"].append(parts[1])
        else:
            dir_structure[current_dir]["files"].update({parts[1]: int(parts[0])})

    for k, v in dir_structure.items():
        print(k, v)


def part_two(filename: str):
    pass


if __name__ == "__main__":
    input_file = "./test_input.txt"
    print(part_one(input_file))
    print(part_two(input_file))
