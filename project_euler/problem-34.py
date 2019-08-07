number = 0
number_set = []

def factorial(ceiling):
	temp_value = 1
	for order in xrange(1, ceiling + 1):
		temp_value = temp_value * order
	return temp_value

for number in xrange(3, factorial(9) * 6):
	temp_value = 0
	for digit in xrange(0, len(str(number))):
		temp_value = temp_value + factorial(int(str(number)[digit]))
	if temp_value == number:
		number_set.append(number)

print sum(number_set)