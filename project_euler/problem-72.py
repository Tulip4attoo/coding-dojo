import time


start_time = time.time()

def my_sieve(n):
	dumb_list = range(0, n)
	limit = int(n ** 0.5)
	for i in xrange(2, limit):
		if dumb_list[i]:
			dumb = (n - 1) / i - 1
			dumb_list[i + i :: i] = [0] * dumb
	return filter(None, dumb_list)

list_prime = my_sieve(1000) 

def factorize(number, dumb_list):
	dumb = number
	factorize_dict = {}
	for i in xrange(1, len(dumb_list)):
		factor = dumb_list[i]
		if dumb % factor == 0:
			dumb = dumb / factor
			factorize_dict[dumb_list[i]] = 1
			while dumb % factor == 0:
				dumb = dumb / factor
				factorize_dict[dumb_list[i]] = factorize_dict[dumb_list[i]] + 1
		if dumb < factor:
			break
	if len(factorize_dict) == 0:
		return {number: 1}
	elif dumb > 1000:
		factorize_dict[dumb] = 1
	return factorize_dict

def phi(number):
	dumb_factorize = factorize(number, list_prime)
	dumb = number
	for i in dumb_factorize:
		dumb = dumb * (i - 1) / i
	return dumb

so_much_dumb = 1

# we will find the first number which dont have p ** n with n > 1
for i in xrange(1, 3000001):
	so_much_dumb = so_much_dumb * list_prime[i]
	if phi(so_much_dumb) * 94744 < (so_much_dumb - 1) * 15499:
		print so_much_dumb
		break

# after this we find the lowest number
less_dumb = so_much_dumb / 29

for i in xrange(2, 29):
	if phi(less_dumb * i) * 94744 < (less_dumb * i - 1) * 15499:
		print less_dumb * i
		break


print("--- %s seconds ---" % (time.time() - start_time))


