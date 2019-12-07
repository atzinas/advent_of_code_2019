RETURN_POSITION = 0 
ADD = 1
MULTIPLY = 2
WANTED_ANSWER = 19690720

with open("in.txt", "r") as f:
	intcode_string = f.read()

intcode_string = intcode_string.split(',')

for pos1 in range(100):
	for pos2 in range(100):
		intcode = list(map(int, intcode_string))
		intcode[1] = pos1
		intcode[2] = pos2
		instruction_pointer = 0
		while instruction_pointer < len(intcode):
			candidate_noun = intcode[instruction_pointer + 1]
			candidate_verb = intcode[instruction_pointer + 2]
			result_position = intcode[instruction_pointer + 3]
			if intcode[instruction_pointer] == ADD:
				intcode[result_position] = intcode[candidate_noun] + intcode[candidate_verb]
			elif intcode[instruction_pointer] == MULTIPLY:
				intcode[result_position] = intcode[candidate_noun] * intcode[candidate_verb]
			else:
				break
			
			instruction_pointer += 4 
	
		if intcode[RETURN_POSITION] == WANTED_ANSWER:
			noun = pos1
			verb = pos2

print(100 * noun + verb)
