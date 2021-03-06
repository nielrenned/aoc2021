DAY = 23
RAW_INPUT = None
INPUT = None

'''
  This problem was HARD for me. The first version I made _worked_ (I think), but was incredibly slow.
  A major optimization came from storing the map states as strings! This required a "clever"
  indexing function, but other than that, didn't change the code much.
  The largest problem for me though, was correctly calculating the reachable positions for any
  amphipod in the map. For a while they could teleport through each other, and move within the 
  hallway, neither of which should be possible. Once these issues were fixed, we were all set!
  
  The code is still pretty slow in my opinion. Some of that is Python's fault, I think. But most of
  it is probably on me. However, I don't really feel the need to opimize it. My solution is calculated
  in less than 10 seconds, which is plenty fast for me.
'''

def load_input(use_test_input=False):
    global RAW_INPUT
    path = f'inputs/day{DAY}.txt'
    if use_test_input:
        path = f'inputs/day{DAY}_test.txt'
    with open(path) as f:
        RAW_INPUT = f.read()

def parse_input():
    global INPUT
    lines = RAW_INPUT.split()
    row1 = lines[2].split('#')[3:7]
    row2 = lines[3].split('#')[1:5]
    INPUT = row1 + row2

HALLWAY_POSITIONS  = [(i,0) for i in range(11)]
SIDEROOM_POSITIONS = [(x, y) for y in (-1,-2,-3,-4) for x in (2,4,6,8)]
ALL_POSITIONS = HALLWAY_POSITIONS + SIDEROOM_POSITIONS

room_x_values = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

def print_state(state):
    s = '#############\n#' + state[:11] + '#\n###'
    for j in range(4):
        for i in range(4):
            s += state[11 + 4*j + i] + '#'
        if j == 0:
            s += '##\n  #'
        else:
            s += '\n  #'
    s += '########\n'
    print(s)

def travel_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1]) + abs(p2[1])

def sindex(x, y=None):
    if y is None:
        x,y = x
    if y == 0:
        return x
    else:
        return x // 2 + (6 - y*4)

def get_reachable_states(state):
    for start_pos in ALL_POSITIONS:
        amphipod_letter = state[sindex(start_pos)]
        if amphipod_letter == '.':
            continue
        
        room_x_value = room_x_values[amphipod_letter]
        
        if start_pos[0] == room_x_values[amphipod_letter]:
            is_in_correct_spot = True
            for y in range(start_pos[1], -5, -1):
                if state[sindex(start_pos[0], y)] != amphipod_letter:
                    is_in_correct_spot = False
                    break
            if is_in_correct_spot:
                continue
        
        for pos in get_valid_next_positions(state, start_pos):
            new_state = state[:]
            new_state = new_state[:sindex(pos)] + amphipod_letter + new_state[sindex(pos)+1:]
            new_state = new_state[:sindex(start_pos)] + '.' + new_state[sindex(start_pos)+1:]
            cost = costs[amphipod_letter] * travel_dist(start_pos, pos)
            yield (new_state, cost)

def get_valid_next_positions(state, start_pos):
    amphipod_letter = state[sindex(start_pos)]
    room_x_value = room_x_values[amphipod_letter]
    
    allowed_to_enter_desired_room = True
    for y in range(-4, 0):
        letter = state[sindex(room_x_value, y)]
        if letter != '.' and letter != amphipod_letter:
            allowed_to_enter_desired_room = False
            break
        
    # if we're in the hallway, we can move if we can
    # go to our desired room
    if start_pos[1] == 0 and not allowed_to_enter_desired_room:
        return set()
    
    # if we're not in the hallway, then try to leave the room
    x0, y0 = start_pos
    reachable_positions = set()
    
    # leave room
    # return {} if blocked
    while y0 < 0:
        y0 += 1
        if state[sindex(x0, y0)] != '.':
            return set()
    
    # walk left as far as possible
    while x0 > 0:
        x0 -= 1
        if state[sindex(x0, y0)] != '.':
            break
        if x0 != 2 and x0 != 4 and x0 != 6 and x0 != 8:
            reachable_positions.add((x0, y0))
    
    # walk right as far as possible
    x0 = start_pos[0]
    while x0 < 10:
        x0 += 1
        if state[sindex(x0, y0)] != '.':
            break
        if x0 != 2 and x0 != 4 and x0 != 6 and x0 != 8:
            reachable_positions.add((x0, y0))
    
    # try to enter desired room, if possible
    # and go to the lowest position
    good_y_value = -4
    for y in range(0, -5, -1):
        if state[sindex(room_x_value, y)] != '.':
            good_y_value = y+1
            break
    lowest_room_position = (room_x_value, good_y_value)
    
    if allowed_to_enter_desired_room and \
       ((room_x_value-1, 0) in reachable_positions or \
        (room_x_value+1, 0) in reachable_positions or \
        (room_x_value+1, 0) == start_pos or \
        (room_x_value-1, 0) == start_pos):
        
        reachable_positions.add(lowest_room_position)
    
    if start_pos[1] == 0:
        return reachable_positions & {lowest_room_position}
        
    return reachable_positions

def is_finished(state):
    return state == '...........ABCDABCDABCDABCD'

def finishing_heuristic(state):
    total = 0
    for pos in ALL_POSITIONS:
        amphipod_letter = state[sindex(pos)]
        if amphipod_letter == '.':
            continue
        room_x_value = room_x_values[amphipod_letter]
        dist_to_room = travel_dist(pos, (room_x_value, -1))
        if room_x_value == pos[0]:
            dist_to_room = 0
        total += dist_to_room * costs[amphipod_letter]
    return total

from collections import defaultdict
from heapq import *

def a_star(starting_state):
    open_set = [(finishing_heuristic(starting_state), starting_state)]
    heapify(open_set)
    
    came_from = {starting_state: None}
    
    g_score = defaultdict(lambda: 1000000)
    g_score[starting_state] = 0
    
    f_score = defaultdict(lambda: 1000000)
    f_score[starting_state] = finishing_heuristic(starting_state)
    
    while len(open_set) > 0:
        _, current = heappop(open_set)
        
        if is_finished(current):
            return g_score[current]
        
        for neighbor, d in get_reachable_states(current):
            tentative_g_score = g_score[current] + d
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                heur = finishing_heuristic(neighbor)
                f_score[neighbor] = tentative_g_score + heur
                heappush(open_set, (tentative_g_score + heur, neighbor))

def part1():    
    starting_state = '.' * 11 + ''.join(INPUT) + 'ABCDABCD'
    return a_star(starting_state)

def part2():
    starting_state = '.' * 11 + ''.join(INPUT[:4]) + 'DCBADBAC' + ''.join(INPUT[4:])
    return a_star(starting_state)

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()