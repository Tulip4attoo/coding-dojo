import time
from math import log


start_time = time.time()

# def the_9_end(a, b):
# 	dumb = int("".join(list(str(a))[- 9 : ])) + int("".join(list(str(b))[- 9 : ]))
# 	return int("".join(list(str(dumb))[- 9 : ]))

# def the_9_begin(a, b):
# 	dumb = int("".join(list(str(a))[ : 9])) + int("".join(list(str(b))[ : 9]))
# 	return int("".join(list(str(dumb))[ : 9]))

# a_begin, a_end = 3, 3
# b_begin, b_end = 2, 2
# count = 4

# def find_k():
# 	a_begin, a_end = 3, 3
# 	b_begin, b_end = 2, 2
# 	count = 4
# 	set_1_9 = set(map(str, range(1, 10)))
# 	for count in xrange(5, 10 ** 5):
# 		a_begin, b_begin = the_9_begin(a_begin, b_begin), a_begin
# 		a_end, b_end = the_9_end(a_end, b_end), a_end
# 		if set(str(a_begin)) == set_1_9:
# 			if set(str(a_end)) == set_1_9:
# 				print count
# 				return count


# we will use ways more simple algorithm 

# this shit is not working :'( should go back to first algo.
# change a bit, it will be ok.
# def find_k():
# 	a = 1
# 	b = 1
# 	count = 2
# 	set_1_9 = set(map(str, range(1, 10)))

# 	for count in xrange(3, 2 * 10 ** 5):
# 		a, b = b, a + b
# 		if set(list(str(b))[- 9 : ]) == set_1_9:
# 			if set(list(str(b))[ : 9]) == set_1_9:
# 				print count
# 				return count

# print find_k()


######

def the_9_end(a, b):
	dumb = int("".join(list(str(a))[- 9 : ])) + int("".join(list(str(b))[- 9 : ]))
	return int("".join(list(str(dumb))[- 9 : ]))

def the_9_begin(k):
	phi = (1 + 5 ** 0.5) / 2
	dumb = k * log(phi, 10)
	more_dumb = 10 ** (dumb - int(dumb) - 1) / 5 ** 0.5
	return list(str(more_dumb))[2 : 11]

# a_begin, a_end = 3, 3
# b_begin, b_end = 2, 2
# count = 4

def find_k():
	a_end = 3
	b_end = 2
	set_1_9 = set(map(str, range(1, 10)))
	for count in xrange(5, 10 ** 6):
		a_end, b_end = the_9_end(a_end, b_end), a_end
		if set(str(a_end)) == set_1_9:
			if set(the_9_begin(count)) == set_1_9:
				print count
				return count

print find_k()

print("--- %s seconds ---" % (time.time() - start_time))


