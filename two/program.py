return_position = 0 
add  = 1
multiply = 2
wanted_answer = 19690720

with open("in.txt", "r") as f:
	intcode_string = f.read()

intcode_string = intcode_string.split(',')

for number_in_position_1 in range(100):
	for number_in_position_2 in range(100):
		intcode = list(map(int, intcode_string))
		intcode[1] = number_in_position_1
		intcode[2] = number_in_position_2
		instruction_pointer = 0
		while instruction_pointer < len(intcode):
			first_number_position = intcode[instruction_pointer + 1]
			second_number_position = intcode[instruction_pointer + 2]
			result_position = intcode[instruction_pointer + 3]
			if intcode[instruction_pointer] == add:
				intcode[result_position] = intcode[first_number_position] + intcode[second_number_position]
				instruction_pointer += 4
			elif intcode[instruction_pointer] == multiply:
				intcode[result_position] = intcode[first_number_position] * intcode[second_number_position]
				instruction_pointer +=4 
			else:
				break
	
		if intcode[return_position] == wanted_answer:
			noun = number_in_position_1
			verb = number_in_position_2

print(100 * noun +verb)
