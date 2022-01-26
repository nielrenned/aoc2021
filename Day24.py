DAY = 24
RAW_INPUT = None
INPUT = None

'''
  I figured this one out by hand!
  
  There's a relationship between the digits in the input. Essentially, z becomes a stack of digits
  mod 26, and certain steps cancel each other out. See below.
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
    INPUT = []
    for line in RAW_INPUT.split('\n')[:-1]:
        instr = line.split()
        for i in range(len(instr)):
            try:
                instr[i] = int(instr[i])
            except:
                pass
        INPUT.append(tuple(instr))

def get_value(x, variables):
    if type(x) is int:
        return x
    else:
        return variables[x]

def base_26_digits(x):
    digits_reversed = []
    while x > 0:
        digits_reversed.append(x % 26)
        x = x//26
    return digits_reversed[::-1]

def run_instructions_with_input(instructions, given_input):
    variables = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    input_i = 0
    for ip, instr in enumerate(instructions):
        command = instr[0]
        if command == 'inp':
            #_ = input()
            variables[instr[1]] = given_input[input_i]
            input_i += 1
        elif command == 'add':
            op1, op2 = instr[1:]
            variables[op1] = get_value(op1, variables) + get_value(op2, variables)
        elif command == 'mul':
            op1, op2 = instr[1:]
            variables[op1] = get_value(op1, variables) * get_value(op2, variables)
        elif command == 'div':
            op1, op2 = instr[1:]
            variables[op1] = get_value(op1, variables) // get_value(op2, variables)
        elif command == 'mod':
            op1, op2 = instr[1:]
            variables[op1] = get_value(op1, variables) % get_value(op2, variables)
        elif command == 'eql':
            op1, op2 = instr[1:]
            variables[op1] = 1 if get_value(op1, variables) == get_value(op2, variables) else 0
        #print(ip+1, ':', instr)
        #print('    ', variables, ' ', base_26_digits(variables['z']))
    return variables

def part1():
    '''
    blocks = []
    block = []
    for instr in INPUT:
        if instr == ('inp', 'w'):
            blocks.append(block)
            block = [instr]
        else:
            block.append(instr)
    blocks.append(block)
    blocks = blocks[1:]
    print(''.join(f'| Block {i: 3}' for i in range(1, 15)) + '|')
    print('|=========='*14 + '|')
    for i in range(len(blocks[0])):
        line = ''
        to_match = blocks[0][i]
        matching = True
        for block in blocks:
            if block[i] != to_match:
                matching = False
            s = '| ' + ' '.join(map(str, block[i]))
            s += ' '*(11 - len(s))
            line += s
        line += '| '
        line += 'yes' if matching else 'no'
        print(line)'''
    
    '''
      The digits that are paired up in the code below must have a certain difference (as in subtraction)
      for z to end up being 0 at the end.
    '''
    test_number = [0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    test_number[1] = 3
    test_number[14] = 9

    test_number[2] = 6
    test_number[13] = 9
    
    test_number[3] = 9
    test_number[4] = 6

    test_number[5] = 9
    test_number[12] = 1
    
    test_number[6] = 7
    test_number[11] = 9
    
    test_number[7] = 9
    test_number[8] = 4

    test_number[9] = 9
    test_number[10] = 7
    
    test_input = test_number[1:]
    test_input = test_input + [0]*(14-len(test_input))
    
    result = run_instructions_with_input(INPUT, test_input)
    if result['z'] == 0:
        return int(''.join(map(str, test_input)))

def part2():
    test_number = [0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    test_number[1] = 1
    test_number[14] = 7

    test_number[2] = 1
    test_number[13] = 4
    
    test_number[3] = 4
    test_number[4] = 1

    test_number[5] = 9
    test_number[12] = 1
    
    test_number[6] = 1
    test_number[11] = 3
    
    test_number[7] = 6
    test_number[8] = 1

    test_number[9] = 3
    test_number[10] = 1
    test_input = test_number[1:]
    test_input = test_input + [0]*(14-len(test_input))
    
    result = run_instructions_with_input(INPUT, test_input)
    if result['z'] == 0:
        return int(''.join(map(str, test_input)))

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()