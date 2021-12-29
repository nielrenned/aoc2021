DAY = 16
RAW_INPUT = None
INPUT = None

def load_input(use_test_input=False):
    global RAW_INPUT
    path = f'inputs/day{DAY}.txt'
    if use_test_input:
        path = f'inputs/day{DAY}_test.txt'
    with open(path) as f:
        RAW_INPUT = f.read()

hex_mapping = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

def parse_input():
    global INPUT
    INPUT = RAW_INPUT.strip()

# packet will return the total version, the length of whatever 
# it processes, and the number of packets
def packet(bits, indent=0):
    version = int(bits[:3], base=2)
    type_id = int(bits[3:6], base=2)
    #print(' '*indent + f'[V{version} T{type_id}] ', end='')
    i = 6
    if type_id == 4: # literal
        #print('literal: ', end='')
        literal_bits = ''
        while True:
            literal_bits += bits[i+1:i+5]
            if bits[i] == '0':
                break
            i += 5
        i += 5
        literal = int(literal_bits, base=2)
        #print(literal)
        return literal, version, i
    else: # operator
        '''print('operator ', end='')
        if type_id == 0: # sum
            print('+')
        elif type_id == 1: # product
            print('*')
        elif type_id == 2: # min
            print('min')
        elif type_id == 3: # max
            print('max')
        elif type_id == 5: # >
            print('>')
        elif type_id == 6: # <
            print('<')
        elif type_id == 7: # ==
            print('=')'''
        
        i += 1
        values = []
        version_total = version
        value = 0
        if bits[i-1] == '0':
            length = int(bits[i:i+15], base=2)
            i += 15
            end_index = i + length
            while i < end_index:
                sub_value, sub_version_totals, sub_length = packet(bits[i:], indent+1)
                version_total += sub_version_totals
                i += sub_length
                values.append(sub_value)
        else:
            total_packets = int(bits[i:i+11], base=2)
            i += 11
            version_total = version
            for _ in range(total_packets):
                sub_value, sub_version_totals, sub_length = packet(bits[i:], indent+1)
                version_total += sub_version_totals
                i += sub_length
                values.append(sub_value)
        
        if type_id == 0: # sum
            value = sum(values)
        elif type_id == 1: # product
            value = 1
            for v in values:
                value *= v
        elif type_id == 2: # min
            value = min(values)
        elif type_id == 3: # max
            value = max(values)
        elif type_id == 5: # >
            value = 1 if values[0] > values[1] else 0
        elif type_id == 6: # <
            value = 1 if values[0] < values[1] else 0
        elif type_id == 7: # ==
            value = 1 if values[0] == values[1] else 0
        
        return value, version_total, i

VALUE = 0

def part1():
    global VALUE
    bits = ''
    for c in INPUT:
        bits += hex_mapping[c]
    VALUE, version, _ = packet(bits)
    return version

def part2():
    return VALUE

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()