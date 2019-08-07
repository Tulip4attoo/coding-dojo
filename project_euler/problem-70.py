import time


def my_sieve(n):
    dumb_list = range(0, n)
    limit = int(n ** 0.5)
    for i in xrange(2, limit):
        if dumb_list[i]:
            dumb = (n - 1) / i - 1
            dumb_list[i + i :: i] = [0] * dumb
    return filter(None, dumb_list)

list_prime = my_sieve(10 ** 4) 

start_time = time.time()

def factorize(number):
    dumb = number
    factorize_list = []
    for i in xrange(1, len(list_prime)):
        factor = list_prime[i]
        if dumb % factor == 0:
            dumb = dumb / factor
            factorize_list.append(factor)
            while dumb % factor == 0:
                dumb = dumb / factor
        if dumb < factor:
            return factorize_list

def phi(number):
    phi_value = number
    factor_list = factorize(number)
    for i in factor_list:
        phi_value = phi_value * (i - 1) / i
    return phi_value

def check_permutation(a, b):
    dumb_a = list(str(a))
    dumb_a.sort()
    dumb_b = list(str(b))
    dumb_b.sort()
    if dumb_a == dumb_b:
        return True
    else:
        return False

min_ratio = 2
result = 0
for n in xrange(2, 10 ** 5):
    dumb = phi(n)
#   if check_permutation(dumb, n) == True:
#       if min_ratio > (n / dumb):
#           min_ratio = n / dumb
#           result = n

print result 

print("--- %s seconds ---" % (time.time() - start_time))
