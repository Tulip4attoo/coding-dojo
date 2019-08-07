import time

start_time = time.time()

# max_value = 1
value_at_max = 1

def my_sieve(n):
    dumb_list = range(0, n)
    limit = int(n ** 0.5)
    for i in xrange(2, limit):
        if dumb_list[i]:
            dumb = (n - 1) / i - 1
            dumb_list[i + i :: i] = [0] * dumb
    return filter(None, dumb_list)

list_prime = my_sieve(1000)

for number in list_prime:
    value_at_max *= number
    if value_at_max > 10 ** 6:
        print(value_at_max / number, number)
        break

# def get_phi(number):


# for n in xrange(2, 10 ** 6 + 1):
#     if max_value < (float(n) / phi(n)):
#         value_at_max = n
#         max_value = float(n) / phi(n)

# print(value_at_max)

print("--- %s seconds ---" % (time.time() - start_time))
