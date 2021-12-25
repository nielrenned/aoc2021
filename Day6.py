DAY = 6
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
    INPUT = list(map(int, RAW_INPUT.split(',')))

def part1():
    population = INPUT[:]
    for _ in range(80):
        new_fish = 0
        for i in range(len(population)):
            population[i] -= 1
            if population[i] < 0:
                population[i] = 6
                new_fish += 1
        population = population + [8]*new_fish
    return len(population)
            

def part2():
    initial_population = INPUT
    counts = {i: 0 for i in range(9)}
    for x in initial_population:
        counts[x] += 1
    for _ in range(256):
        new_counts = {i: counts[i+1] for i in range(8)}
        new_counts[6] += counts[0]
        new_counts[8] = counts[0]
        counts = new_counts
    return sum(counts[i] for i in range(9))

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()