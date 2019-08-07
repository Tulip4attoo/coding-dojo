from sys import exit
import math
from time import time


# generate n-first prime numbers.


#def prime_generate():
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
# print prime_list
#return prime_list

#prime_list = prime_generate(5000)

# print "%r" % prime_generate(100)

#def prime_factor(prime_list):
#n = int(raw_input("Ban muon phan tich so nao: "))
factor = m
prime_factorize = []
while factor > 1:
	for i in prime_list:
		if factor % i == 0:
			prime_factorize.append(i)
			factor = factor / i
			if factor < i:
				break
			else:
				continue
print prime_factorize[-1]

print("#1: ", time() - start)

	# print prime_list

#prime_factor(prime_list)

# print len([2,3,4])
# phan tich thua so nguyen to cuar so nhap vao