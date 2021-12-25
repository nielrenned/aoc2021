DAY = 3
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
        INPUT.append(list(line))

def part1():
    num_bits = len(INPUT[0])
    counts = [0] * num_bits
    for bitset in INPUT:
        for i in range(num_bits):
            counts[i] += 1 if bitset[i] == '1' else -1
    # gamma_bits = [1 if x > 0 else 0 for x in counts]
    # epsilon_bits = [0 if x > 0 else 1 for x in counts]
    gamma = 0
    epsilon = 0
    for x in counts:
        gamma *= 2
        epsilon *= 2
        if x > 0:
            gamma += 1
        else:
            epsilon += 1
    return gamma * epsilon

def part2():
    num_bits = len(INPUT[0])
    
    o2_rating_bitsets = INPUT[:]
    for i in range(num_bits):
        num_ones = 0
        for bitset in o2_rating_bitsets:
            if bitset[i] == '1':
                num_ones += 1
        num_zeroes = len(o2_rating_bitsets) - num_ones
        if num_ones >= num_zeroes:
            o2_rating_bitsets = list(filter(lambda _: _[i] == '1', o2_rating_bitsets))
        else:
            o2_rating_bitsets = list(filter(lambda _: _[i] == '0', o2_rating_bitsets))
        if len(o2_rating_bitsets) == 1:
            break
    o2_rating_bits = o2_rating_bitsets[0]
    o2_rating = 0
    for bit in o2_rating_bits:
        o2_rating *= 2
        o2_rating += int(bit)
    
    co2_rating_bitsets = INPUT[:]
    for i in range(num_bits):
        num_ones = 0
        for bitset in co2_rating_bitsets:
            if bitset[i] == '1':
                num_ones += 1
        num_zeroes = len(co2_rating_bitsets) - num_ones
        if num_ones < num_zeroes:
            co2_rating_bitsets = list(filter(lambda _: _[i] == '1', co2_rating_bitsets))
        else:
            co2_rating_bitsets = list(filter(lambda _: _[i] == '0', co2_rating_bitsets))
        if len(co2_rating_bitsets) == 1:
            break
    co2_rating_bits = co2_rating_bitsets[0]
    co2_rating = 0
    for bit in co2_rating_bits:
        co2_rating *= 2
        co2_rating += int(bit)
    
    return o2_rating * co2_rating

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()