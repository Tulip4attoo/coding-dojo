
def digit_sum(number):
	dumb_list = list(str(number))
	dumb = 0
	for i in dumb_list:
		dumb = dumb + int(i)
	return dumb

max_digit_sum = 0

for a in xrange(10, 100):
	for b in xrange(10, 100):
		a_power_b = a ** b
		if max_digit_sum < digit_sum(a_power_b):
			max_digit_sum = digit_sum(a_power_b)

print max_digit_sum
