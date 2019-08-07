
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





def count_prime(a, b):
	for n in xrange(0, 1000):
		quadratic = n ** 2 + a * n + b
		if quadratic not in list_prime:
			return n

def find_a_b():
	max_prime = 0
	product = 0
	for b in xrange(1, 170):
		for a in xrange(- 999, 1000):
			prime_b = list_prime[b]
			dumb = count_prime(a, prime_b)
			if dumb > max_prime:
				max_prime = dumb
				product = a * prime_b
	return product

print find_a_b()

print("--- %s seconds ---" % (time.time() - start_time))
