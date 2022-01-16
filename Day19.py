DAY = 19
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
    scanner = None
    for line in RAW_INPUT.split('\n'):
        if len(line) == 0:
            continue
        elif line.startswith('---'):
            if scanner is not None:
                INPUT.append(scanner)
            scanner = []
        else:
            scanner.append(tuple(map(int, line.split(','))))
    INPUT.append(scanner)

def add_coords(c1, c2):
    return tuple(c1[i] + c2[i] for i in range(3))

def subtract_coords(c1, c2):
    return tuple(c1[i] - c2[i] for i in range(3))

def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

import numpy as np

def get_rotation_matrices():
    matrices = []
    for x_dir in (1, -1, 2, -2, 3, -3):
        y_dir = None
        z_dir = None
        if abs(x_dir) == 1:
            y_dir = 2
            z_dir = 3 if x_dir > 0 else -3
        elif abs(x_dir) == 2:
            y_dir = 3
            z_dir = 1 if x_dir > 0 else -1
        else:
            y_dir = 1
            z_dir = 2 if x_dir > 0 else -2
        for _ in range(4):
            matrix = [[0,0,0], [0,0,0], [0,0,0]]
            matrix[0][abs(x_dir)-1] = sign(x_dir)
            matrix[1][abs(y_dir)-1] = sign(y_dir)
            matrix[2][abs(z_dir)-1] = sign(z_dir)
            y_dir, z_dir = z_dir, -y_dir
            matrices.append(np.array(matrix))
    return matrices

def get_rotation(scanner, matrix):
    new_scanner = []
    for coord in scanner:
        new_scanner.append(tuple(np.matmul(matrix, coord)))
    return new_scanner

from collections import Counter, defaultdict
from queue import Queue
from itertools import product
from tqdm import tqdm # progress bar

ABSOLUTE_COORDS = {}

def part1():
    global ABSOLUTE_COORDS
    # find all connections
    rot_matrices = get_rotation_matrices()
    connections = defaultdict(list)
    for i,j in tqdm(list(product(range(len(INPUT)), repeat=2))):
        if i == j:
            continue
        scanner_i = INPUT[i]
        scanner_j = INPUT[j]
        for rot in rot_matrices:
            rotated_scanner = get_rotation(scanner_j, rot)
            counter = Counter()
            for c1 in scanner_i:
                for c2 in rotated_scanner:
                    counter.update([subtract_coords(c1, c2)])
            offset, count = counter.most_common(1)[0]
            if count >= 12:
                connections[i].append((j, offset, rot))
                break
    
    # build pathways
    points = set()
    added = set()
    q = Queue()
    q.put((0, (0,0,0), get_rotation_matrices()[0]))
    while not q.empty():
        index, base, rot = q.get()
        ABSOLUTE_COORDS[index] = base
        for coord in get_rotation(INPUT[index], rot):
            points.add(add_coords(base, coord))
        added.add(index)
        
        for conn, offset, next_rot in connections[index]:
            if conn not in added:
                rotated_offset = tuple(np.matmul(rot, offset))
                q.put((conn, add_coords(base, rotated_offset), np.matmul(rot, next_rot)))
    return len(points)
   
def part2():
    max_dist = 0
    for i in range(len(INPUT)):
        for j in range(len(INPUT)):
            coord_i = ABSOLUTE_COORDS[i]
            coord_j = ABSOLUTE_COORDS[j]
            diff = subtract_coords(coord_i, coord_j)
            dist = sum(map(abs, diff))
            max_dist = max(max_dist, dist)
    return max_dist

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()