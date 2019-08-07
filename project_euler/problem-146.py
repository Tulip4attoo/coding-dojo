import time

# i just read the problem in the wrong way. terrible misunderstanding :/
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

list_prime = my_sieve(15 * 10 ** 7) 

#it takes too long, should change algo
# def check_number(number):
# 	if number ** 2 + 1 in list_prime:
# 		if number ** 2 + 3 in list_prime:
# 				if number ** 2 + 7 in list_prime:
# 					if number ** 2 + 9 in list_prime:
# 						if number ** 2 + 13 in list_prime:
# 							if number ** 2 + 27 in list_prime:
# 								return True
# 	else:
# 		return False

def check_number(number):
	for i in xrange(1, len(list_prime) - 5):
		if list_prime[i] == number ** 2 + 1:
			# check 5 next numbers
			if list_prime[i + 1] - list_prime[i] == 2:
				if list_prime[i + 2] - list_prime[i] == 6:
					if list_prime[i + 3] - list_prime[i] == 8:
						if list_prime[i + 4] - list_prime[i] == 12:
							if list_prime[i + 5] - list_prime[i] == 26:
								return True
		if list_prime[i] > number ** 2 + 1:
			return False

# we do some math to find out if n satisfies the condition,
# n must divisible by 10, and could not divisible by 3, 7 and 13.
# we create this list to reduce number of n

def maybe_list(number):
	limit = int(number ** 0.5) / 10 + 1
	dumb_list = range(0, limit)
	for i in (3, 7, 13):
		dumb = (limit - 1) / i
		dumb_list[i :: i] = [0] * dumb
	return filter(None, dumb_list)

candidate_list = maybe_list(15 * 10 ** 7)

for n in candidate_list:
	if check_number(10 * n) == True:
		sum_value = sum_value + 10 * n

print sum_value

print("--- %s seconds ---" % (time.time() - start_time))


