import time

start_time = time.time()

a_power_b_list = []

for a in xrange(2, 101):
	for b in xrange(2, 101):
		a_power_b_list.append(a ** b)

print len(set(a_power_b_list))


print("--- %s seconds ---" % (time.time() - start_time))
