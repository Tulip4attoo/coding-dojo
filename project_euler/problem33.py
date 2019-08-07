

for a in xrange(1,10):
	for c in xrange(1, 10):
		if (9 * a * c) % (10 * a - c) == 0:
			b = (9 * a * c) / (10 * a - c)
			print "ab: %d%d, bc: %d%d" % (a, b, b, c)
