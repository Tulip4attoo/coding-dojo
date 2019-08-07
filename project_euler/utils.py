def sieve(floor):
    """
    implementation of prime sieve algo
    return a list of primes under a floor number
    """
    dumb_list = [i for i in range(floor)]
    limit = int(floor ** 0.5) + 1
    for i in range(2, limit):
        if dumb_list[i]:
            dumb = (floor - 1) // i - 1
            dumb_list[i + i :: i] = [0] * dumb
    # because the list include number 1
    # we filter the 0s out
    return (list(filter(None, dumb_list))[1:])
