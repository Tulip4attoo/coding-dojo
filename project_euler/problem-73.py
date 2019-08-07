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

list_prime = my_sieve(1000) 

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
			break
	if len(factorize_dict) == 0:
		return {number: 1}
	elif dumb > 1000:
		factorize_dict[dumb] = 1
	return factorize_dict

def counter(number):
	dumb = factorize(number, list_prime)
	dumb_list = range(0, number)
	for i in dumb:
		dumb_list[0 :: i] = [0] * (number / i)
	dumb_list[0 : number / 3 + 1] = [0] * (number / 3 + 2)
	dumb_list[(number + 3) / 2 : number + 1] = [0] * (number / 2 + 1)
	return len(filter(None, dumb_list))

for i in xrange(2, 12000):
	sum_value = sum_value + counter(i)

print sum_value

print("--- %s seconds ---" % (time.time() - start_time))


