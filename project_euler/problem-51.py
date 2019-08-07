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

primes_list = my_sieve(10 ** 6)
part_str_prime_list = map(str, [i for i in primes_list if i > 5 * 10 ** 4])

def find_3_duplicated_digits(number):
    for digit in xrange(0, 10):
        if number.count(str(digit)) >= 3:
            return digit
    return -1

def get_3_number_of_list(number_list):
    result_list = []
    for n_1 in number_list:
        for n_2 in number_list:
            for n_3 in number_list:
                list_of_3 = [n_1, n_2, n_3]
                list_of_3.sort()
                if len(list_of_3) == 3:
                    if list_of_3 not in result_list:
                        result_list.append(list_of_3)
    return result_list

def replace_3_digit(number, dup3Digits_list):
    number_list = []
    for str_digit in map(str, xrange(0, 10)):
        new_number = number[ : dup3Digits_list[0]] + str_digit + \
            number[dup3Digits_list[0] + 1 : dup3Digits_list[1]] + str_digit + \
            number[dup3Digits_list[1] + 1 : dup3Digits_list[2]] + str_digit + \
            number[dup3Digits_list[2] + 1 : ] 
        number_list.append(new_number)
    return number_list

def get_dupDigit_ind_list(number, digit):
    result_list = []
    for ind in xrange(0, len(number)):
        if number[ind] == str(digit):
            result_list.append(ind)
    return result_list

def find_smallest_in_8():
    for prime in part_str_prime_list:
        digit = find_3_duplicated_digits(prime)
        if digit == -1:
            continue
        else:
            print(prime)
            digit_ind_list = get_dupDigit_ind_list(prime, digit)
            three_ind_list = get_3_number_of_list(digit_ind_list)
            for a_3_ind in three_ind_list:
                count = 0
                replaced_number_list = replace_3_digit(prime, a_3_ind)
                for psudo_prime in replaced_number_list:
                    if psudo_prime in part_str_prime_list:
                        count += 1
                    if count == 8:
                        return prime

a = find_smallest_in_8()
print(a)

print("--- %s seconds ---" % (time.time() - start_time))


