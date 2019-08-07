from fractions import Fraction


e_continue_frac = [2]

for number in xrange(1, 100):
	e_continue_frac.append(1)
	e_continue_frac.append(2 * number)
	e_continue_frac.append(1)

dumb = Fraction(e_continue_frac[99])

for number in xrange(0, 99):
	dumb = 1 / dumb + e_continue_frac[98 - number]

value = dumb.numerator
print sum(map(int, list(str(value)))) 