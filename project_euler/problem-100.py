import time

start_time = time.time()

# by doing some math (that cannot write here, of course), I find the formula 
# of b (total disks) is: b[i + 1] = 6 * b[i] - b[i - 1] - 2, same as a (blue disks)
# it will be easy peasy

def find_a_b(number):
	for n in xrange(1, 10 ** 8):
		b = number + n
		a = int(b / 2 ** 0.5) + 1
		if (a - 1) * a * 2 == (b - 1) * b:
			return a, b

def find_2_first_a_b():
	c = find_a_b(1)
	d = find_a_b(c[1])
	return c, d

def find_blue_disks(number):
	a_list = [find_2_first_a_b()[0][0], find_2_first_a_b()[1][0]]
	b_list = [find_2_first_a_b()[0][1], find_2_first_a_b()[1][1]]
	for i in xrange(1, 1000):
		a_list.append(a_list[i] * 6 - a_list[i - 1] - 2)
		b_list.append(b_list[i] * 6 - b_list[i - 1] - 2)
		if b_list[i] > number:
			return a_list[i]

print find_blue_disks(10 ** 12)

print("--- %s seconds ---" % (time.time() - start_time))
