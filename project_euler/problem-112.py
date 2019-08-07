import time

start_time = time.time()

def is_decreasing(number):
    list_string = list(str(number))
    list_string_order = list(str(number))
    list_string_order.sort(reverse = True)
    return list_string == list_string_order

def is_increasing(number):
    list_string = list(str(number))
    list_string_order = list(str(number))
    list_string_order.sort(reverse = False)
    return list_string == list_string_order

def is_bouncy(number):
    if not is_increasing(number):
        if not is_decreasing(number):
            return True
    return False

# def count_bouncy(limit):
#     bouncy_count = 0
#     for number in xrange(0, limit + 1):
#         if is_bouncy(number):
#             bouncy_count += 1
#     return bouncy_count

status = False
bouncy_count = 0
number = 1

while status != True:
    number += 1
    if is_bouncy(number):
        bouncy_count += 1
    if bouncy_count * 100 == number * 99:
        status = True

print(number)

print("--- %s seconds ---" % (time.time() - start_time))


