number = 0

def factorial(ceiling):
	temp_value = 1
	for order in xrange(1, ceiling + 1):
		temp_value = temp_value * order
	return temp_value

print factorial(40) / (factorial(20) * factorial(20))