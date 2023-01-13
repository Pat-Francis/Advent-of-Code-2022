def process_input(file: str):
    with open(file) as f:
        input_data = f.read().splitlines()
    current_dir = ""
    dir_structure = {"/": {"parent_dir": "/", "child_dir": [], "files": {}}}

    for line in input_data:
        parts = line.split(" ")
        if parts[0] == "$":
            if parts[1] == "ls":
                pass
            else:
                if parts[2] == "..":
                    current_dir = dir_structure[current_dir].get("parent_dir")
                else:
                    parent_dir = current_dir
                    current_dir += parts[2]

                    if current_dir not in dir_structure:
                        dir_structure.update({current_dir: {"parent_dir": parent_dir, "child_dir": [], "files": {}}})

        elif parts[0] == "dir":
            dir_structure[current_dir]["child_dir"].append(f"{current_dir}{parts[1]}")
        else:
            dir_structure[current_dir]["files"].update({parts[1]: int(parts[0])})

    return dir_structure


def dir_size(dir_dict, directory):
    total_size = 0

    # Add direct files
    total_size += sum(dir_dict[directory]['files'].values())

    # Add indirect files
    for sub_dir in dir_dict[directory]['child_dir']:
        total_size += dir_size(dir_dict, sub_dir)

    return total_size


def part_one(filename: str):
    data_dict = process_input(filename)
    dir_sizes = {}

    for k, _ in data_dict.items():
        total_size = dir_size(data_dict, k)

        if total_size < 100000:
            dir_sizes[k] = total_size

    return sum(dir_sizes.values())


def part_two(filename: str):
    pass


if __name__ == "__main__":
    input_file = "./input.txt"
    print(part_one(input_file))
    print(part_two(input_file))
