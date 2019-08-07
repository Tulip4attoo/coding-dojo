import time

start_time = time.time()

def calc_sum_square(number):
    str_number = str(number)
    return sum([int(i) ** 2 for i in str_number])

def get_root_sumSquare(number):
    psydo_root = number
    while psydo_root not in [1, 89]:
        # print('ting')
        psydo_root = calc_sum_square(psydo_root)
    return (psydo_root == 89)

count = 0
for number in xrange(1, 10 ** 7):
    count += get_root_sumSquare(number)

print("--- %s seconds ---" % (time.time() - start_time))
