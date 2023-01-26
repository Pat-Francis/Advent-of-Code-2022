import re
from math import gcd
from functools import reduce


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
        self.lcm = 0

    def inspect_items(self):
        ops = {'+': lambda x, y: x + y,
               '-': lambda x, y: x - y,
               '*': lambda x, y: x * y,
               '/': lambda x, y: x / y
               }

        for i, item in enumerate(self.items):
            # Operation
            if self.op[1] == 'old':
                self.items[i] = ops[self.op[0]](item, item)
            else:
                self.items[i] = ops[self.op[0]](item, int(self.op[1]))

    def calc_passes(self):
        for item in self.items:
            if item % self.test == 0:
                self.to_pass.append([self.if_true, item])
            else:
                self.to_pass.append([self.if_false, item])

            self.inspected += 1
        self.items.clear()

    def catch_item(self, passed_item):
        self.items.append(passed_item)


def lcm(arr):
    return reduce(lambda x, y: (x * y) // gcd(x, y), arr)


def part_one(filename: str):
    inspection_count = []
    monkey_data = process_input(filename)
    monkeys = [Monkey(monkey) for monkey in monkey_data]
    rounds = 20

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.inspect_items()

            # Update worry level
            for i, item in enumerate(monkey.items):
                monkey.items[i] //= 3

            monkey.calc_passes()

            for pass_to, item in monkey.to_pass:
                monkeys[pass_to].catch_item(item)

            monkey.to_pass.clear()

    for monkey in monkeys:
        inspection_count.append(monkey.inspected)

    inspect_counts = sorted(inspection_count)

    return inspect_counts[-1] * inspect_counts[-2]


def part_two(filename: str):
    inspection_count = []
    monkey_data = process_input(filename)
    monkeys = [Monkey(monkey) for monkey in monkey_data]
    monkey_test_lcm = lcm([monkey.test for monkey in monkeys])
    rounds = 10_000

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.inspect_items()

            # Update worry level
            for i, item in enumerate(monkey.items):
                monkey.items[i] = monkey.items[i] % monkey_test_lcm

            monkey.calc_passes()

            for pass_to, item in monkey.to_pass:
                monkeys[pass_to].catch_item(item)

            monkey.to_pass.clear()

    for monkey in monkeys:
        inspection_count.append(monkey.inspected)

    inspect_counts = sorted(inspection_count)

    return inspect_counts[-1] * inspect_counts[-2]


if __name__ == "__main__":
    input_file = "./input.txt"
    print(part_one(input_file))
    print(part_two(input_file))
