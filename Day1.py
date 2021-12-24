DAY = 1
RAW_INPUT = None
INPUT = None

def load_input(use_test_input=False):
    global DAY, RAW_INPUT
    path = f'inputs/day{DAY}.txt'
    if use_test_input:
        path = f'inputs/day{DAY}_test.txt'
    with open(path) as f:
        RAW_INPUT = f.read()

def parse_input():
    global RAW_INPUT, INPUT
    INPUT = list(map(int, RAW_INPUT.split('\n')[:-1]))

def part1():
    global INPUT
    prev = INPUT[0]
    count = 0
    for depth in INPUT[1:]:
        if depth > prev:
            count += 1
        prev = depth
    return count

def part2():
    global INPUT
    pass

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    # print('PART 2:', part1())

if __name__ == "__main__":
    main()