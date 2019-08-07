text = open("problem-10.txt", "r")

abc = []
base_data = {}
n = -1
for line in text:
	abc = line.split()
	n = n + 1
	base_data[n] = map(int, abc)

largest_product = 0
updown_product = 1
leftright_product = 1
polly1_product = 1
polly2_product = 1

for column in range(0, 17):
	for row in range(3, 20):
		polly2_product = base_data[row][column] * base_data[row - 1][column + 1] * base_data[row - 2][column + 2] * base_data[row - 3][column + 3]
		if polly2_product > largest_product:
			largest_product = polly2_product

print largest_product

