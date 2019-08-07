import time


start_time = time.time()

sum_value = 0

def my_sieve(n):
	dumb_list = range(0, n)
	limit = int(n ** 0.5) + 1
	for i in xrange(2, limit):
		if dumb_list[i]:
			dumb = (n - 1) / i - 1
			dumb_list[i + i :: i] = [0] * dumb
	dumb_list[1] = 0
	return filter(None, dumb_list)


def count(n):
	dumb_list = [0] * n
	prime_under_range = my_sieve(n / 2)
	limit = int(n ** 0.5)
	no_of_prime = len(prime_under_range)
	for index_1 in xrange(0, no_of_prime):
		prime_1 = prime_under_range[index_1]
		if prime_1 > limit:
			break
		for index_2 in xrange(index_1, no_of_prime):
			prime_2 = prime_under_range[index_2]
			if prime_1 * prime_2 > n:
				break
			else:
				dumb_list[prime_1 * prime_2] = 1
	return len(filter(None, dumb_list))

print count(10**8)

print("--- %s seconds ---" % (time.time() - start_time))


