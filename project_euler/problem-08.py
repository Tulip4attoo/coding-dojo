text = open('problem-08.txt', 'r')
data_string = text.read().replace("\n", "")

largest_product = 0

for start_string in range(0, len(data_string) - 13):
	thirteen_product = int(data_string[start_string])
	
	for i in range(1, 13):
		thirteen_product = thirteen_product * int(data_string[start_string + i])
	
	if thirteen_product > largest_product:
		largest_product = thirteen_product

print largest_product