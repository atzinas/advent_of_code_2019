WIDE = 25
TALL = 6
import math
with open("in.txt", "r") as f:
    data_string = f.read()

def make_int(digit):
    if digit != '\n':
        return int(digit)

def not_none(digit):
    if digit is not None:
        return True
    return False

image_data = list(filter(not_none, map(make_int, list(data_string))))

counter_0 = 0
min_0 = math.inf
pos = 1
counter_1 = 0
counter_2 = 0
for data in image_data:
    if data == 0:
        counter_0 += 1
    elif data == 1:
        counter_1 += 1
    elif data == 2:
        counter_2 += 1
    if pos % (WIDE * TALL) == 0:
        if counter_0 < min_0:
            best_pos = pos - (WIDE * TALL) + 1
            min_0 = counter_0
            best_1 = counter_1
            best_2 = counter_2
        counter_0 = 0
        counter_1 = 0
        counter_2 = 0
    pos += 1

print(best_1 * best_2)

for i in range(WIDE * TALL):
    pixel = image_data[i]
    pos = i
    while pixel == 2:
        pos += WIDE * TALL
        pixel = image_data[pos]
    if pixel == 1:
        print('o', end = '')
    else:
        print(' ', end = '')
    if (i+1) % WIDE == 0:
        print()
