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

list_prime = my_sieve(10000) 


def nearest_index_prime_number(number, dumb_list):
	for i in xrange(0, len(dumb_list)):
		if dumb_list[i] > number:
			return (i - 1)

def power_triple(number, dumb_list):
	count = 0
	power_triple_list = []
	dumb_forth = int(number ** 0.25)
	index_forth = nearest_index_prime_number(dumb_forth, dumb_list)
	for i in xrange(1, index_forth + 1):
		p_forth = dumb_list[i]
		dumb_triple = int((number - p_forth ** 4) ** (1. / 3))
		index_triple = nearest_index_prime_number(dumb_triple, dumb_list)
		for j in xrange(1, index_triple + 1):
			p_triple = dumb_list[j]
			dumb_double = int((number - p_forth ** 4 - p_triple ** 3) ** 0.5)
			index_double = nearest_index_prime_number(dumb_double, dumb_list)
			for l in xrange(1, index_double + 1):
				power_triple_list.append(p_forth ** 4 + p_triple ** 3 + dumb_list[l] ** 2)
	return len(set(power_triple_list))

print power_triple(50000000, list_prime)




print("--- %s seconds ---" % (time.time() - start_time))
