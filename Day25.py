DAY = 25
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
    INPUT = list(map(list, lines))

def part1():
    count = 0
    width = len(INPUT[0])
    height = len(INPUT)
    current_step = INPUT
    while True:
        east_step = [['.']*width for _ in range(height)]
        for x in range(width):
            for y in range(height):
                if current_step[y][x] == 'v':
                    east_step[y][x] = 'v'
                if current_step[y][x] == '>':
                    new_x = (x+1) % width
                    if current_step[y][new_x] == '.':
                        east_step[y][new_x] = '>'
                    else:
                        east_step[y][x] = '>'
        
        south_step = [['.']*width for _ in range(height)]
        for x in range(width):
            for y in range(height):
                if east_step[y][x] == '>':
                    south_step[y][x] = '>'
                if east_step[y][x] == 'v':
                    new_y = (y+1) % height
                    if east_step[new_y][x] == '.':
                        south_step[new_y][x] = 'v'
                    else:
                        south_step[y][x] = 'v'
        
        count += 1
        if south_step == current_step:
            return count
        current_step = south_step

def part2():
    return 'Merry Christmas!~!'

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()