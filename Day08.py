DAY = 8
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
        signal, output = line.split(' | ')
        signal = tuple(signal.split())
        output = tuple(output.split())
        INPUT.append((signal, output))

def part1():
    total = 0
    for _, output in INPUT:
        for digit in output:
            if len(digit) == 2 or \
               len(digit) == 3 or \
               len(digit) == 4 or \
               len(digit) == 7:
                total += 1
    return total

from functools import reduce

'''
  This map came from a by-hand analysis of the 7-segment display configuration. We
  can figure out the wire mappings one-by-one as seen below, just by logic.
'''
def part2():
    total = 0
    for signal, output in INPUT:
        sets = list(map(set, sorted(signal, key=len)))
        
        segs = {}
        segs['a'] = sets[1] - sets[0]
        segs['d'] = sets[3] & sets[4] & sets[5] & (sets[2] - sets[0])
        segs['b'] = sets[2] - segs['d'] - sets[0]
        segs['g'] = (sets[3] & sets[4] & sets[5]) - segs['a'] - segs['d']
        segs['f'] = (sets[6] & sets[7] & sets[8]) -  segs['a'] - segs['b'] - segs['g']
        segs['c'] = sets[0] - segs['f']
        segs['e'] = sets[-1] - segs['a'] - segs['b'] - segs['c'] - segs['d'] - segs['f'] - segs['g']
        
        digits = {}
        digits[frozenset(reduce(lambda x, y: x | y, (segs[x] for x in 'abcefg')))]  = '0'
        digits[frozenset(reduce(lambda x, y: x | y, (segs[x] for x in 'cf')))]      = '1'
        digits[frozenset(reduce(lambda x, y: x | y, (segs[x] for x in 'acdeg')))]   = '2'
        digits[frozenset(reduce(lambda x, y: x | y, (segs[x] for x in 'acdfg')))]   = '3'
        digits[frozenset(reduce(lambda x, y: x | y, (segs[x] for x in 'bcdf')))]    = '4'
        digits[frozenset(reduce(lambda x, y: x | y, (segs[x] for x in 'abdfg')))]   = '5'
        digits[frozenset(reduce(lambda x, y: x | y, (segs[x] for x in 'abdefg')))]  = '6'
        digits[frozenset(reduce(lambda x, y: x | y, (segs[x] for x in 'acf')))]     = '7'
        digits[frozenset(reduce(lambda x, y: x | y, (segs[x] for x in 'abcdefg')))] = '8'
        digits[frozenset(reduce(lambda x, y: x | y, (segs[x] for x in 'abcdfg')))]  = '9'
        
        total += int(reduce(lambda x, y: x+y, (digits[frozenset(x)] for x in output)))
    return total


def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()