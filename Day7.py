DAY = 7
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
    INPUT = list(map(int, RAW_INPUT.split(',')))

def part1():
    a = min(INPUT)
    b = max(INPUT)
    min_dist = 10000000000
    for i in range(a, b+1):
        total_dist = 0
        for x in INPUT:
            total_dist += abs(x-i)
        min_dist = min(total_dist, min_dist)
    return min_dist

def part2():
    a = min(INPUT)
    b = max(INPUT)
    min_dist = 10000000000
    for i in range(a, b+1):
        total_dist = 0
        for x in INPUT:
            n = abs(x-i)
            total_dist += n*(n+1)//2
        min_dist = min(total_dist, min_dist)
    return min_dist

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()