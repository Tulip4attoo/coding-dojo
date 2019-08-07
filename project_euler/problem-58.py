# first create the number list
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

list_prime = my_sieve(10 ** 6) 

def check_prime(number):
	limit = int(number ** 0.5) + 1
	for i in xrange(1, len(list_prime)):
		dumb = list_prime[i]
		if number % dumb == 0:
			return False
		if dumb > limit:
			return True

count_number = 5
count_prime = 3

for n in xrange(5, 200001, 2):
	count_number = count_number + 4
	for i in xrange(1, 4):
		if check_prime(n ** 2 - (n - 1) * i) == True:
			count_prime = count_prime + 1
	if count_prime * 10 < count_number:
		print n
		break

print("--- %s seconds ---" % (time.time() - start_time))
