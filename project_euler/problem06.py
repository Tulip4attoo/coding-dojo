

def sum_square(floor):
	return (floor - 1) * floor * (floor + 1) / 3 + floor * (floor + 1) / 2

def square_sum(floor):
	return (floor + 1) ** 2 * floor ** 2 / 4

k = int(raw_input("nhap k: "))

print "%d" % (square_sum(k) - sum_square(k))