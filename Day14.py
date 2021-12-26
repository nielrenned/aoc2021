DAY = 14
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
    lines = list(RAW_INPUT.split('\n')[:-1])
    start = lines[0]
    rules = {}
    for line in lines[2:]:
        pair, insertion = line.split(' -> ')
        rules[pair] = insertion
    INPUT = (start, rules)

from collections import Counter

def part1():
    current_polymer, rules = INPUT
    for _ in range(10):
        new_polymer = current_polymer[0]
        for i in range(len(current_polymer)-1):
            pair = current_polymer[i:i+2]
            if pair in rules:
                new_polymer += rules[pair]
            new_polymer += pair[-1]
        current_polymer = new_polymer
    count = Counter(current_polymer)
    return count.most_common()[0][1] - count.most_common()[-1][1]

from collections import defaultdict

def part2():
    starting_polymer, rules = INPUT
    counts = defaultdict(int)
    pairs = defaultdict(int)
    for i in range(len(starting_polymer) - 1):
        pairs[starting_polymer[i:i+2]] += 1
        counts[starting_polymer[i]] += 1
    counts[starting_polymer[-1]] += 1
    
    for _ in range(40):
        new_pairs = pairs.copy()
        for pair in pairs:
            if pair in rules:
                insertion = rules[pair]
                count = pairs[pair]
                counts[insertion] += count
                new_pairs[pair[0] + insertion] += count
                new_pairs[insertion + pair[1]] += count
                new_pairs[pair] -= count
        pairs = new_pairs
    
    commonality = sorted(counts[elem] for elem in counts)
    return commonality[-1] - commonality[0]

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()