import time


start_time = time.time()

sum_value = 0

# just explore the (a + 1) ** n + (a - 1) ** n
# we find the remain is 2 * n * a or 2
# so we calculate the a from n - so much easy

for n in xrange(3, 1001):
	sum_value = sum_value + ((n - 1) / 2) * n * 2

print sum_value

print("--- %s seconds ---" % (time.time() - start_time))


