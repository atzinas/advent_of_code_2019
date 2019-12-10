INPUT_LOW = 357253 
INPUT_HIGH = 892942 

counter = 0
counter_new = 0

for password in range(INPUT_LOW, INPUT_HIGH + 1):
    correct = True
    correct_new = True
    is_double = False
    is_double_new = False
    password_list = list(map(int, str(password)))
    double_count = 1
    for digit_pos in range(1, len(password_list)):
        if password_list[digit_pos] < password_list[digit_pos - 1]:
            correct = False 
            correct_new = False
        if password_list[digit_pos] == password_list[digit_pos - 1]:
            is_double = True
            double_count +=1
        else:
            if double_count == 2:
                is_double_new = True
            double_count = 1
    if double_count == 2:
        is_double_new = True

    if is_double is False:
        correct = False
    
    if is_double_new is False:
        correct_new = False

    if correct is True:
        counter += 1
    
    if correct_new is True:
        counter_new += 1
print(counter)
print(counter_new)
