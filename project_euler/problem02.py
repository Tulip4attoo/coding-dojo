#class fib(object):

	#def fibonacci():
n = int(raw_input("Moi ban nhap so n: "))
fib = [1, 2, 3]
k = 2
l = 0
while l < n:
	l = fib[k - 1] + fib[k]
	fib.append(l)
	k = k + 1
print "So Fibonacci lon nhat nho hon %d la: %d" % (n, fib[k - 1])

#fib.fibonacci
sum = 0
for x in xrange(k):
	if x % 3 == 1:
		sum = sum + fib[x]

print fib[1]

print sum
