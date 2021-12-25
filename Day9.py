DAY = 9
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

# x and y are flipped, but whatever
def part1():
    max_x = len(INPUT)-1
    max_y = len(INPUT[0]) - 1
    total_risk = 0
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            height = INPUT[x][y]
            if x > 0 and INPUT[x-1][y] <= height:
                continue
            elif x < max_x and INPUT[x+1][y] <= height:
                continue
            elif y > 0 and INPUT[x][y-1] <= height:
                continue
            elif y < max_y and INPUT[x][y+1] <= height:
                continue
            total_risk += height + 1
    return total_risk

def basin_finder(start_loc, basin):
    max_x = len(INPUT)-1
    max_y = len(INPUT[0]) - 1
    x, y = start_loc
    height = INPUT[x][y]
    if height == 9:
        return
    basin.add((x,y))
    if x > 0 and (x-1, y) not in basin:
        basin_finder((x-1, y), basin)
    if x < max_x and (x+1, y) not in basin:
        basin_finder((x+1, y), basin)
    if y > 0 and (x, y-1) not in basin:
        basin_finder((x, y-1), basin)
    if y < max_y and (x, y+1) not in basin:
        basin_finder((x, y+1), basin)

def part2():
    max_x = len(INPUT)-1
    max_y = len(INPUT[0]) - 1
    sizes = []
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            height = INPUT[x][y]
            if x > 0 and INPUT[x-1][y] <= height:
                continue
            elif x < max_x and INPUT[x+1][y] <= height:
                continue
            elif y > 0 and INPUT[x][y-1] <= height:
                continue
            elif y < max_y and INPUT[x][y+1] <= height:
                continue
            # find basin
            basin = {(x,y)}
            basin_finder((x,y), basin)
            sizes.append(len(basin))
    sizes = sorted(sizes)
    return sizes[-1] * sizes[-2] * sizes[-3]

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()