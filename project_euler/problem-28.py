import time


start_time = time.time()


sum_value = 1

for n in xrange(3, 1003, 2):
	for i in xrange(0, 4):
		sum_value = sum_value + (n ** 2 - (n - 1) * i) 

print sum_value

print("--- %s seconds ---" % (time.time() - start_time))
