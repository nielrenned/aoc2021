DAY = 22
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
    for line in RAW_INPUT.split('\n')[:-1]:
        instr = None
        if line.startswith('on'):
            instr = 'on'
        elif line.startswith('off'):
            instr = 'off'
        x_block, y_block, z_block = line[len(instr)+1:].split(',')
        x_coords = tuple(map(int, x_block[2:].split('..')))
        y_coords = tuple(map(int, y_block[2:].split('..')))
        z_coords = tuple(map(int, z_block[2:].split('..')))
        INPUT.append((instr, (x_coords, y_coords, z_coords)))

from collections import defaultdict

def part1():
    reactor = defaultdict(int)
    for instr, ((x0, x1), (y0, y1), (z0, z1)) in INPUT:
        new_state = 1 if instr == 'on' else 0
        for x in range(max(x0, -50), min(x1, 50)+1):
            for y in range(max(y0, -50), min(y1, 50)+1):
                for z in range(max(z0, -50), min(z1, 50)+1):
                    reactor[(x,y,z)] = new_state
    count = 0
    for x in range(-50, 50+1):
        for y in range(-50, 50+1):
            for z in range(-50, 50+1):
                if reactor[(x,y,z)] == 1:
                    count += 1
    return count

def regions_disjoint(region1, region2):
    (x0, x1), (y0, y1), (z0, z1) = region1
    (X0, X1), (Y0, Y1), (Z0, Z1) = region2
    return (X0 > x1 or x0 > X1 or Y0 > y1 or y0 > Y1 or z0 > Z1 or Z0 > z1)

def region_contains(larger, smaller):
    (x0, x1), (y0, y1), (z0, z1) = larger
    (X0, X1), (Y0, Y1), (Z0, Z1) = smaller
    return ((x0 <= X0 and X1 <= x1) and (y0 <= Y0 and Y1 <= y1) and (z0 <= Z0 and Z1 <= z1))

def get_intersection(region1, region2):
    if regions_disjoint(region1, region2):
        return None
    
    (x0, x1), (y0, y1), (z0, z1) = region1
    (X0, X1), (Y0, Y1), (Z0, Z1) = region2
    
    return ((max(x0, X0), min(x1, X1)), (max(y0, Y0), min(y1, Y1)), (max(z0, Z0), min(z1, Z1)))

def region_size(region):
    if region is None:
        return 0
    (x0, x1), (y0, y1), (z0, z1) = region
    return (x1-x0+1)*(y1-y0+1)*(z1-z0+1)

def subtract_regions(region1, region2):
    if regions_disjoint(region1, region2):
        return [region1]

def part2():
    q = []
    

def main():
    load_input(True)
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()