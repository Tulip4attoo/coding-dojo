

factorial = [1]
time = 1
for i in xrange(1 , 10):
	time = time * i
	factorial.append(time)

print factorial

for a1 in xrange(0, 4):
	for a2 in xrange(0, 10):
		for a3 in xrange(0, 10):
			for a4 in xrange(0, 10):
				for a5 in xrange(0, 10):
					for a6 in xrange(0, 10):
						for a7 in xrange(0, 10):
							if factorial[a1] + factorial[a2] + factorial[a3] + factorial[a4] + factorial[a5] + factorial[a6] + factorial[a7] == 10 ** 6 * a1 + 10 ** 5 * a2 + 10 ** 4 * a3 + 10 ** 3 * a4 + 10 ** 2 * a5 + 10 * a6 + a7:
								print 10 ** 6 * a1 + 10 ** 5 * a2 + 10 ** 4 * a3 + 10 ** 3 * a4 + 10 ** 2 * a5 + 10 * a6 + a7