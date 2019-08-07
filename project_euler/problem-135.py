import time

start_time = time.time()

def counter(number):
	list_number = [0] * number
	for z in xrange(1, number):
		for a in xrange(z / 3 + 1, number):
			n = (a + z) * (3 * a - z)
			if n + 1 > number:
				break
			else:
				list_number[n] = list_number[n] + 1
	return list_number.count(10)

print counter(10 ** 6)

print("--- %s seconds ---" % (time.time() - start_time))
