import time

start_time = time.time()

CEILING = 5 * 10 ** 5

def my_sieve(n):
    dumb_list = range(0, n)
    limit = int(n ** 0.5)
    for i in xrange(2, limit):
        if dumb_list[i]:
            dumb = (n - 1) / i - 1
            dumb_list[i + i :: i] = [0] * dumb
    return filter(None, dumb_list)

primes_list = my_sieve(CEILING) 


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

max_root_list = []
max_all_list = []

def rAll

def root

for number in xrange(2, CEILING):
    if number in primes_list:
        max_root_list.append(0)
        max_all_list.append(root_a_prime(number))
    else:
        max_root = root_a_composite(number)
        max_root_list.append(max_root)
        max_all_list.append(max_root)

def sumDigitalRootFactor(N):
    return max_root_list[N]

print result 

print("--- %s seconds ---" % (time.time() - start_time))
