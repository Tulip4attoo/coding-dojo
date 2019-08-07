text = open("problem-81.txt", "r")
temp_list = []
base_data = {}
n = 0
for line in text:
	temp_list = line.split(",")
	base_data[n] = map(int, temp_list)
	n = n + 1


# part 2: processing
# find the path + calculate the sum.

# create 2 stuff for storing results: square_sum and number_dict store sum of 
# number squares and order of chosen numbers.

processed_data = {}
for i in xrange(0, 80):
	for j in xrange(0, i + 1):
		dumb_list = []
		for k in xrange(79 - i, )
		processed_data[i] = 



square_sum = [0]
for k in range (0, n + 1):
	square_sum.append(0)

number_dict = {}
for k in range (0, n + 1):
	temp_number = []
	for j in range (0, k):
		temp_number.append(0)
	number_dict[k] = temp_number

# get the (path + sum) and put them into (number_dict + square_sum).
for k in range (0, n + 1):
	for j in range (0, n - k + 1):
		if square_sum[j] < square_sum[j + 1]:
			square_sum[j] = square_sum[j + 1] + base_data[n - k][j]
			number_dict[j] = [base_data[n - k][j]] + number_dict[j+1]			
		else:
			square_sum[j] = square_sum[j] + base_data[n - k][j]
			number_dict[j] = [base_data[n - k][j]] + number_dict[j]


# part 3
# write the output file.

file = open("output.txt", "w")
for i in range (0, n + 1):
	file.write("%d " % number_dict[0][i])
file.write("\n%d" % square_sum[0])
file.close()