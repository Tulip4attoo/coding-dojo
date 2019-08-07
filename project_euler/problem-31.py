count = 0


current_value1 = 200
dumb_value = current_value1

for eur_1 in xrange(current_value1 / 100, - 1, - 1):
	current_value2 = current_value1 - eur_1 * 100
	for pound_50 in xrange(current_value2 / 50, - 1, - 1):
		current_value3 = current_value2 - pound_50 * 50
		for pound_20 in xrange(current_value3 / 20, - 1, - 1):
			current_value4 = current_value3 - pound_20 * 20
			for pound_10 in xrange(current_value4 / 10, - 1, - 1):
				current_value5 = current_value4 - pound_10 * 10
				for pound_05 in xrange(current_value5 / 05, - 1, - 1):
					current_value6 = current_value5 - pound_05 * 05
					for pound_02 in xrange(current_value6 / 02, - 1, - 1):
						count = count + 1

print count