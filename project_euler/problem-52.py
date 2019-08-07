import time

start_time = time.time()

def check_permuted(number_1, number_2):
	if set(str(number_1)) == set(str(number_2)):
		return True
	else:
		return False

def find_n():
	for n in xrange(10, 10 ** 8):
		for i in xrange(2, 8):
			if i == 7:
				return n
			if check_permuted(n, i * n) == False:
				break

find_n()

print("--- %s seconds ---" % (time.time() - start_time))
