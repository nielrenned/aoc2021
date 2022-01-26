DAY = 21
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
    p1_line = RAW_INPUT.split('\n')[0]
    p2_line = RAW_INPUT.split('\n')[1]
    p1_pos = int(p1_line[p1_line.index(':')+1:])
    p2_pos = int(p2_line[p2_line.index(':')+1:])
    INPUT = (p1_pos-1, p2_pos-1)

def part1():
    positions = list(INPUT)
    scores = [0, 0]
    current_roll = 1
    roll_count = 0
    whose_turn = 0
    while scores[0] < 1000 and scores[1] < 1000:
        advancement = 0
        for _ in range(3):
            advancement += current_roll
            current_roll += 1
            if current_roll > 100:
                current_roll -= 100
            roll_count += 1
        positions[whose_turn] += advancement
        positions[whose_turn] %= 10
        scores[whose_turn] += positions[whose_turn] + 1
        whose_turn = 1 if whose_turn == 0 else 0
    return min(scores) * roll_count

from collections import defaultdict

def part2():
    p1_start, p2_start = INPUT
    state_counts = {((p1_start, p2_start), (0, 0), 0): 1}
    end_counts = [0,0]
    # state will be a tuple of the form ((p1_pos, p2_pos), (p1_score, p2_score), whose_turn)
    #print(state_counts)
    while True:
        new_state_counts = defaultdict(int)
        for state in state_counts:
            num_universes = state_counts[state]
            positions, scores, whose_turn = state
            # the list below is all possible sums of 3 rolls of a 3-sided die,
            # along with how many ways there are to combine three rolls to get that total
            for roll, num_combos in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
                new_pos = (positions[whose_turn] + roll) % 10
                new_score = scores[whose_turn] + new_pos + 1
                
                if new_score >= 21:
                    end_counts[whose_turn] += num_universes * num_combos
                    continue
                
                new_positions = list(positions)
                new_positions[whose_turn] = new_pos
                
                new_scores = list(scores)
                new_scores[whose_turn] = new_score
                
                new_state = (tuple(new_positions), tuple(new_scores), int(not whose_turn))
                new_state_counts[new_state] += num_universes * num_combos
        if len(new_state_counts) == 0:
            break
        state_counts = new_state_counts
    return max(end_counts)       

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()