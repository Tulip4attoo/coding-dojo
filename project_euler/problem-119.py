import time

start_time = time.time()

def check_a_b(a, b):
	dumb = sum(map(int, list(str(a ** b))))
	if dumb == a:
		return True
	else:
		return False

dumb_list = []

for a in xrange(3, 200):
	for b in xrange(2, 200):
		if check_a_b(a, b) == True:
			dumb_list.append(long(a ** b))

dumb_list.sort()

print dumb_list[29]

print("--- %s seconds ---" % (time.time() - start_time))
