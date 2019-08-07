import time

start_time = time.time()

def calc_factorial(number):
    factorial_value = 1
    for i in xrange(1, number + 1):
        factorial_value *= i
    return factorial_value

def calc_C(n_factorial, n, r):
    r_factorial = calc_factoriwal(r)
    n_minus_r_factorial = calc_factorial(n - r)
    return n_factorial / (r_factorial * n_minus_r_factorial)

def find_min_r(number):
    number_factorial = calc_factorial(number)
    for r in xrange(1, number):
        if calc_C(number_factorial, number, r) > 10 ** 6:
            return r
    return 0

def calc_number_for_n(number):
    r_min = find_min_r(number)
    if r_min == 0:
        return 0
    else:
        return number - 2 * r_min + 1

count = 0
for number in xrange(2, 101):
    count += calc_number_for_n(number)

print(count)
print("--- %s seconds ---" % (time.time() - start_time))
