import re


def process_input(file: str):
    with open(file) as f:
        input_data = f.read().split("\n\n")

    processed_data = []

    for i in input_data:
        processed_data.append(i.splitlines())

    return processed_data


class Monkey:
    def __init__(self, monkey_info: list[str]):
        self.id = int(monkey_info[0][-2])
        self.items = [int(item) for item in re.findall(r'\d+', monkey_info[1])]
        self.op = re.split(r'\s', re.findall(r'(?:= old\s)(.+)', monkey_info[2])[0])
        self.test = int(re.findall(r'\d+', monkey_info[3])[0])
        self.if_true = int(monkey_info[4][-1])
        self.if_false = int(monkey_info[5][-1])
        self.inspected = 0
        self.to_pass = []

    def inspect_items(self):
        ops = {'+': lambda x, y: x + y,
               '-': lambda x, y: x - y,
               '*': lambda x, y: x * y,
               '/': lambda x, y: x / y
               }

        for item in self.items:
            # Operation
            if self.op[1] == 'old':
                item = ops[self.op[0]](item, item)
            else:
                item = ops[self.op[0]](item, int(self.op[1]))

            item //= 3

            # Test
            if item % self.test == 0:
                self.to_pass.append([self.if_true, item])
            else:
                self.to_pass.append([self.if_false, item])

            self.inspected += 1
        self.items.clear()

    def catch_item(self, passed_item):
        self.items.append(passed_item)


def part_one(filename: str):
    monkey_data = process_input(filename)
    monkeys = [Monkey(monkey) for monkey in monkey_data]
    inspection_count = []

    for _ in range(0, 20):
        for monk in monkeys:
            monk.inspect_items()
            for pass_to, item in monk.to_pass:
                monkeys[pass_to].catch_item(item)
            monk.to_pass.clear()

    for monk in monkeys:
        inspection_count.append(monk.inspected)

    sorted_inspec = sorted(inspection_count)

    return sorted_inspec[-1] * sorted_inspec[-2]


def part_two(filename: str):
    pass


if __name__ == "__main__":
    input_file = "./input.txt"
    print(part_one(input_file))
    print(part_two(input_file))
