DAY = 23
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
    lines = RAW_INPUT.split()
    row1 = lines[2].split('#')[3:7]
    row2 = lines[3].split('#')[1:5]
    col1 = (row1[0], row2[0])
    col2 = (row1[1], row2[1])
    col3 = (row1[2], row2[2])
    col4 = (row1[3], row2[3])
    INPUT = (col1, col2, col3, col4)

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