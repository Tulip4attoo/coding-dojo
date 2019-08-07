


prime_list = [2]

m = int(raw_input("Ban chon chan tren nao: "))
k = prime_list[-1]
while k < m:
	for i in prime_list:
		if k % i == 0:
			k = k + 1
			break
	else:
		prime_list.append(k)

list05 = []

for i in prime_list:
	power = 1
	while i ** (power + 1) < m:
		power = power + 1
	list05.append(i ** power)

number = 1

print list05

for i in list05:
	number = number * i

print number