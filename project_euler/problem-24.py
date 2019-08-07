import time


start_time = time.time()

def find_millionth():
    count = 0
    for i_0 in xrange(0, 10):
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
                                            count += 1
                                            if count == 10 ** 6:
                                                print("%s%s%s%s%s%s%s%s%s%s"%(i_0, i_1, i_2, i_3, i_4, i_5, i_6, i_7, i_8, i_9))
                                                return

find_millionth()

print("--- %s seconds ---" % (time.time() - start_time))
