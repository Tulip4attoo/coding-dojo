import time
import math

start_time = time.time()

def my_sieve(n):
	dumb_list = range(0, n)
	limit = int(n ** 0.5)
	for i in xrange(2, limit):
		if dumb_list[i]:
			dumb = (n - 1) / i - 1
			dumb_list[i + i :: i] = [0] * dumb
	return filter(None, dumb_list)

list_prime = my_sieve(10 ** 4) 

def check_prime(number):
	limit = int(number ** 0.5) + 1
	for i in xrange(1, len(list_prime)):
		dumb = list_prime[i]
		if number % dumb == 0:
			return False
		if dumb > limit:
			return True

def check_pandigital(number):
	digit = int(math.log(number, 10)) + 1
	if set(list(str(number))) == set(map(str, range(1, digit + 1))):
		return True
	else:
		return False


def find_n():
	for n in xrange(7654321, 10, - 1):
		if check_pandigital(n) == True:
			if check_prime(n) == True:
				return n

print find_n()

print("--- %s seconds ---" % (time.time() - start_time))


