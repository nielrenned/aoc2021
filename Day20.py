DAY = 20
RAW_INPUT = None
INPUT = None

def load_input(use_test_input=False):
    global RAW_INPUT
    path = f'inputs/day{DAY}.txt'
    if use_test_input:
        path = f'inputs/day{DAY}_test.txt'
    with open(path) as f:
        RAW_INPUT = f.read()

from collections import defaultdict

def parse_input():
    global INPUT
    lines = RAW_INPUT.split()
    algo = lines[0]
    starting_image_lines = list(map(list, lines[1:]))
    starting_image = defaultdict(int)
    for x in range(len(starting_image_lines[0])):
        for y in range(len(starting_image_lines)):
            if starting_image_lines[y][x] == '#':
                starting_image[(x,y)] = 1
    INPUT = (algo, starting_image)

def get_dimensions(image):
    points = image.keys()
    min_x = min(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)
    return (min_x, max_x, min_y, max_y)

def print_image(image):
    min_x, max_x, min_y, max_y = get_dimensions(image)
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if image[(x,y)] == 1:
                print('#', end='')
            else:
                print('.', end='')
        print()

def part1():
    algo, current_image = INPUT
    current_bg = 0
    for _ in range(2):
        min_x, max_x, min_y, max_y = get_dimensions(current_image)
        min_x = min_x - 1
        max_x = max_x + 1
        min_y = min_y - 1
        max_y = max_y + 1
        
        new_image = None
        if algo[current_bg] == '#':
            new_image = defaultdict(lambda: 1)
            current_bg = 511
        else:
            new_image = defaultdict(lambda: 0)
            current_bg = 0
        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):
                c = current_image
                bin_str =  str(c[(x-1, y-1)]) + str(c[(x, y-1)]) + str(c[(x+1, y-1)])
                bin_str += str(c[(x-1, y)])   + str(c[(x, y)])   + str(c[(x+1, y)])
                bin_str += str(c[(x-1, y+1)]) + str(c[(x, y+1)]) + str(c[(x+1, y+1)])
                index = int(bin_str, base=2)
                if algo[index] == '#':
                    new_image[(x,y)] = 1
                else:
                    new_image[(x,y)] = 0
        current_image = new_image
    total = 0
    for p in current_image:
        if current_image[p] == 1:
            total += 1
    return total

def part2():
    algo, current_image = INPUT
    current_bg = 0
    for _ in range(50):
        min_x, max_x, min_y, max_y = get_dimensions(current_image)
        min_x = min_x - 1
        max_x = max_x + 1
        min_y = min_y - 1
        max_y = max_y + 1
        
        new_image = None
        if algo[current_bg] == '#':
            new_image = defaultdict(lambda: 1)
            current_bg = 511
        else:
            new_image = defaultdict(lambda: 0)
            current_bg = 0
        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):
                c = current_image
                bin_str =  str(c[(x-1, y-1)]) + str(c[(x, y-1)]) + str(c[(x+1, y-1)])
                bin_str += str(c[(x-1, y)])   + str(c[(x, y)])   + str(c[(x+1, y)])
                bin_str += str(c[(x-1, y+1)]) + str(c[(x, y+1)]) + str(c[(x+1, y+1)])
                index = int(bin_str, base=2)
                if algo[index] == '#':
                    new_image[(x,y)] = 1
                else:
                    new_image[(x,y)] = 0
        current_image = new_image
    total = 0
    for p in current_image:
        if current_image[p] == 1:
            total += 1
    return total

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()