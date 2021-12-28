DAY = 15
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
        INPUT.append(list(map(int, list(line))))


def get_adj_points(x,y):
    max_x = len(INPUT)-1
    max_y = len(INPUT[0]) - 1
    adj_points = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return list(filter(lambda p: 0 <= p[0] <= max_x and 0 <= p[1] <= max_y, adj_points))

from collections import defaultdict

# A* path-finding (Djikstra was too slow)
# The hueristic is taxicab distance of current point from bottom-right
def part1():
    max_x = len(INPUT[0])-1
    max_y = len(INPUT)-1
    
    open_set = {(0,0)}
    came_from = {}
    
    gScore = defaultdict(lambda: 1000000000)
    gScore[(0,0)] = 0
    
    fScore = defaultdict(lambda: 1000000000)
    fScore[(0,0)] = max_x + max_y
    
    while len(open_set) != 0:
        min_f_score = 1000000000
        current = None
        for v in open_set:
            if fScore[v] < min_f_score:
                min_f_score = fScore[v]
                current = v
        
        if current == (max_x, max_y):
            total = 0
            u = current
            while u != (0,0):
                total += INPUT[u[1]][u[0]]
                u = came_from[u]
            return total
        
        open_set.remove(current)
        
        x0,y0 = current
        for v in [(x0-1, y0), (x0+1, y0), (x0, y0-1), (x0, y0+1)]:
            x, y = v
            if 0 <= x <= max_x and 0 <= y <= max_y:
                tentative_g_score = gScore[current] + INPUT[y][x]
                if tentative_g_score < gScore[v]:
                    came_from[v] = current
                    gScore[v] = tentative_g_score
                    fScore[v] = tentative_g_score + (max_x - x) + (max_y - y)
                    open_set.add(v)

def part2():
    global INPUT
    len_x = len(INPUT[0])
    len_y = len(INPUT)
    
    new_map = [[0 for y in range(len_y*5)] for x in range(len_x*5)]
    for rx in range(5):
        for ry in range(5):
            for x in range(len_x):
                for y in range(len_y):
                    value = INPUT[y][x]+(rx+ry)
                    while value > 9:
                        value -= 9
                    new_map[len_y*ry+y][len_x*rx+x] = value
    
    INPUT = new_map
    
    return part1()

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()