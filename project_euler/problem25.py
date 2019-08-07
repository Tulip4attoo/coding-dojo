n = int(raw_input("Moi ban nhap so n: "))
fib = [1, 1, 2]
k = 2
l = 0
number = 10 ** (n - 1)
while l < number:
	l = fib[k - 1] + fib[k]
	fib.append(l)
	k = k + 1
print "So Fibonacci lon nhat nho hon %d la: %d" % (number, k + 1)