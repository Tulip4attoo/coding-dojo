
palindrome = []

for m in xrange(0, 10, 1):
	for n in xrange(0, 10, 1):
		palindrome.append(900009 + 10010 * m + 1100 * n)


#print palindrome[1]


for m in xrange(9, -1, -1):
	#print m
	for n in xrange(9, -1, -1):
		if (900 + 10 * m + 7) * (900 + 10 * n + 7) in palindrome:
			print (900 + 10 * m + 7) * (900 + 10 * n + 7)
			break
		elif (900 + 10 * m + 1) * (900 + 10 * n + 9) in palindrome:
			print (900 + 10 * m + 1), (900 + 10 * n + 9)
			break
		elif (900 + 10 * m + 3) * (900 + 10 * n + 3) in palindrome:
			print (900 + 10 * m + 3), (900 + 10 * n + 3)
			break
	break
