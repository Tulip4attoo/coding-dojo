import time

start_time = time.time()

def factorial(number):
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    return factorial

def sum_factorial_digits(number):
    return sum([factorial(int(digit)) for digit in str(number)])

def get_length_chain(number):
    chain = [number]
    curr_number = sum_factorial_digits(number)
    while curr_number not in chain:
        chain.append(curr_number)
        curr_number = sum_factorial_digits(curr_number)
    return len(chain)

count = 0
for number in xrange(1, 10 ** 6):
    if get_length_chain(number) >= 60:
        count += 1

print(count)

print("--- %s seconds ---" % (time.time() - start_time))
