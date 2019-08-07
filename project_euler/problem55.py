import time

count = 0
dumb_list = []
dumb = 0

def reverse(number):
	dumb_list = list(str(number))[::-1]
	dumb = int(''.join(dumb_list))
	return dumb
	
def palindrome_check(number):
	if (number == reverse(number)):
		return 1
	else:
		return 0

def lychrel_check(number):
	dumb = number
	dumb_count = 0
	while (dumb_count < 50):
		dumb = dumb + reverse(dumb)
		if (palindrome_check(dumb) == 1):
			return 0
		dumb_count = dumb_count + 1
	return 1
	
now = time.time()

for number in xrange(1, 10000):
	count = count + lychrel_check(number)


print count
print (time.time() - now)
