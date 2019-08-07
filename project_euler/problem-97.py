ten_ten = 10 ** 10
two_forty = 2 ** 40
dumb = two_forty % ten_ten

for power in xrange(1, 195761):
	dumb = (dumb * two_forty) % ten_ten

print (dumb * 28433 * 2 ** 17 + 1) % ten_ten