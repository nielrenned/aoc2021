DAY = 18
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
        INPUT.append(eval(line))

def add_numbers(left, right):
    return [left, right]

def magnitude(num):
    if type(num) is int:
        return num
    else:
        left, right = num
        return 3*magnitude(left) + 2*magnitude(right)

def explode(num):
    return num, False

def split(num):
    return num, False

def part1():
    result = INPUT[0]
    for next_num in INPUT[1:]:
        result = add_numbers(result, next_num)
        while True:
            did_split = False
            result, did_explode = explode(result)
            if not did_explode:
                result, did_split = split(result)
            if not (did_explode or did_split):
                break
    return magnitude(result)

def part2():
    pass

def main():
    load_input(True)
    parse_input()
    print('PART 1:', part1())
    # print('PART 2:', part2())

if __name__ == "__main__":
    main()