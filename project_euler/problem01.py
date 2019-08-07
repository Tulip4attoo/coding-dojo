sum = 0

for x in xrange(int(raw_input("Nhap n: "))):
	if (x % 3 == 0) | (x % 5 == 0):
		sum = sum + x

print sum