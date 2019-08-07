from time import time

start = time()

y = 1

for i in xrange(1,100000000):
	y = i

print("#1: ", time() - start)
