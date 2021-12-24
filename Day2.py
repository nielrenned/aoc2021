DAY = 2
RAW_INPUT = None
INPUT = None

def load_input(use_test_input=False):
    global RAW_INPUT
    path = f'inputs/day{DAY}.txt'
    if use_test_input:
        path = f'inputs/day{DAY}_test.txt'
    with open(path) as f:
        RAW_INPUT = f.read()

def parse_input():
    global INPUT
    INPUT = []
    for line in RAW_INPUT.split('\n')[:-1]:
        direction, amount = line.split()
        amount = int(amount)
        INPUT.append((direction, amount))

def part1():
    horiz = 0
    depth = 0
    for direction, amount in INPUT:
        if direction == 'forward':
            horiz += amount
        elif direction == 'down':
            depth += amount
        elif direction == 'up':
            depth -= amount
    return horiz * depth

def part2():
    horiz = 0
    depth = 0
    aim = 0
    for direction, amount in INPUT:
        if direction == 'forward':
            horiz += amount
            depth += aim * amount
        elif direction == 'down':
            aim += amount
        elif direction == 'up':
            aim -= amount
    return horiz * depth

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()