import time


start_time = time.time()

date_of_1900_dict = {}
date_of_20th_dict = {}

def check_leap_year(year):
    if (year % 4) != 0:
        return False
    elif (year % 100) != 0:
        return True
    elif (year % 400) != 0:
        return False
    else:
        return True

for year in xrange(1900, 2001):
    date_of_20th_dict[year] = {}
    for month in xrange(1, 13):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            date_list = range(1, 32)
        elif month != 2:
            date_list = range(1, 31)
        else:
            if check_leap_year(year):
                date_list = range(1, 30)
            else:
                date_list = range(1, 29)
        date_of_20th_dict[year][month] = date_list

date_of_1900_dict = date_of_20th_dict[1900]

count_1900 = 0
count_20th = 0
day_of_week = 0

for year in xrange(1900, 2001):
    for month in xrange(1, 13):
        for date in date_of_20th_dict[year][month]:
            day_of_week += 1
            if day_of_week == 6:
                day_of_week = -1
                if date == 1:
                    count_20th += 1
                    if year == 1900:
                        count_1900 += 1

print(count_20th - count_1900)

print("--- %s seconds ---" % (time.time() - start_time))


