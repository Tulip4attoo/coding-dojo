text = open("problem-12.txt", "r")

base_data = {}
line_data = []
n = -1
for line in text:
	line_data = str(line.split())
	n = n + 1
	base_data[n] = [line_data[i : i + 1] for i in range(2 , len(line_data) - 2, 1)]

sum_not_process_1 = {}
sum_not_process_2 = {}
sum_not_process_3 = {}
sum_not_process_4 = {}

for column in xrange(0, 50):
	temp_vari = 0
	for row in xrange(0, 100):
		temp_vari = temp_vari + int(base_data[row][column])
	sum_not_process_1[column] = temp_vari


sum_not_process_2[0] = sum_not_process_1[0] + sum_not_process_1[1] / 10 + sum_not_process_1[2] / 100
sum_not_process_2[48] = sum_not_process_1[48] % 10 + (sum_not_process_1[49] / 10) % 10
sum_not_process_2[49] = sum_not_process_1[49] % 10


for column in xrange(1, 48):
	temp_vari = 0
	sum_not_process_2[column] = sum_not_process_1[column] % 10 + (sum_not_process_1[column + 1] / 10) % 10 + sum_not_process_1[column + 2] / 100


sum_not_process_3[0] = sum_not_process_2[0] + sum_not_process_2[1] / 10 + sum_not_process_2[2] / 100
sum_not_process_3[48] = sum_not_process_2[48] % 10 + (sum_not_process_2[49] / 10) % 10
sum_not_process_3[49] = sum_not_process_2[49] % 10


for column in xrange(1, 48):
	temp_vari = 0
	sum_not_process_3[column] = sum_not_process_2[column] % 10 + (sum_not_process_2[column + 1] / 10) % 10 + sum_not_process_2[column + 2] / 100



sum_not_process_4[0] = sum_not_process_3[0] + sum_not_process_3[1] / 10 + sum_not_process_3[2] / 100
sum_not_process_4[48] = sum_not_process_3[48] % 10 + (sum_not_process_3[49] / 10) % 10
sum_not_process_4[49] = sum_not_process_3[49] % 10


for column in xrange(1, 48):
	temp_vari = 0
	sum_not_process_4[column] = sum_not_process_3[column] % 10 + (sum_not_process_3[column + 1] / 10) % 10 + sum_not_process_3[column + 2] / 100

print sum_not_process_1
print sum_not_process_2
print sum_not_process_3
print sum_not_process_4



first_ten_digits = str(sum_not_process_4[0])
for column in xrange(1, 8):
	first_ten_digits = first_ten_digits + str(sum_not_process_4[column])

print first_ten_digits









