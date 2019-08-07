import time


start_time = time.time()

abundant_list = range(0, 28124)
number_list = range(0, 28124)

def factor_list(number):
	dumb_list = [0] * number
	limit = int(number ** 0.5) + 1
	dumb_list[0] = 1
	for i in xrange(2, limit):
		if number % i == 0:
			dumb_list[i] = i
			dumb_list[number / i] = number / i
	return filter(None, dumb_list)

def check_abundant(number):
	if number < sum(factor_list(number)):
		return True
	return False

for i in xrange(1, 28124):
	if check_abundant(i) == False:
		abundant_list[i] = 0

abundant_list = filter(None, abundant_list)

for abu_1 in abundant_list:
	for abu_2 in abundant_list:
		if abu_1 + abu_2 > 28123:
			break
		else:
			number_list[abu_1 + abu_2] = 0

print sum(number_list)



print("--- %s seconds ---" % (time.time() - start_time))


