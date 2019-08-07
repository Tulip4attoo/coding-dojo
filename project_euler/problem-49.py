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

def check_permutations(n_1, n_2):
    list_sortedDigit_1 = list(str(n_1))
    list_sortedDigit_2 = list(str(n_2))
    list_sortedDigit_1.sort()
    list_sortedDigit_2.sort()
    if list_sortedDigit_1 == list_sortedDigit_2:
        return True
    return False

prime_list = my_sieve(10 ** 4) 
shortern_prime_list = [i for i in prime_list if i > 1000]

for ind_1 in xrange(0, len(shortern_prime_list)):
    for ind_2 in xrange(ind_1 + 1, len(shortern_prime_list)):
        prime_1 = shortern_prime_list[ind_1]
        prime_2 = shortern_prime_list[ind_2]
        next_number = - prime_1 + 2 * prime_2
        if next_number in shortern_prime_list:
            if (check_permutations(prime_1, prime_2) and 
                check_permutations(prime_2, next_number)):
                print(str(prime_1) + str(prime_2) + str(next_number))


print("--- %s seconds ---" % (time.time() - start_time))


