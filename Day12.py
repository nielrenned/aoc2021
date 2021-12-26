DAY = 12
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
    INPUT = defaultdict(set)
    for line in RAW_INPUT.split():
        e1, e2 = line.split('-')
        INPUT[e1].add(e2)
        INPUT[e2].add(e1)

from queue import Queue

def part1():
    all_paths = set()
    new_paths = Queue()
    new_paths.put(['start'])
    while not new_paths.empty():
        path = new_paths.get()
        pos = path[-1]
        if pos == 'end':
            all_paths.add(tuple(path))
            continue
        for conn in INPUT[pos]:
            if (conn.islower() and conn not in path) or conn.isupper():
                new_path = path[:] + [conn]
                new_paths.put(new_path)
    return len(all_paths)

def part2():
    all_paths = set()
    new_paths = Queue()
    new_paths.put((['start'], False))
    while not new_paths.empty():
        path, duped_small = new_paths.get()
        pos = path[-1]
        if pos == 'end':
            all_paths.add(tuple(path))
            continue
        for conn in INPUT[pos]:
            if (conn.islower() and conn not in path) or conn.isupper():
                new_path = path[:] + [conn]
                new_paths.put((new_path, duped_small))
            elif not duped_small and conn != 'start' and conn != 'end':
                new_path = path[:] + [conn]
                new_paths.put((new_path, True))
    return len(all_paths)

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()