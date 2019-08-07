"""time = 1

k = int(raw_input("nhap so: "))

for i in xrange(1, k + 1):
	time = time * i"""
time = 2 ** 1000
joinexample = ','.join("%d" % time)

splitjoin = joinexample.split(',')

sum = 0

for i in splitjoin:
	sum = sum + int(i)

print sum