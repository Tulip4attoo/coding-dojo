import utils

prime_list = utils.sieve(1e6)


def check_devided(p):
    """

    """
    power_of_power = 9
    mod = 10
    for i in range(power_of_power):
        mod = mod ** 10 % p
    if mod % p == 1:
        return True
    else:
        return False

result = 0
count = 0

for p in prime_list[2:]: #because it not devided by 2 and 3
    check = check_devided(p)
    if check:
        result += p
        count += 1
        if count == 40:
            print(result)
