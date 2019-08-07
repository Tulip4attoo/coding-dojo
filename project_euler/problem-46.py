import time

contra = 0

start_time = time.time()

def my_sieve(n):
	dumb_list = range(0, n)
	limit = int(n ** 0.5)
	for i in xrange(2, limit):
		if dumb_list[i]:
			dumb = (n - 1) / i - 1
			dumb_list[i + i :: i] = [0] * dumb
	return filter(None, dumb_list)

list_prime = my_sieve(100000) 


def check_conjecture(number):
	square_part = int((number / 2) ** 0.5) + 1
	dumb_3 = 0
	if number in list_prime:
		return 1
	for i in xrange(1, square_part):
		dumb_2 = number - 2 * i ** 2
		if dumb_2 in list_prime:
			dumb_3 = 1
	return dumb_3

for number in xrange(1, 10000, 2):
	contra = number
	dumb = check_conjecture(number)
	if dumb == 0:
		break

print contra

print("--- %s seconds ---" % (time.time() - start_time))
