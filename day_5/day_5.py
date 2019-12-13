JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUAL = 8
INPUT = 3
OUTPUT = 4
RETURN_POSITION = 0 
ADD = 1
MULTIPLY = 2
END = 99

with open("in.txt", "r") as f:
    intcode_string = f.read()

intcode = intcode_string.split(',')

instruction_pointer = 0
while instruction_pointer < len(intcode) - 1:
    mode = [0, 0, 0]
    if len(intcode[instruction_pointer]) > 1:
        instruction_size = len(intcode[instruction_pointer])
        command = int(intcode[instruction_pointer][instruction_size - 2] + intcode[instruction_pointer][instruction_size - 1])
        digit_pointer = instruction_size -3 
        mode_pointer = 0
        while digit_pointer >= 0:
            mode[mode_pointer] = int(intcode[instruction_pointer][digit_pointer])
            mode_pointer += 1
            digit_pointer -= 1
    else:
        command = int(intcode[instruction_pointer])
    if command == ADD:
        pos_1 = int(intcode[instruction_pointer + 1])
        pos_2 = int(intcode[instruction_pointer + 2])
        pos_3 = int(intcode[instruction_pointer + 3])
        instruction_pointer += 4
        if mode[0] == 0:
            value_1 = int(intcode[pos_1])
        else:
            value_1 = pos_1
        if mode[1] == 0:
            value_2 = int(intcode[pos_2])
        else:
            value_2 = pos_2
        intcode[pos_3] = str(value_1 + value_2)
    elif command  == MULTIPLY:
        pos_1 = int(intcode[instruction_pointer + 1])
        pos_2 = int(intcode[instruction_pointer + 2])
        pos_3 = int(intcode[instruction_pointer + 3])
        instruction_pointer += 4
        if mode[0] == 0:
            value_1 = int(intcode[pos_1])
        else:
            value_1 = pos_1
        if mode[1] == 0:
            value_2 = int(intcode[pos_2])
        else:
            value_2 = pos_2
        intcode[pos_3] = str(value_1 * value_2) 
    elif command == OUTPUT:
        pos_1 = int(intcode[instruction_pointer + 1])
        instruction_pointer += 2
        print(intcode[pos_1])
    elif command == INPUT:
        pos_1 = int(intcode[instruction_pointer + 1])
        instruction_pointer += 2
        intcode[pos_1] = '5'
    elif command == JUMP_IF_TRUE:
        pos_1 = int(intcode[instruction_pointer + 1])
        pos_2 = int(intcode[instruction_pointer + 2])
        if mode[0] == 0:
            value_1 = int(intcode[pos_1])
        else:
            value_1 = pos_1
        if value_1 != 0:
            if mode[1] == 0:
                instruction_pointer = int(intcode[pos_2]) 
            else:
                instruction_pointer = pos_2
        else:
            instruction_pointer += 3
    elif command == JUMP_IF_FALSE:
        pos_1 = int(intcode[instruction_pointer + 1])
        pos_2 = int(intcode[instruction_pointer + 2])
        if mode[0] == 0:
            value_1 = int(intcode[pos_1])
        else:
            value_1 = pos_1
        if value_1 == 0:
            if mode[1] == 0:
                instruction_pointer = int(intcode[pos_2]) 
            else:
                instruction_pointer = pos_2
        else:
            instruction_pointer += 3
    elif command == LESS_THAN:
        pos_1 = int(intcode[instruction_pointer + 1])
        pos_2 = int(intcode[instruction_pointer + 2])
        pos_3 = int(intcode[instruction_pointer + 3])
        if mode[0] == 0:
            value_1 = int(intcode[pos_1])
        else:
            value_1 = pos_1
        if mode[1] == 0:
            value_2 = int(intcode[pos_2])
        else:
            value_2 = pos_2
        if value_1 < value_2:
            intcode[pos_3] = '1'
        else:
            intcode[pos_3] = '0'
        instruction_pointer += 4
    elif command == EQUAL:
        pos_1 = int(intcode[instruction_pointer + 1])
        pos_2 = int(intcode[instruction_pointer + 2])
        pos_3 = int(intcode[instruction_pointer + 3])
        if mode[0] == 0:
            value_1 = int(intcode[pos_1])
        else:
            value_1 = pos_1
        if mode[1] == 0:
            value_2 = int(intcode[pos_2])
        else:
            value_2 = pos_2
        if value_1 == value_2:
            intcode[pos_3] = '1'
        else:
            intcode[pos_3] = '0'
        instruction_pointer += 4
    elif command == END:
        break
