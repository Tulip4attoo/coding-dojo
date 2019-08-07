import time

start_time = time.time()

def return_Pandigital(number):
    full_number = str(number) + str(2 * number)
    if len(set(full_number)) == 9:
        if '0' not in full_number:
            return int(full_number)
    else:
        return 0

max_pandigital_number = 918273645

for number in xrange(9100, 10 ** 4):
    pandigital = return_Pandigital(number)
    if pandigital != 0:
        if pandigital > max_pandigital_number:
            max_pandigital_number = pandigital

print(max_pandigital_number)

print("--- %s seconds ---" % (time.time() - start_time))


