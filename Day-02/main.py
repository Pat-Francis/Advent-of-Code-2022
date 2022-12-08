def process_input(file: str):
    with open(file) as f:
        lines = f.read().splitlines()

        return lines

# win: 6, draw: 3, loss: 0
# A & X: Rock - 1 point
# B & Y: Paper - 2 points
# C & Z: Scissors - 3 points

# map_one
# A X - Draw - 1 + 3 = 4
# A Y - Win  - 2 + 6 = 8
# A Z - Loss - 3 + 0 = 3
# B X - Loss - 1 + 0 = 1
# B Y - Draw - 2 + 3 = 5
# B Z - Win  - 3 + 6 = 9
# C X - Win  - 1 + 6 = 7
# C Y - Loss - 2 + 0 = 2
# C Z - Draw - 3 + 3 = 6


map_one = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}


def part_one(filename: str):
    hands = process_input(filename)
    score = 0

    for hand in hands:
        score += map_one[hand]

    return score


# map_two
# X = Lose, Y = Draw, z = Win
# A X - Lose - 3 + 0 = 3
# A Y - Draw - 1 + 3 = 4
# A Z - Win  - 2 + 6 = 8
# B X - Loss - 1 + 0 = 1
# B Y - Draw - 2 + 3 = 5
# B Z - Win  - 3 + 6 = 9
# C X - Loss - 2 + 0 = 2
# C Y - Draw - 3 + 3 = 6
# C Z - Win  - 1 + 6 = 7

map_two = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}


def part_two(filename: str):
    hands = process_input(filename)
    score = 0

    for hand in hands:
        score += map_two[hand]

    return score


if __name__ == "__main__":
    input_file = "./input.txt"
    print(part_one(input_file))
    print(part_two(input_file))
