DAY = 11
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
    for line in RAW_INPUT.split():
        INPUT.append(list(map(int, list(line))))

def get_adj_points(x,y):
    max_x = len(INPUT)-1
    max_y = len(INPUT[0]) - 1
    adj_points = [(x+i, y+j) for i in [1,0,-1] for j in [1,0,-1] if i != 0 or j != 0]
    return list(filter(lambda p: 0 <= p[0] <= max_x and 0 <= p[1] <= max_y, adj_points))

from itertools import product
import copy

def part1():
    max_x = len(INPUT)-1
    max_y = len(INPUT[0]) - 1
    octopi = copy.deepcopy(INPUT)
    num_flashes = 0
    for _ in range(100):
        flashed = True
        first_loop = True
        while flashed:
            flashed = False
            for x,y in product(range(max_x + 1), range(max_y + 1)):
                if first_loop:
                    octopi[x][y] += 1
                if octopi[x][y] <= 9:
                    continue
                flashed = True
                num_flashes += 1
                octopi[x][y] = -1
                for x0, y0 in get_adj_points(x,y):
                    if octopi[x0][y0] != -1:
                        octopi[x0][y0] += 1
            first_loop = False
        # replace -1's
        for x,y in product(range(max_x + 1), range(max_y + 1)):
            if octopi[x][y] == -1:
                octopi[x][y] = 0
    return num_flashes

def part2():
    max_x = len(INPUT)-1
    max_y = len(INPUT[0]) - 1
    octopi = copy.deepcopy(INPUT)
    step = 0
    while True:
        flashed = True
        first_loop = True
        while flashed:
            flashed = False
            for x,y in product(range(max_x + 1), range(max_y + 1)):
                if first_loop:
                    octopi[x][y] += 1
                if octopi[x][y] <= 9:
                    continue
                flashed = True
                octopi[x][y] = -1
                for x0, y0 in get_adj_points(x,y):
                    if octopi[x0][y0] != -1:
                        octopi[x0][y0] += 1
            first_loop = False
        # replace -1's
        for x,y in product(range(max_x + 1), range(max_y + 1)):
            if octopi[x][y] == -1:
                octopi[x][y] = 0
        step += 1
        # check all flashed
        for x,y in product(range(max_x + 1), range(max_y + 1)):
            if octopi[x][y] != 0:
                break
        else:
            return step

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()