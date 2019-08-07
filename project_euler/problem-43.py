import time


start_time = time.time()

sum_value = 0

def check_number(number):
	if len(set(str(number))) != 10:
		return False
	if int("".join(list(str(number))[1 : 4])) % 2 == 0:
		if int("".join(list(str(number))[2 : 5])) % 3 == 0:
			if int("".join(list(str(number))[3 : 6])) % 5 == 0:
				if int("".join(list(str(number))[4 : 7])) % 7 == 0:
					if int("".join(list(str(number))[5 : 8])) % 11 == 0:
						if int("".join(list(str(number))[6 : 9])) % 13 == 0:
							if int("".join(list(str(number))[7 : 10])) % 17 == 0:
								return True
	return False

# it take too long, again...
# for i in xrange(10 ** 9, 10 ** 10):
# 	if check_number(i) == True:
# 		sum_value = sum_value + i

count = 0
for i_0 in xrange(1, 10):
    for i_1 in xrange(0, 10):
        if i_1 in [i_0]:
            continue
        for i_2 in xrange(0, 10):
            if i_2 in [i_0, i_1]:
                continue
            for i_3 in xrange(0, 10):
                if i_3 in [i_0, i_1, i_2]:
                    continue
                for i_4 in xrange(0, 10):
                    if i_4 in [i_0, i_1, i_2, i_3]:
                        continue
                    for i_5 in xrange(0, 10):
                        if i_5 in [i_0, i_1, i_2, i_3, i_4]:
                            continue
                        for i_6 in xrange(0, 10):
                            if i_6 in [i_0, i_1, i_2, i_3, i_4, i_5]:
                                continue
                            for i_7 in xrange(0, 10):
                                if i_7 in [i_0, i_1, i_2, i_3, i_4, i_5, i_6]:
                                    continue
                                for i_8 in xrange(0, 10):
                                    if i_8 in [i_0, i_1, i_2, i_3, i_4, i_5, i_6, i_7]:
                                        continue
                                    for i_9 in xrange(0, 10):
                                        if i_9 in [i_0, i_1, i_2, i_3, i_4, i_5, i_6, i_7, i_8]:
                                            continue
                                        number = int("%s%s%s%s%s%s%s%s%s%s"%(i_0, i_1, i_2, i_3, i_4, i_5, i_6, i_7, i_8, i_9))
                                        if check_number(number) == True:
                                            print(number)
                                            sum_value += number

print sum_value

print("--- %s seconds ---" % (time.time() - start_time))
