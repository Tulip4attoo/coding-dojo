read_number = [0] * 1001
string = "hundred"
sum_text= 0

read_number[0] = ""
read_number[1] = "one"
read_number[2] = "two"
read_number[3] = "three"
read_number[4] = "four"
read_number[5] = "five"
read_number[6] = "six"
read_number[7] = "seven"
read_number[8] = "eight"
read_number[9] = "nine"
read_number[10] = "ten"
read_number[11] = "eleven"
read_number[12] = "twelve"
read_number[13] = "thirteen"
read_number[14] = "fourteen"
read_number[15] = "fifteen"
read_number[16] = "sixteen"
read_number[17] = "seventeen"
read_number[18] = "eighteen"
read_number[19] = "nineteen"
read_number[20] = "twenty"
read_number[30] = "thirty"
read_number[40] = "forty"
read_number[50] = "fifty"
read_number[60] = "sixty"
read_number[70] = "seventy"
read_number[80] = "eighty"
read_number[90] = "ninety"
read_number[1000] = "onethousand"

for number in xrange(20, 100):
	temp_value = ""
	temp_value = read_number[(number / 10 ) * 10] + read_number[(number % 10 )]
	read_number[number] = temp_value

for number in xrange(100, 1000):
	temp_value = ""
	if number % 100 == 0:
		temp_value = read_number[(number / 100)] + string
	else:
		temp_value = read_number[(number / 100)] + string + "and" + read_number[(number % 100)]
	read_number[number] = temp_value

for number in xrange(0, len(read_number)):
	sum_text = sum_text + len(read_number[number])

print sum_text