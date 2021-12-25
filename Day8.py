DAY = 8
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
    for line in RAW_INPUT.split('\n')[:1]:
        signal, output = line.split(' | ')
        signal = tuple(signal.split())
        output = tuple(output.split())
        INPUT.append((signal, output))
        

def part1():
    total = 0
    for _, output in INPUT:
        for digit in output:
            if len(digit) == 2 or \
               len(digit) == 3 or \
               len(digit) == 4 or \
               len(digit) == 7:
                total += 1
    return total

def part2():
    pass

def main():
    load_input(True)
    parse_input()
    print('PART 1:', part1())
    # print('PART 2:', part2())

if __name__ == "__main__":
    main()