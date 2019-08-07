for number in xrange(144, 1000000):
	hexagonal = number * (number * 2 - 1)
	delta = (1 + 24 * hexagonal) ** 0.5
	pen_number = (1 + delta) / 6
	if pen_number == int(pen_number):
		print hexagonal
		break
