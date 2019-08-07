import time
from math import log
circular_list = []

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

def circle_generate(number):
	digit = int(log(number, 10)) + 1
	str_number = list(str(number))
	circle_list = [number]
	for i in xrange(1, digit):
		temp = str_number.pop(0)
		str_number.append(temp)
		circle_list.append(int("".join(str_number)))
	return circle_list

def check_circlar_prime(number):
	dumb_list = circle_generate(number)
	for n in dumb_list:
		if n not in list_prime:
			return False
	return True

# to reduce the input
maybe_list = range(0, 10 ** 6)
maybe_list[1 : 10] = [0] * 9
not_accept_list = {"0", "2", "4", "5", "6", "8"}
for number in xrange(10, 10 ** 6):
	str_number = list(str(number))
	if len(not_accept_list.intersection(str_number)) > 0:
		maybe_list[number] = 0

maybe_list = filter(None, maybe_list)

for number in maybe_list:
	if check_circlar_prime(number):
		circular_list.append(number)

print len(set(circular_list)) + 4 # count 1 digit


print("--- %s seconds ---" % (time.time() - start_time))
