for c in range(400, 500):
	for a in range(1, int(c / 2)):
		b = 1000 - a - c
		if a ** 2 + b ** 2 == c ** 2:
			product = a * b * c

print product