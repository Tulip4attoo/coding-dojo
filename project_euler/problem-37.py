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

def is_left_truncatable(prime, primes_list):
    for ind in xrange(1, len(prime)):
        if prime[: len(prime) - ind ] not in primes_list:
            return False
    return True


def is_right_truncatable(prime, primes_list):
    if len(prime) == 1:
        return False
    for ind in xrange(1, len(prime)):
        if prime[ind : ] not in primes_list:
            return False
    return True

primes_list = my_sieve(10 ** 6)
primes_list.remove(1)
primes_str_list = map(str, primes_list)

def get_sum_trunPrimes(primes_list):
    count = 0
    sum_trunPrimes = 0
    for prime in primes_list:
        if is_right_truncatable(prime, primes_list):
            if is_left_truncatable(prime, primes_list):
                print(prime)
                count += 1
                sum_trunPrimes += int(prime)
                if count == 11:
                    return sum_trunPrimes

print(get_sum_trunPrimes(primes_str_list))

print("--- %s seconds ---" % (time.time() - start_time))


