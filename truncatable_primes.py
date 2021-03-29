from math import sqrt


def isPrime(number):
    if number <= 1:
        return False

    for index in range(2, int(sqrt(number)) + 1):
        if number % index == 0:
            return False

    return True


def isTruncatable(prime):
    str_prime = str(prime)
    for index in range(len(str_prime)):
        right_trunc = int(str_prime[index:])
        left_trunc = int(str_prime[:index+1])

        if not(isPrime(right_trunc)) or not(isPrime(left_trunc)):
            return False

    return True


def truncatablePrimes():
    primes = []
    num_tracker = 10
    while True:
        if isTruncatable(num_tracker):
            primes.append(num_tracker)
        if len(primes) == 11:
            return sum(primes)

        num_tracker += 1


print(truncatablePrimes())
