STARTING_X_Y = 0

import re

with open("in.txt", "r") as f:
    movement_data_string = f.read()

def remove_spaces(data):
    if data == '':
        return False
    return True  

positions = set()

movement_data = movement_data_string.splitlines()
mov_1_string = movement_data[0]
mov_2_string = movement_data[1]

mov_1_string = mov_1_string.split(',')
mov_2_string = mov_2_string.split(',')

mov_1 = []
mov_2 = []

best_distance = 'EMPTY'

for pos in range(len(mov_1_string)):
    mov_1.append(re.split('(\d+)', mov_1_string[pos]))
for pos in range(len(mov_2_string)):
    mov_2.append(re.split('(\d+)', mov_2_string[pos]))

for pos in range(len(mov_1)):
    mov_1[pos] = list(filter(remove_spaces, mov_1[pos]))
    mov_1[pos][1] = int(mov_1[pos][1])
for pos in range(len(mov_2)):
    mov_2[pos] = list(filter(remove_spaces, mov_2[pos]))
    mov_2[pos][1] = int(mov_2[pos][1])

x = STARTING_X_Y
y = STARTING_X_Y


for pos in range(len(mov_1)):
    direction = mov_1[pos][0]
    steps = mov_1[pos][1]
    
    if direction == 'U':
        y_2 = y + steps
        while y < y_2:
            y += 1
            positions.add((x, y))

    if direction == 'D':
        y_2 = y - steps
        while y > y_2:
            y -= 1
            positions.add((x, y))

    if direction == 'R':
        x_2 = x + steps
        while x < x_2:
            x += 1
            positions.add((x, y))

    if direction == 'L':
        x_2 = x - steps
        while x > x_2:
            x -= 1
            positions.add((x, y))

x = STARTING_X_Y
y = STARTING_X_Y


for pos in range(len(mov_2)):
    direction = mov_2[pos][0]
    steps = mov_2[pos][1]
    
    if direction == 'U':
        y_2 = y + steps
        while y < y_2:
            if (x,y) in positions:
                distance = abs(x - STARTING_X_Y) + abs(y - STARTING_X_Y)
                if best_distance == 'EMPTY' or distance < best_distance:
                    best_distance = distance
            y += 1

    if direction == 'D':
        y_2 = y - steps
        while y > y_2:
            if (x,y) in positions:
                distance = abs(x - STARTING_X_Y) + abs(y - STARTING_X_Y)
                if best_distance == 'EMPTY' or distance < best_distance:
                    best_distance = distance
            y -= 1

    if direction == 'R':
        x_2 = x + steps
        while x < x_2:
            if (x,y) in positions:
                distance = abs(x - STARTING_X_Y) + abs(y - STARTING_X_Y)
                if best_distance == 'EMPTY' or distance < best_distance:
                    best_distance = distance
            x += 1

    if direction == 'L':
        x_2 = x - steps
        while x > x_2:
            if (x,y) in positions:
                distance = abs(x - STARTING_X_Y) + abs(y - STARTING_X_Y)
                if best_distance == 'EMPTY' or distance < best_distance:
                    best_distance = distance
            x -= 1


print(best_distance)
