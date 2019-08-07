from time import time

start = time()

limit = int(raw_input("Ban phan tich so nao: "))
 
f = [True]*(limit)

for i in xrange( 2, int(limit ** 0.5) + 1):
	if not f[i]:
		continue
	else:	
		for j in xrange(i * i, limit, i):
			if f[j]: f[j]=False


primes = [2, 3]
sum = 5
for i in xrange(5, limit, 2):
	if f[i]:
		#primes.append(i)
		sum = sum + i

print sum
#print("number of primes:",len(primes))
#print("0-100:",primes[:25]) # check 1-100
#print("5 last primes",primes[-5:])
print("#1: ", time() - start)
