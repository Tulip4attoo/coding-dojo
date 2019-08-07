number = 0
number_set = []

for number in xrange(2, 9 ** 5 * 6):
	temp_value = 0
	for digit in xrange(0, len(str(number))):
		temp_value = temp_value + int(str(number)[digit]) ** 5
	if temp_value == number:
		number_set.append(number)

print sum(number_set)