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

list_prime = my_sieve(10 ** 6) 

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

def check_4_distinct(number):
	if len(factorize(number, list_prime)) == 4:
		return True
	return False

def find_number():
	for i in xrange(2, 1000001):
		if check_4_distinct(i) == True:
			if check_4_distinct(i + 1) == True:
				if check_4_distinct(i + 2) == True:
					if check_4_distinct(i + 3) == True:
						return i
	return 0

print find_number()

print("--- %s seconds ---" % (time.time() - start_time))


