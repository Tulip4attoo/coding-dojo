from sys import exit
import math
from time import time



prime_list = [2]
m = int(raw_input("Ban phan tich so nao: "))
start = time()
k = prime_list[-1]
while prime_list[-1] < math.sqrt(m) + 1:
	for i in prime_list:
		if k % i == 0:
			k = k + 1
			break
		elif i > math.sqrt(k):
			prime_list.append(k)
			k = k + 1
			break

number_list = range(2, m / 100 + 1)
print("#1: ", time() - start)

#for i in prime_list:


#print prime_list