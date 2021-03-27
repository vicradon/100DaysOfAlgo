from math import sqrt


def isPrime(num):
    for index in range(2, int(sqrt(num)) + 1):
        if num % index == 0:
            return False

    return True


def isCircularPrime(number):
    str_number = str(number)
    primePermutations = {
        int(str_number[index:] + str_number[:index]) for index in range(len(str_number))}

    for prime in primePermutations:
        if not(isPrime(prime)):
            return False

    return True


def getCircularPrimes(limit):
    circularPrimes = []

    for num in range(2, limit):
        if isCircularPrime(num):
            circularPrimes.append(num)

    return len(circularPrimes)


print(getCircularPrimes(int(1e6)))
