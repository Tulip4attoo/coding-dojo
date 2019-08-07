import time
import winsound


start_time = time.time()


def sum_divisors(number):
    result = 1
    divisor = 0
    for divisor in xrange(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            result += divisor + number / divisor
    if divisor ** 2 == number:
        result -= divisor
    return result

max_len = 0
longest_list = []

divisors_sum_list = [0, 0]

def get_chain(number):
    status = False
    current_number = number
    current_list = [number]
    while status != True:
        try:
            next_number = divisors_sum_list[current_number]
            if next_number == 1:
                return 0
            elif next_number > 10 ** 6:
                return 0
            elif next_number in current_list:
                current_list.append(next_number)
                return current_list
            elif next_number in longest_list:
                return 0
            else:
                current_list.append(next_number)
                current_number = next_number
        except:
            print(number)
            return 0

def get_true_list(number_list):
    for ind in xrange(0, len(number_list)):
        element = number_list[ind]
        if number_list.count(element) == 2:
            return number_list[ind : number_list.index(element, ind + 1)]
    return number_list

for number in xrange(2, 10 ** 6):
    divisors_sum_list.append(sum_divisors(number))

for number in xrange(2, 10 ** 6):
    curr_list = get_chain(number)
    if curr_list != 0:
        curr_list = get_true_list(curr_list)
        if len(curr_list) < len(longest_list):
            continue
        elif len(curr_list) == len(longest_list):
            if min(curr_list) < min(longest_list):
                longest_list = curr_list[:]
        else:
            longest_list = curr_list[:]


print(min(longest_list))

winsound.Beep(1000, 2500)
time.sleep(1)


print("--- %s seconds ---" % (time.time() - start_time))