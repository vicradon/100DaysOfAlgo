import math


def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True


def tenThousandthAndOnePrime():
    primes = []
    count = 2
    while True:
        if isPrime(count):
            primes.append(count)
            if len(primes) == 10001:
                return primes[-1]
            count += 1
        else:
            count += 1


print(tenThousandthAndOnePrime())
