one_digit = 9 * 1
two_digit = one_digit + 90 * 2
three_digit = two_digit + 900 * 3
four_digit = three_digit + 9000 * 4
five_digit = four_digit + 90000 * 5
six_digit = five_digit + 900000 * 6
seven_digit = six_digit + 9000000 * 7

temp_value = 0
digit_value = 0

def digit_in_place(order):
	if order <= one_digit:
		digit_value = order
	elif order <= two_digit:
		temp_value = 10 ** 1 + (order - one_digit) / 2
		digit_value = str(temp_value)[(order - one_digit - 1) % 2]
	elif order <= three_digit:
		temp_value = 10 ** 2 + (order - two_digit) / 3
		digit_value = str(temp_value)[(order - two_digit - 1) % 3]
	elif order <= four_digit:
		temp_value = 10 ** 3 + (order - three_digit) / 4
		digit_value = str(temp_value)[(order - three_digit - 1) % 4]
	elif order <= five_digit:
		temp_value = 10 ** 4 + (order - four_digit) / 5
		digit_value = str(temp_value)[(order - four_digit - 1) % 5]
	elif order <= six_digit:
		temp_value = 10 ** 5 + (order - five_digit) / 6
		digit_value = str(temp_value)[(order - five_digit - 1) % 6]
	elif order <= seven_digit:
		temp_value = 10 ** 6 + (order - six_digit) / 7
		digit_value = str(temp_value)[(order - six_digit - 1) % 7]
	else:
		temp_value = 10 ** 7 + (order - seven_digit) / 8
		digit_value = str(temp_value)[(order - seven_digit - 1) % 8]
	return int(digit_value)

result = digit_in_place(1) * digit_in_place(10) * digit_in_place (100) * digit_in_place(1000) * digit_in_place (10000) * digit_in_place(100000) * digit_in_place(1000000)


print result