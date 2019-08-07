import time

A = range(1, 10)
dump = 0
result = []
dump_first_value = 0

start_time = time.time()

for i in xrange(500000, 1000000):
	dump = i
	count = 0
	while (dump > 1):
		if (dump % 2 == 0):
			dump = dump / 2
			count = count + 1
		else: 
			dump = 3 * dump + 1
			count = count + 1
	result.append(count)

print (result.index(max(result)) + 500000)

print("--- %s seconds ---" % (time.time() - start_time))
