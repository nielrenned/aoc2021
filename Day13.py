DAY = 13
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
    dots = []
    instructions = []
    seen_blank = False
    for line in RAW_INPUT.split('\n')[:-1]:
        if line == '':
            seen_blank = True
            continue
        if not seen_blank:
            dots.append(tuple(map(int, line.split(','))))
        else:
            axis, value = line.split('=')
            instructions.append((axis[-1], int(value)))
    INPUT = (dots, instructions)

def part1():
    dots = INPUT[0]
    max_x = max(d[0] for d in dots)
    max_y = max(d[1] for d in dots)
    axis, value = INPUT[1][0]
    
    new_dots = set()
    if axis == 'x':
        for x,y in dots:
            if x > value:
                new_dots.add((max_x - x, y))
            else:
                new_dots.add((x, y))
    elif axis == 'y':
        for x,y in dots:
            if y > value:
                new_dots.add((x, max_y - y))
            else:
                new_dots.add((x, y))
    return len(new_dots)

def part2():
    dots = INPUT[0]
    max_x = max(d[0] for d in dots)
    max_y = max(d[1] for d in dots)
    
    for axis, value in INPUT[1]:
        new_dots = set()
        if axis == 'x':
            for x,y in dots:
                if x > value:
                    new_dots.add((max_x - x, y))
                else:
                    new_dots.add((x, y))
            max_x = value - 1
        elif axis == 'y':
            for x,y in dots:
                if y > value:
                    new_dots.add((x, max_y - y))
                else:
                    new_dots.add((x, y))
            max_y = value - 1
        dots = new_dots
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x,y) in new_dots:
                print('# ', end='')
            else:
                print('  ', end='')
        print()
    return '^^ SEE ABOVE ^^'

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()