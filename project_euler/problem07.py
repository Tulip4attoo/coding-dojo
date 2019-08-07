import math

prime_list = [2]
m = int(raw_input("Ban phan tich so nao: "))
k = prime_list[-1]
while len(prime_list) < m:
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

print prime_list[-1]