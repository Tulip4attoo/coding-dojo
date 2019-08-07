import time


start_time = time.time()

sum_value = 0
ami_list = []

def sum_proper(number):
	limit = int(number ** 0.5)
	sum_dumb = 1
	for n in xrange(2, limit + 1):
		if number % n == 0:
			sum_dumb = sum_dumb + n + number / n
	if limit ** 2 == number:
		sum_dumb = sum_dumb - limit
	return sum_dumb

for n in xrange(2, 10 ** 4):
	if n == sum_proper(sum_proper(n)):
		if n != sum_proper(n):
			sum_value = sum_value + n
			ami_list.append(n)

print sum_value

print("--- %s seconds ---" % (time.time() - start_time))

