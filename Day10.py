DAY = 10
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
    INPUT = RAW_INPUT.split()

OPEN_CHARS = '[{(<'
CLOSE_CHARS = {'[': ']', '{': '}', '(': ')', '<': '>'}
SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}
def part1():
    score = 0
    for line in INPUT:
        stack = []
        for c in line:
            if c in OPEN_CHARS:
                stack.append(c)
            else:
                open_char = stack.pop()
                match = CLOSE_CHARS[open_char]
                if c != match:
                    score += SCORES[c]
    return score

SCORES = {')': 1, ']': 2, '}': 3, '>': 4}
def part2():
    scores = []
    for line in INPUT:
        stack = []
        corrupted = False
        for c in line:
            if c in OPEN_CHARS:
                stack.append(c)
            else:
                open_char = stack.pop()
                match = CLOSE_CHARS[open_char]
                if c != match:
                    corrupted = True
                    break
        if not corrupted:
            score = 0
            while len(stack) > 0:
                close_char = CLOSE_CHARS[stack.pop()]
                score *= 5
                score += SCORES[close_char]
            scores.append(score)
    scores = sorted(scores)
    return scores[(len(scores)-1) // 2]

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()