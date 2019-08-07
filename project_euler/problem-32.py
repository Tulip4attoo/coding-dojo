import time


start_time = time.time()

pan_list = []


def check_pandigital_products(a, b):
	dumb = str(a) + str(b) + str(a * b)
	if len(set(dumb)) == 9:
		if "0" not in set(dumb):
			if len(list(dumb)) == 9:
				return True
	return False

for a in xrange(1, 100):
	for b in xrange(99, 1000000 / a):
		if check_pandigital_products(a, b):
			pan_list.append(a * b)

print sum(set(pan_list))

print("--- %s seconds ---" % (time.time() - start_time))
