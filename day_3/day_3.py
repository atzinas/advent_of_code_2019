from math import inf

with open("in.txt", "r") as f:
    movement_data_string = f.read()

mov_1_string, mov_2_string = movement_data_string.splitlines()

mov_1_string = mov_1_string.split(',')
mov_2_string = mov_2_string.split(',')

mov_1 = []
mov_2 = []

for item in mov_1_string:
    mov_1.append((item[0], int(item[1:])))

for item in mov_2_string:
    mov_2.append((item[0], int(item[1:])))

def follow_snake(snake):
    x = y = 0
    counter = 0
    positions = {}

    for direction, steps in snake:
        dx, dy = {
            'U': (0, 1),
            'D': (0, -1),
            'L': (-1, 0),
            'R': (1, 0)
        }[direction]

        target_x = x + steps * dx
        target_y = y + steps * dy

        while x != target_x or y != target_y:
            counter += 1
            x += dx
            y += dy
            positions[(x, y)] = counter

    return positions

positions1 = follow_snake(mov_1)
positions2 = follow_snake(mov_2)

meet_points = set(positions1.keys()).intersection(set(positions2.keys()))

best_steps = inf
best_distance = inf

for point in meet_points:
    current_steps = positions1[point] + positions2[point]
    best_steps = min(current_steps, best_steps)
    distance = abs(point[0]) + abs(point[1])
    best_distance = min(distance, best_distance)

print(best_distance)
print(best_steps)
