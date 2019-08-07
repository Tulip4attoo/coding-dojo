import time


start_time = time.time()


def my_sieve(n):
	dumb_list = range(0, n)
	limit = int(n ** 0.5) + 1
	for i in xrange(2, limit):
		if dumb_list[i]:
			dumb = (n - 1) / i - 1
			dumb_list[i + i :: i] = [0] * dumb
	return filter(None, dumb_list)

list_prime = my_sieve(1000000) 

def find_limit_seq(number):
	dumb = 0
	for i in xrange(1, number):
		dumb = dumb + list_prime[i]
		if dumb > number:
			return i - 1

def find_prime(number):
	limit = find_limit_seq(number)
	for i in xrange(limit, 1, - 1):
		for j in xrange(1, len(list_prime) - i + 1):
			sum_seq = 0
			for k in xrange(0, i):
				sum_seq = sum_seq + list_prime[j + k]
			if sum_seq > number:
					break
			if sum_seq in list_prime:
				return sum_seq

print find_prime(10 ** 6)

print("--- %s seconds ---" % (time.time() - start_time))
