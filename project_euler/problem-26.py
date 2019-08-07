import time


start_time = time.time()

def is_devidable_by_e10(number):
    if 10 ** 10 % number == 0:
        return True
    else:
        return False

def find_len_recurring_cycle(number):
    devidable = False
    power = 1
    while devidable != True:
        if (10 ** power - 1) % number == 0:
            devidable = True
        else:
            power += 1
    return power

def modify_number(number):
    modified_number = number
    while modified_number % 2 == 0:
        modified_number /= 2
    while modified_number % 5 == 0:
        modified_number /= 5
    return modified_number

max_len = 1
number_max_len = 1
for number in xrange(2, 1000):
    if is_devidable_by_e10(number):
        continue
    else:
        modified_number = modify_number(number)
        current_len = find_len_recurring_cycle(modified_number)
        if current_len > max_len:
            max_len = current_len
            number_max_len = number

print(number_max_len)


print("--- %s seconds ---" % (time.time() - start_time))


