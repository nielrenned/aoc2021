DAY = 5
RAW_INPUT = None
INPUT = None

from collections import defaultdict

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
        start, end = line.split(' -> ')
        x1,y1 = map(int, start.split(','))
        x2,y2 = map(int, end.split(','))
        INPUT.append(((x1, y1), (x2, y2)))

def part1():
    points = defaultdict(int)
    for (x1, y1), (x2, y2) in INPUT:
        if x1 == x2:
            y1, y2 = sorted((y1, y2))
            for y in range(y1, y2+1):
                points[(x1, y)] += 1
        elif y1 == y2:
            x1, x2 = sorted((x1, x2))
            for x in range(x1, x2+1):
                points[(x, y1)] += 1
    count = 0
    for p in points:
        if points[p] > 1:
            count += 1
    return count

def part2():
    points = defaultdict(int)
    for (x1, y1), (x2, y2) in INPUT:
        delta_x = x2 - x1
        if delta_x > 0:
            delta_x = 1
        elif delta_x < 0:
            delta_x = -1
        
        delta_y = y2 - y1
        if delta_y > 0:
            delta_y = 1
        elif delta_y < 0:
            delta_y = -1
        
        start = [x1, y1]
        end = [x2, y2]
        while start != end:
            points[tuple(start)] += 1
            start[0] += delta_x
            start[1] += delta_y
        points[tuple(end)] += 1
    count = 0
    for p in points:
        if points[p] > 1:
            count += 1
    return count

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()