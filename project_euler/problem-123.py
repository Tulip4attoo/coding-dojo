import time


start_time = time.time()

sum_value = 0

def my_sieve(n):
	dumb_list = range(0, n)
	limit = int(n ** 0.5)
	for i in xrange(2, limit):
		if dumb_list[i]:
			dumb = (n - 1) / i - 1
			dumb_list[i + i :: i] = [0] * dumb
	return filter(None, dumb_list)

list_prime = my_sieve(1000000) 

for index in xrange(1, 10000000, 2):
	prime = list_prime[index]
	if 2 * prime * index > 10 ** 10:
		print index
		break

print("--- %s seconds ---" % (time.time() - start_time))


