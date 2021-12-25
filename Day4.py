DAY = 4
RAW_INPUT = None
INPUT = None

import copy

def load_input(use_test_input=False):
    global RAW_INPUT
    path = f'inputs/day{DAY}.txt'
    if use_test_input:
        path = f'inputs/day{DAY}_test.txt'
    with open(path) as f:
        RAW_INPUT = f.read()

def parse_input():
    global INPUT
    lines = list(filter(lambda _: len(_) > 0, RAW_INPUT.split('\n')))
    draws = list(map(int, lines[0].split(',')))
    boards = []
    for i in range(1, len(lines)-1, 5):
        board = []
        for line in lines[i:i+5]:
            board.append(list(map(int, line.split())))
        boards.append(board)
    INPUT = (draws, boards)

def part1():
    draws, boards = INPUT
    boards = copy.deepcopy(boards)
    winning_board = None
    done = False
    for draw in draws:
        for board in boards:
            for line in board:
                for i in range(5):
                    if line[i] == draw:
                        line[i] = -1
            # check rows
            board_won = False
            for row in board:
                won = True
                for cell in row:
                    if cell != -1:
                        won = False
                        break
                if won:
                    board_won = True
                    break
            
            for i in range(5):
                col = [row[i] for row in board]
                won = True
                for cell in col:
                    if cell != -1:
                        won = False
                        break
                if won:
                    board_won = True
                    break
            
            if board_won:
                winning_board = board
                done = True
                break
        if done:
            break
    total = 0
    for row in winning_board:
        for x in row:
            if x != -1:
                total += x
    return total * draw

def part2():
    draws, boards = INPUT
    boards = copy.deepcopy(boards)
    won_indices = []
    for draw in draws:
        for i in range(len(boards)):
            if i in won_indices:
                continue
            board = boards[i]
            for line in board:
                for j in range(5):
                    if line[j] == draw:
                        line[j] = -1
            # check rows
            board_won = False
            for row in board:
                won = True
                for cell in row:
                    if cell != -1:
                        won = False
                        break
                if won:
                    board_won = True
                    break
            
            for j in range(5):
                col = [row[j] for row in board]
                won = True
                for cell in col:
                    if cell != -1:
                        won = False
                        break
                if won or board_won:
                    board_won = True
                    break
            
            if board_won:
                won_indices.append(i)
        if len(won_indices) == len(boards):
            break
    last_board = boards[won_indices[-1]]
    total = 0
    for row in last_board:
        for x in row:
            if x != -1:
                total += x
    return total * draw

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()