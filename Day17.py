DAY = 17
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
    
    i0 = RAW_INPUT.find('=')
    i1 = RAW_INPUT.find('..')
    x_min = int(RAW_INPUT[i0+1:i1])
    
    i0 = i1+1
    i1 = RAW_INPUT.find(',')
    x_max = int(RAW_INPUT[i0+1:i1])
    
    i0 = RAW_INPUT.find('=', i1)
    i1 = RAW_INPUT.find('..', i0)
    y_min = int(RAW_INPUT[i0+1:i1])
    
    i0 = i1+1
    i1 = RAW_INPUT.find('\n')
    y_max = int(RAW_INPUT[i0+1:i1])
    
    INPUT = [x_min, x_max, y_min, y_max]

MADE_IT_COUNT = 0

def part1():
    global MADE_IT_COUNT
    x_min, x_max, y_min, y_max = INPUT
    
    valid_x_velocities = []
    for start_vel in range(x_max+1):
        x_pos = 0
        x_vel = start_vel
        while x_vel > 0:
            x_pos += x_vel
            if x_min <= x_pos <= x_max:
                valid_x_velocities.append(start_vel)
                break
            x_vel -= 1
    
    valid_y_velocities = []
    for start_vel in range(y_min, abs(y_min)+1):
        y_pos = 0
        y_vel = start_vel
        while y_pos >= y_min:
            y_pos += y_vel
            if y_min <= y_pos <= y_max:
                valid_y_velocities.append(start_vel)
                break
            y_vel -= 1
    
    overall_max_height = 0
    for x_start in valid_x_velocities:
        for y_start in valid_y_velocities:
            x_vel = x_start
            y_vel = y_start
            x_pos = 0
            y_pos = 0
            max_height = 0
            made_it = False
            while y_pos >= y_min:
                x_pos += x_vel
                if x_vel > 0:
                    x_vel -= 1
                y_pos += y_vel
                max_height = max(y_pos, max_height)
                y_vel -= 1
                if x_min <= x_pos <= x_max and y_min <= y_pos <= y_max:
                    made_it = True
                    MADE_IT_COUNT += 1
                    break
            overall_max_height = max(max_height, overall_max_height)
    return overall_max_height

def part2():
    return MADE_IT_COUNT

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()