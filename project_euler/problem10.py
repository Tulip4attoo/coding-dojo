import math
from time import time


prime_list = [2]
m = int(raw_input("Ban phan tich so nao: "))
start = time()
k = prime_list[-1]
while prime_list[-1] < m:
	for i in prime_list:
		if k % i == 0:
			k = k + 1
			break
		elif i > math.sqrt(k):
			prime_list.append(k)
			k = k + 1
			break
	#else:
		#prime_list.append(k)

sum = 0

for i in prime_list:
	sum = sum + i

print sum - prime_list[-1]

print("#1: ", time() - start)
