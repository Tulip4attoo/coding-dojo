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

list_prime = my_sieve(1001000) 


def smallest_n(p_1, p_2):
	digit = len(str(p_1))
	factor = 10 ** digit
	for i in xrange(1, p_2):
		n = i * factor + p_1
		if n % p_2 == 0:
			return n

# it is fucking take too much time
for index_1 in xrange(3, len(list_prime)):
	p_1 = list_prime[index_1]
	p_2 = list_prime[index_1 + 1]
	if p_1 > 10 ** 6:
		break
	sum_value = sum_value + smallest_n(p_1, p_2)
	
print sum_value

print("--- %s seconds ---" % (time.time() - start_time))

