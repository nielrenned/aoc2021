DAY = 19
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
    scanner = None
    for line in RAW_INPUT.split('\n'):
        if len(line) == 0:
            continue
        elif line.startswith('---'):
            if scanner is not None:
                INPUT.append(scanner)
            scanner = []
        else:
            scanner.append(tuple(map(int, line.split(','))))
    INPUT.append(scanner)

def part1():
    print(INPUT)

def part2():
    pass

def main():
    load_input(True)
    parse_input()
    print('PART 1:', part1())
    # print('PART 2:', part2())

if __name__ == "__main__":
    main()