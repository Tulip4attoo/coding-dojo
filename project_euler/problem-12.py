import time


start_time = time.time()

def my_sieve(n):
	dumb_list = range(0, n)
	limit = int(n ** 0.5)
	for i in xrange(2, limit):
		if dumb_list[i]:
			dumb = (n - 1) / i - 1
			dumb_list[i + i :: i] = [0] * dumb
	return filter(None, dumb_list)

list_prime = my_sieve(500000) 

def factorize(number, dumb_list):
	dumb = number
	factorize_dict = {}
	for i in xrange(1, len(dumb_list)):
		factor = dumb_list[i]
		if dumb % factor == 0:
			dumb = dumb / factor
			factorize_dict[dumb_list[i]] = 1
			while dumb % factor == 0:
				dumb = dumb / factor
				factorize_dict[dumb_list[i]] = factorize_dict[dumb_list[i]] + 1
		if dumb < factor:
			return factorize_dict

def number_divisible(number):
	dumb = factorize(number, list_prime)
	divisible = 1
	for i in dumb:
		divisible = divisible * (dumb[i] + 1)
	return divisible

for i in xrange(1, 1000000):
	triangular = i * (i + 1) / 2
	if number_divisible(triangular) > 500:
		print triangular
		break


print("--- %s seconds ---" % (time.time() - start_time))


