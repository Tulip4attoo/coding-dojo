import math

# first ten 1 digit numbers do count but 0
count = 9

max_n = int(math.log(0.1, 10) / math.log(0.9, 10))
for n in xrange(2, max_n + 1):
	dumb = int((10 ** (n - 1)) ** (1.0 / n))
	count = count + 9 - dumb

print count