import time

start_time = time.time()

f = open('p022_names.txt', 'r')
abc = []
for line in f:
    abc = line.split()

strip_data = abc[0].replace('"', '')
name_list = strip_data.split(",")
name_list.sort()
result = 0
for ind in xrange(0, len(name_list)):
	value = 0
	for char in name_list[ind]:
		value += ord(char) - ord('A') + 1
	result += value * (ind + 1)

print(result)

print("--- %s seconds ---" % (time.time() - start_time))
