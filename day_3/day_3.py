from math import inf

with open("in.txt", "r") as f:
    movement_data_string = f.read()

def remove_spaces(data):
    if data == '':
        return False
    return True  

positions = {} 

mov_1_string, mov_2_string = movement_data_string.splitlines()

mov_1_string = mov_1_string.split(',')
mov_2_string = mov_2_string.split(',')

mov_1 = []
mov_2 = []

for item in mov_1_string:
    mov_1.append((item[0], int(item[1:])))

for item in mov_2_string:
    mov_2.append((item[0], int(item[1:])))

x = y = 0
counter = 0
deltas = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}


for direction, steps in mov_1:
    dx, dy = deltas[direction]
    target_x = x + steps * dx
    target_y = y + steps * dy

    while x != target_x or y != target_y:
        counter += 1
        x += dx
        y += dy
        positions[(x, y)] = counter

x = y = 0

counter = 0
best_steps = inf
best_distance = inf

current_steps = 0

for direction, steps in mov_2:
    dx, dy = deltas[direction]

    target_x = x + dx * steps
    target_y = y + dy * steps

    while x != target_x or y != target_y:
        counter += 1 
        x += dx
        y += dy
        if (x, y) in positions:
            current_steps = counter + positions[(x, y)]
            best_steps = min(current_steps, best_steps)
            distance = abs(x) + abs(y)
            best_distance = min(distance, best_distance)

print(best_distance)
print(best_steps)
