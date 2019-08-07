import math

palindromic_list = []

#should use str(number) == str(number)[:: - 1]
def check_palin(number):
	dumb = int("".join(list(str(number))[:: - 1]))
	return dumb == number

def dec_2_bin(number):
	dumb = int(math.log(number, 2)) + 1
	dumb_list = [0] * dumb
	dumb_2 = number
	for digit in xrange(dumb - 1, 0, - 1):
		dumb_list[digit] = int(((math.log(dumb_2 + 0.5, 2) - digit) > 0))
		dumb_2 = dumb_2 - int(((math.log(dumb_2 + 0.5, 2) - digit) > 0)) * 2 ** digit
	dumb_list[0] = number % 2 
	return int("".join(str(x) for x in dumb_list[:: - 1]))

for i in xrange(1, 1000000):
	if check_palin(i) == True:
		dumb = check_palin(dec_2_bin(i))
		if dumb == True:
			palindromic_list.append(i)

print sum(palindromic_list)