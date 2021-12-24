DAY = 0
RAW_INPUT = None
INPUT = None

def load_input():
    global DAY, RAW_INPUT
    with open(f'inputs/day{DAY}.txt') as f:
        RAW_INPUT = f.read()

def parse_input():
    global RAW_INPUT, INPUT
    pass

def part1():
    global INPUT
    pass

def part2():
    global INPUT
    pass

def main():
    load_input()
    parse_input()
    part1()
    # part2()

if __name__ == "__main__":
    main()