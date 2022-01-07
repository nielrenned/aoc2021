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

from copy import deepcopy

def add_numbers(left, right):
    return deepcopy([left, right])

def magnitude(num):
    if type(num) is int:
        return num
    else:
        left, right = num
        return 3*magnitude(left) + 2*magnitude(right)

def get_num_at_index(num, index):
    if len(index) == 0:
        return num
    return get_num_at_index(num[index[0]], index[1:])

'''
  This is a DFS on the binary tree, where we look for the first pair with depth >= 4.
'''
def explode_searcher(num, depth=0, current_index=[]):
    if type(num) is int:
        return False, None
    
    if depth >= 4:
        return True, current_index
    
    left, right = num
    found_needs_exploding, index = explode_searcher(left, depth+1, current_index + [0])
    if found_needs_exploding:
        return found_needs_exploding, index
    
    found_needs_exploding, index = explode_searcher(right, depth+1, current_index + [1])
    return found_needs_exploding, index

def explode(num):
    found_needs_exploding, index = explode_searcher(num)
    if found_needs_exploding:
        new_num = deepcopy(num)
        parent_list = get_num_at_index(new_num, index[:-1])
        replace_index = index[-1]
        num_to_explode = parent_list[replace_index]
        left_value, right_value = num_to_explode
        
        '''
          We want to add `right_value` to the first regular number to the right.
        
          These "numbers" are essentially binary trees. To find the next number to the right,
          we have to walk back up our path until we find the a place we went to the left. Then
          we change that to a right turn, and then take only lefts until we reach a regular number.
          In our model, a "left" is a zero, and a "right" is a one. So if we never took a left, 
          there won't be a number to the right.
        '''
        if 0 in index:
            last_zero_loc = index[::-1].index(0)
            right_index = index[::-1][last_zero_loc:][::-1]
            right_index[-1] = 1
            while True:
                right_num = get_num_at_index(new_num, right_index)
                if right_num is None or type(right_num) is int:
                    break
                right_index = right_index + [0]
            if right_num is not None:
                right_num_parent = get_num_at_index(new_num, right_index[:-1])
                right_num_parent[right_index[-1]] += right_value
        
        # Same as above, except switch left and right.
        if 1 in index:
            last_one_loc = index[::-1].index(1)
            left_index = index[::-1][last_one_loc:][::-1]
            left_index[-1] = 0
            while True:
                left_num = get_num_at_index(new_num, left_index)
                if left_num is None or type(left_num) is int:
                    break
                left_index = left_index + [1]
            if left_num is not None:
                left_num_parent = get_num_at_index(new_num, left_index[:-1])
                left_num_parent[left_index[-1]] += left_value
        
        parent_list[replace_index] = 0
        return True, new_num
    return False, num

'''
  This is a DFS on the binary tree, where we look for the first regular number that's >= 10.
'''
def split_searcher(num, current_index=[]):
    if type(num) is int:
        if num >= 10:
            return True, current_index
        else:
            return False, None
    
    left, right = num
    found_needs_splitting, index = split_searcher(left, current_index + [0])
    if found_needs_splitting:
        return found_needs_splitting, index
    
    found_needs_splitting, index = split_searcher(right, current_index + [1])
    return found_needs_splitting, index

def split(num):
    found_needs_splitting, index = split_searcher(num)
    if found_needs_splitting:
        new_num = deepcopy(num)
        parent_list = get_num_at_index(new_num, index[:-1])
        replace_index = index[-1]
        num_to_split = parent_list[replace_index]
        new_left = num_to_split // 2
        new_right = num_to_split - new_left
        parent_list[replace_index] = [new_left, new_right]
        return True, new_num
    return False, num

def reduce(num):
    result = num
    while True:
        did_split = False
        did_explode, result = explode(result)
        if not did_explode:
            did_split, result = split(result)
        if not (did_explode or did_split):
            break
    return result

def part1():
    result = INPUT[0]
    for next_num in INPUT[1:]:
        result = add_numbers(result, next_num)
        result = reduce(result)
    return magnitude(result)

def part2():
    max_mag = 0
    for i in range(len(INPUT)):
        for j in range(i+1, len(INPUT)):
            n1 = INPUT[i]
            n2 = INPUT[j]
            
            mag1 = magnitude(reduce(add_numbers(n1, n2)))
            mag2 = magnitude(reduce(add_numbers(n2, n1)))
            max_mag = max(max_mag, max(mag1, mag2))
    return max_mag

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()